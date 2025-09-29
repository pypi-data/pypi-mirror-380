import json
import logging
import sys
import importlib.metadata
import yaml
import time
import copy
import os
import hashlib
import ipaddress

from typing import Union, Dict, List, Optional, Any
from norfab.models import Result
from norfab.core.worker import NFPWorker, WorkerWatchDog, Task, Job
from norfab.core.inventory import merge_recursively
from norfab.core.exceptions import UnsupportedPluginError
from norfab.models.nornir import GetNornirHosts, GetNornirHostsResponse
from nornir import InitNornir
from nornir_salt.plugins.tasks import (
    netmiko_send_commands,
    scrapli_send_commands,
    napalm_send_commands,
    napalm_configure,
    netmiko_send_config,
    scrapli_send_config,
    nr_test,
    connections as nr_connections,
)
from nornir_salt.plugins.functions import (
    FFun_functions,
    FFun,
    ResultSerializer,
    HostsKeepalive,
    InventoryFun,
)
from nornir_salt.plugins.processors import (
    TestsProcessor,
    ToFileProcessor,
    DiffProcessor,
    DataProcessor,
    NorFabEventProcessor,
)
from nornir_napalm.plugins.tasks import napalm_get
from nornir_netmiko.tasks import netmiko_file_transfer
from nornir_salt.utils.pydantic_models import modelTestsProcessorSuite
from threading import Lock
from norfab.clients.shell_clients.nornir.nornir_picle_shell_cli import NorniCliInput

SERVICE = "nornir"

log = logging.getLogger(__name__)

# ----------------------------------------------------------------------
# Nornir Service watchdog class
# -----------------------------------------------------------------------


class WatchDog(WorkerWatchDog):
    """
    Class to monitor Nornir worker performance.

    Args:
        worker (Worker): The worker instance that this NornirWorker will manage.

    Attributes:
        worker (Worker): The worker instance being monitored.
        connections_idle_timeout (int): Timeout value for idle connections.
        connections_data (dict): Dictionary to store connection use timestamps.
        started_at (float): Timestamp when the watchdog was started.
        idle_connections_cleaned (int): Counter for idle connections cleaned.
        dead_connections_cleaned (int): Counter for dead connections cleaned.
        watchdog_tasks (list): List of tasks for the watchdog to run in a given order.
    """

    def __init__(self, worker):
        super().__init__(worker)
        self.worker = worker
        self.connections_idle_timeout = worker.inventory.get(
            "connections_idle_timeout", None
        )
        self.connections_data = {}  # store connections use timestamps
        self.started_at = time.time()

        # stats attributes
        self.idle_connections_cleaned = 0
        self.dead_connections_cleaned = 0

        # list of tasks for watchdog to run in given order
        self.watchdog_tasks = [
            self.connections_clean,
            self.connections_keepalive,
        ]

    def stats(self) -> Dict:
        """
        Collects and returns statistics about the worker.

        Returns:
            dict: A dictionary containing the following keys:

                - runs (int): The number of runs executed by the worker.
                - timestamp (str): The current time in a human-readable format.
                - alive (int): The time in seconds since the worker started.
                - dead_connections_cleaned (int): The number of dead connections cleaned.
                - idle_connections_cleaned (int): The number of idle connections cleaned.
                - worker_ram_usage_mbyte (float): The current RAM usage of the worker in megabytes.
        """
        return {
            "runs": self.runs,
            "timestamp": time.ctime(),
            "alive": int(time.time() - self.started_at),
            "dead_connections_cleaned": self.dead_connections_cleaned,
            "idle_connections_cleaned": self.idle_connections_cleaned,
            "worker_ram_usage_mbyte": self.get_ram_usage(),
        }

    def configuration(self) -> Dict:
        """
        Returns the configuration settings for the worker.

        Returns:
            Dict: A dictionary containing the configuration settings:

                - "watchdog_interval" (int): The interval for the watchdog timer.
                - "connections_idle_timeout" (int): The timeout for idle connections.
        """
        return {
            "watchdog_interval": self.watchdog_interval,
            "connections_idle_timeout": self.connections_idle_timeout,
        }

    def connections_get(self) -> Dict:
        """
        Retrieve the current connections data.

        Returns:
            Dict: A dictionary containing the current connections data.
        """
        return {
            "connections": self.connections_data,
        }

    def connections_update(self, nr, plugin: str) -> None:
        """
        Function to update connection use timestamps for each host

        Args:
            nr: Nornir object
            plugin: connection plugin name
        """
        conn_stats = {
            "last_use": None,
            "last_keepealive": None,
            "keepalive_count": 0,
        }
        for host_name in nr.inventory.hosts:
            self.connections_data.setdefault(host_name, {})
            self.connections_data[host_name].setdefault(plugin, conn_stats.copy())
            self.connections_data[host_name][plugin]["last_use"] = time.ctime()
        log.info(
            f"{self.worker.name} - updated connections use timestamps for '{plugin}'"
        )

    def connections_clean(self):
        """
        Cleans up idle connections based on the configured idle timeout.

        This method checks for connections that have been idle for longer than the
        specified `connections_idle_timeout` and disconnects them. The behavior
        varies depending on the value of `connections_idle_timeout`:

        - If `connections_idle_timeout` is None, no connections are disconnected.
        - If `connections_idle_timeout` is 0, all connections are disconnected.
        - If `connections_idle_timeout` is greater than 0, only connections that
          have been idle for longer than the specified timeout are disconnected.

        The method acquires a lock to ensure thread safety while modifying the
        connections data. It logs the disconnection actions and updates the
        `idle_connections_cleaned` counter.

        Raises:
            Exception: If an error occurs while attempting to disconnect idle
            connections, an error message is logged.
        """
        # dictionary keyed by plugin name and value as a list of hosts
        disconnect = {}
        if not self.worker.connections_lock.acquire(blocking=False):
            return
        try:
            # if idle timeout not set, connections don't age out
            if self.connections_idle_timeout is None:
                disconnect = {}
            # disconnect all connections for all hosts
            elif self.connections_idle_timeout == 0:
                disconnect = {"all": list(self.connections_data.keys())}
            # only disconnect aged/idle connections
            elif self.connections_idle_timeout > 0:
                for host_name, plugins in self.connections_data.items():
                    for plugin, conn_data in plugins.items():
                        last_use = time.mktime(time.strptime(conn_data["last_use"]))
                        age = time.time() - last_use
                        if age > self.connections_idle_timeout:
                            disconnect.setdefault(plugin, [])
                            disconnect[plugin].append(host_name)
            # run task to disconnect connections for aged hosts
            for plugin, hosts in disconnect.items():
                if not hosts:
                    continue
                aged_hosts = FFun(self.worker.nr, FL=hosts)
                aged_hosts.run(task=nr_connections, call="close", conn_name=plugin)
                log.debug(
                    f"{self.worker.name} watchdog, disconnected '{plugin}' "
                    f"connections for '{', '.join(hosts)}'"
                )
                self.idle_connections_cleaned += len(hosts)
                # wipe out connections data if all connection closed
                if plugin == "all":
                    self.connections_data = {}
                    break
                # remove disconnected plugin from host's connections_data
                for host in hosts:
                    self.connections_data[host].pop(plugin)
                    if not self.connections_data[host]:
                        self.connections_data.pop(host)
        except Exception as e:
            msg = f"{self.worker.name} - watchdog failed to close idle connections, error: {e}"
            log.error(msg)
        finally:
            self.worker.connections_lock.release()

    def connections_keepalive(self):
        """
        Keepalive connections and clean up dead connections if any.

        This method performs the following tasks:

        - If `connections_idle_timeout` is 0, it returns immediately without performing any actions.
        - Attempts to acquire a lock on `worker.connections_lock` to ensure thread safety.
        - Logs a debug message indicating that the keepalive process is running.
        - Uses `HostsKeepalive` to check and clean up dead connections, updating the `dead_connections_cleaned` counter.
        - Removes connections that are no longer present in the Nornir inventory.
        - Removes hosts from `connections_data` if they have no remaining connections.
        - Updates the keepalive statistics for each connection plugin, including the last keepalive time and keepalive count.
        - Logs an error message if an exception occurs during the keepalive process.
        - Releases the lock on `worker.connections_lock` in the `finally` block to ensure it is always released.

        Raises:
            Exception: If an error occurs during the keepalive process, it is logged as an error.
        """
        if self.connections_idle_timeout == 0:  # do not keepalive if idle is 0
            return
        if not self.worker.connections_lock.acquire(blocking=False):
            return
        try:
            log.debug(f"{self.worker.name} - watchdog running connections keepalive")
            stats = HostsKeepalive(self.worker.nr)
            self.dead_connections_cleaned += stats["dead_connections_cleaned"]
            # remove connections that are no longer present in Nornir inventory
            for host_name, host_connections in self.connections_data.items():
                for connection_name in list(host_connections.keys()):
                    if not self.worker.nr.inventory.hosts[host_name].connections.get(
                        connection_name
                    ):
                        self.connections_data[host_name].pop(connection_name)
            # remove host if no connections left
            for host_name in list(self.connections_data.keys()):
                if self.connections_data[host_name] == {}:
                    self.connections_data.pop(host_name)
            # update connections statistics
            for plugins in self.connections_data.values():
                for plugin in plugins.values():
                    plugin["last_keepealive"] = time.ctime()
                    plugin["keepalive_count"] += 1
        except Exception as e:
            msg = f"{self.worker.name} - watchdog HostsKeepalive check error: {e}"
            log.error(msg)
        finally:
            self.worker.connections_lock.release()


class NornirWorker(NFPWorker):
    """
    NornirWorker class for managing Nornir Service tasks.

    Args:
        inventory (str): Path to the inventory file.
        broker (str): Broker address.
        worker_name (str): Name of the worker.
        exit_event (threading.Event, optional): Event to signal worker exit. Defaults to None.
        init_done_event (threading.Event, optional): Event to signal initialization completion. Defaults to None.
        log_level (str, optional): Logging level. Defaults to None.
        log_queue (object, optional): Queue for logging. Defaults to None.

    Attributes:
        init_done_event (threading.Event): Event to signal initialization completion.
        tf_base_path (str): Base path for files folder saved using `tf` processor.
        connections_lock (threading.Lock): Lock for managing connections.
        nornir_inventory (dict): Inventory data for Nornir.
        watchdog (WatchDog): Watchdog instance for monitoring.
    """

    nr = None
    nornir_inventory = {}

    def __init__(
        self,
        inventory: str,
        broker: str,
        worker_name: str,
        exit_event=None,
        init_done_event=None,
        log_level: str = None,
        log_queue: object = None,
    ):
        super().__init__(
            inventory, broker, SERVICE, worker_name, exit_event, log_level, log_queue
        )
        self.init_done_event = init_done_event
        self.tf_base_path = os.path.join(self.base_dir, "tf")

        # misc attributes
        self.connections_lock = Lock()

        # initiate Nornir
        self.refresh_nornir(job=Job())

        # initiate watchdog
        self.watchdog = WatchDog(self)
        self.watchdog.start()

        # run startup hooks
        for f in self.inventory.hooks.get("nornir-startup", []):
            f["function"](self, *f.get("args", []), **f.get("kwargs", {}))

        if self.init_done_event is not None:
            self.init_done_event.set()

        log.info(f"{self.name} - Started")

    def worker_exit(self):
        """
        Executes all functions registered under the "nornir-exit" hook in the inventory.

        This method iterates through the list of hooks associated with the "nornir-exit"
        key in the inventory's hooks.

        For each hook, it calls the function specified in the hook, passing the current
        instance (`self`) as the first argument, followed by any additional positional
        and keyword arguments specified in the hook.
        """
        # run exit hooks
        for f in self.inventory.hooks.get("nornir-exit", []):
            f["function"](self, *f.get("args", []), **f.get("kwargs", {}))

    def init_nornir(self, inventory: dict) -> None:
        """
        Initializes the Nornir automation framework with the provided inventory.

        This method first closes any existing Nornir connections if present, optionally emitting a progress event.
        It then creates a new Nornir instance using the supplied inventory dictionary, which should contain
        configuration for logging, runner, hosts, groups, defaults, and user-defined settings.

        Args:
            inventory (dict): A dictionary containing Nornir inventory and configuration options.
            progress (bool, optional): If True, emits progress events during initialization. Defaults to False.

        Returns:
            None
        """
        # clean up existing Nornir instance
        if self.nr is not None and self.nr.inventory.hosts:
            self.nr.close_connections()

        # initiate Nornir
        self.nr = InitNornir(
            logging=inventory.get("logging", {"enabled": False}),
            runner=inventory.get("runner", {}),
            inventory={
                "plugin": "DictInventory",
                "options": {
                    "hosts": inventory.get("hosts", {}),
                    "groups": inventory.get("groups", {}),
                    "defaults": inventory.get("defaults", {}),
                },
            },
            user_defined=inventory.get("user_defined", {}),
        )

    @Task(fastapi={"methods": ["POST"]})
    def refresh_nornir(
        self,
        job: Job,
        progress: bool = False,
    ) -> Result:
        """
        Refreshes the Nornir instance by reloading the inventory from configured sources.

        This method performs the following steps:

            1. Loads the inventory configuration from the broker.
            2. If Netbox is specified in the inventory, pulls inventory data from Netbox.
            3. If Containerlab is specified in the inventory, pulls inventory data from Containerlab.
            4. Initializes the Nornir instance with the refreshed inventory.
            5. Optionally emits progress events at each stage if `progress` is True.

        Args:
            job: NorFab Job object containing relevant metadata
            progress (bool, optional): If True, emits progress events during the refresh process. Defaults to False.

        The inventory configuration is expected to be a dictionary with the following keys:

        - "logging": A dictionary specifying logging configuration (default: {"enabled": False}).
        - "runner": A dictionary specifying runner options (default: {}).
        - "hosts": A dictionary specifying host details (default: {}).
        - "groups": A dictionary specifying group details (default: {}).
        - "defaults": A dictionary specifying default values (default: {}).
        - "user_defined": A dictionary specifying user-defined options (default: {}).

        Returns:
            Result: A Result object indicating the outcome of the refresh operation.
        """
        ret = Result(task=f"{self.name}:refresh_nornir", result=True)

        # get inventory from broker
        self.nornir_worker_inventory = self.load_inventory()

        # pull Nornir inventory from Netbox
        if "netbox" in self.nornir_worker_inventory:
            self.nornir_inventory_load_netbox(job=job)
            job.event("Pulled Nornir inventory data from Netbox")

        # pull Nornir inventory from Containerlab
        if "containerlab" in self.nornir_worker_inventory:
            self.nornir_inventory_load_containerlab(
                job=job,
                **self.nornir_worker_inventory["containerlab"],
                re_init_nornir=False,
            )
            job.event("Pulled Nornir inventory data from Containerlab")

        job.event(f"Pulled inventories, refreshing Nornir instance")

        self.init_nornir(self.nornir_worker_inventory)

        job.event("Nornir instance refreshed")

        return ret

    @Task(fastapi={"methods": ["POST"]})
    def nornir_inventory_load_netbox(
        self,
        job: Job,
        progress: bool = False,
    ) -> Result:
        """
        Queries inventory data from Netbox Service and merges it into the Nornir inventory.

        This function checks if there is Netbox data in the inventory and retrieves
        it if available. It handles retries and timeout configurations, and ensures
        that necessary filters or devices are specified. The retrieved inventory
        data is then merged into the existing Nornir inventory.

        Args:
            job: NorFab Job object containing relevant metadata

        Logs:
            - Critical: If the inventory has no hosts, filters, or devices defined.
            - Error: If no inventory data is returned from Netbox.
            - Warning: If the Netbox instance returns no hosts data.
        """
        ret = Result(task=f"{self.name}:nornir_inventory_load_netbox", result=True)

        # form Netbox inventory load arguments
        if isinstance(self.nornir_worker_inventory.get("netbox"), dict):
            kwargs = self.nornir_worker_inventory["netbox"]
        elif self.nornir_worker_inventory.get("netbox") is True:
            kwargs = {}
        retry = max(1, kwargs.pop("retry", 3))
        retry_timeout = max(10, kwargs.pop("retry_timeout", 100))

        # check if need to add devices list
        if "filters" not in kwargs and "devices" not in kwargs:
            if self.nornir_worker_inventory.get("hosts"):
                kwargs["devices"] = list(self.nornir_worker_inventory["hosts"])
            else:
                log.warning(
                    f"{self.name} - inventory has no hosts, Netbox filters or devices defined"
                )
                return

        nb_inventory_data = self.client.run_job(
            service="netbox",
            task="get_nornir_inventory",
            workers="any",
            kwargs=kwargs,
            timeout=retry_timeout * retry,
            retry=retry,
        )

        if nb_inventory_data is None:
            msg = f"{self.name} - Netbox get_nornir_inventory no inventory returned"
            log.error(msg)
            raise RuntimeError(msg)

        # merge Netbox inventory into Nornir inventory
        for wname, wdata in nb_inventory_data.items():
            if wdata["failed"] is False and wdata["result"].get("hosts"):
                merge_recursively(self.nornir_worker_inventory, wdata["result"])
                break
        else:
            msg = (
                f"{self.name} - Netbox worker(s) "
                f"'{', '.join(list(nb_inventory_data.keys()))}' returned no hosts data."
            )
            log.error(msg)
            raise RuntimeError(msg)

        job.event(f"Pulled Nornir inventory from Netbox")

        return ret

    @Task(fastapi={"methods": ["POST"]})
    def nornir_inventory_load_containerlab(
        self,
        job: Job,
        lab_name: str = None,
        groups: Union[None, list] = None,
        clab_workers: str = "all",
        use_default_credentials: bool = True,
        progress: bool = False,
        dry_run: bool = False,
        re_init_nornir: bool = True,
    ) -> Result:
        """
        Pulls the Nornir inventory from a Containerlab lab instance and merges it with the
        existing Nornir inventory.

        Args:
            job: NorFab Job object containing relevant metadata
            lab_name (str): The name of the Containerlab lab to retrieve the inventory from.
            groups (list, optional): A list of group names to include into the hosts' inventory.
            use_default_credentials (bool): Whether to use default credentials for the hosts.

        Returns:
            Result: A Result object indicating the success or failure of the operation.
                    If successful, the Nornir inventory is updated with the retrieved data.

        Notes:
            - The method retrieves inventory data from a Containerlab lab using a client job.
            - If the retrieved inventory contains host data, it is merged into the existing
              Nornir inventory using the `merge_recursively` function.
            - If no inventory or host data is returned, the method logs an error and marks
              the operation as failed.
            - After successful merging of inventory, Nornir instance is re-initialized with the
              updated inventory.
        """
        groups = groups or []
        ret = Result(
            task=f"{self.name}:nornir_inventory_load_containerlab", result=True
        )
        job.event(
            f"Pulling Containerlab '{lab_name or 'all'}' inventory from '{clab_workers}' workers"
        )

        clab_inventory_data = self.client.run_job(
            service="containerlab",
            task="get_nornir_inventory",
            workers=clab_workers,
            kwargs={
                "lab_name": lab_name,
                "groups": groups,
                "use_default_credentials": use_default_credentials,
            },
        )

        if clab_inventory_data is None:
            msg = f"{self.name} - Containerlab get_nornir_inventory no data returned"
            log.error(msg)
            raise RuntimeError(msg)

        job.event(f"Pulled Containerlab '{lab_name or 'all'}' lab inventory")

        if dry_run is True:
            ret.result = {w: r["result"] for w, r in clab_inventory_data.items()}
            return ret

        for wname, wdata in clab_inventory_data.items():
            # use inventory from first worker that returned hosts data
            if wdata["failed"] is False and wdata["result"].get("hosts"):
                merge_recursively(self.nornir_worker_inventory, wdata["result"])
                break
        else:
            msg = (
                f"{self.name} - Containerlab worker(s) '{', '.join(list(clab_inventory_data.keys()))}' "
                f"returned no hosts data for '{lab_name}' lab."
            )
            log.error(msg)
            raise RuntimeError(msg)

        job.event(
            f"Merged Containerlab '{lab_name or 'all'}' lab inventory with Nornir runtime inventory"
        )

        if re_init_nornir is True:
            self.init_nornir(self.nornir_worker_inventory)
            job.event("Nornir instance re-initialized")

        return ret

    def _add_processors(self, nr, kwargs: Dict, job: Job):
        """
        Add various processors to the Nornir object based on the provided keyword arguments.

        Args:
            nr (Nornir): The Nornir object to which processors will be added.
            kwargs (dict): A dictionary of keyword arguments specifying which
                processors to add and their configurations.

        Keyword Args:
            tf (str, optional): Path to the file for ToFileProcessor.
            tf_skip_failed (bool, optional): Whether to skip failed tasks in ToFileProcessor.
            diff (str, optional): Configuration for DiffProcessor.
            diff_last (int, optional): Number of last diffs to keep for DiffProcessor.
            dp (list, optional): Configuration for DataProcessor.
            xml_flake (str, optional): Pattern for xml_flake function in DataProcessor.
            match (str, optional): Pattern for match function in DataProcessor.
            before (int, optional): Number of lines before match in DataProcessor.
            run_ttp (str, optional): Template for run_ttp function in DataProcessor.
            ttp_structure (str, optional): Structure for run_ttp results in DataProcessor.
            remove_tasks (bool, optional): Whether to remove tasks in DataProcessor and TestsProcessor.
            tests (list, optional): Configuration for TestsProcessor.
            subset (list, optional): Subset of tests for TestsProcessor.
            failed_only (bool, optional): Whether to include only failed tests in TestsProcessor.
            xpath (str, optional): XPath expression for DataProcessor.
            jmespath (str, optional): JMESPath expression for DataProcessor.
            iplkp (str, optional): IP lookup configuration for DataProcessor.
            ntfsm (bool, optional): Whether to use ntc-templates TextFSM parsing in DataProcessor.
            progress (bool, optional): Whether to emit progress events using NorFabEventProcessor.

        Returns:
            Nornir: The Nornir object with the added processors.
        """
        processors = []

        # extract parameters
        tf = kwargs.pop("tf", None)  # to file
        tf_skip_failed = kwargs.pop("tf_skip_failed", False)  # to file
        diff = kwargs.pop("diff", "")  # diff processor
        diff_last = kwargs.pop("diff_last", 1) if diff else None  # diff processor
        dp = kwargs.pop("dp", [])  # data processor
        xml_flake = kwargs.pop("xml_flake", "")  # data processor xml_flake function
        match = kwargs.pop("match", "")  # data processor match function
        before = kwargs.pop("before", 0)  # data processor match function
        run_ttp = kwargs.pop("run_ttp", None)  # data processor run_ttp function
        ttp_structure = kwargs.pop(
            "ttp_structure", "flat_list"
        )  # data processor run_ttp function
        remove_tasks = kwargs.pop("remove_tasks", True)  # tests and/or run_ttp
        tests = kwargs.pop("tests", None)  # tests
        subset = kwargs.pop("subset", [])  # tests
        failed_only = kwargs.pop("failed_only", False)  # tests
        xpath = kwargs.pop("xpath", "")  # xpath DataProcessor
        jmespath = kwargs.pop("jmespath", "")  # jmespath DataProcessor
        iplkp = kwargs.pop("iplkp", "")  # iplkp - ip lookup - DataProcessor
        ntfsm = kwargs.pop("ntfsm", False)  # ntfsm - ntc-templates TextFSM parsing
        progress = kwargs.pop(
            "progress", True
        )  # Emit progress events using NorFabEventProcessor

        # add processors if any
        if dp:
            processors.append(DataProcessor(dp))
        if iplkp:
            processors.append(
                DataProcessor(
                    [
                        {
                            "fun": "iplkp",
                            "use_dns": True if iplkp == "dns" else False,
                            "use_csv": iplkp if iplkp else False,
                        }
                    ]
                )
            )
        if xml_flake:
            processors.append(
                DataProcessor([{"fun": "xml_flake", "pattern": xml_flake}])
            )
        if xpath:
            processors.append(
                DataProcessor(
                    [{"fun": "xpath", "expr": xpath, "recover": True, "rm_ns": True}]
                )
            )
        if jmespath:
            processors.append(DataProcessor([{"fun": "jmespath", "expr": jmespath}]))
        if match:
            processors.append(
                DataProcessor([{"fun": "match", "pattern": match, "before": before}])
            )
        if run_ttp:
            processors.append(
                DataProcessor(
                    [
                        {
                            "fun": "run_ttp",
                            "template": run_ttp,
                            "res_kwargs": {"structure": ttp_structure},
                            "remove_tasks": remove_tasks,
                        }
                    ]
                )
            )
        if ntfsm:
            processors.append(DataProcessor([{"fun": "ntfsm"}]))
        if tests:
            processors.append(
                TestsProcessor(
                    tests=tests,
                    remove_tasks=remove_tasks,
                    failed_only=failed_only,
                    build_per_host_tests=True,
                    subset=subset,
                    render_tests=False,
                )
            )
        if diff:
            processors.append(
                DiffProcessor(
                    diff=diff,
                    last=int(diff_last),
                    base_url=self.tf_base_path,
                    index=self.name,
                )
            )
        if progress:
            processors.append(NorFabEventProcessor(job=job))
        # append ToFileProcessor as the last one in the sequence
        if tf and isinstance(tf, str):
            processors.append(
                ToFileProcessor(
                    tf=tf,
                    base_url=self.tf_base_path,
                    index=self.name,
                    max_files=1000,
                    skip_failed=tf_skip_failed,
                    tf_index_lock=None,
                )
            )

        return nr.with_processors(processors)

    def load_job_data(self, job_data: Any):
        """
        Helper function to download job data YAML files and load it.

        Args:
            job_data (str): job data NorFab file path to download and load using YAML.

        Returns:
            data: The job data loaded from the YAML string.

        Raises:
            FileNotFoundError: If the job data is a URL and the file download fails.
        """
        if self.is_url(job_data):
            job_data = self.fetch_file(job_data)
            if job_data is None:
                msg = f"{self.name} - '{job_data}' job data file download failed"
                raise FileNotFoundError(msg)
            job_data = yaml.safe_load(job_data)

        return job_data

    # ----------------------------------------------------------------------
    # Nornir Service Jinja2 Filters
    # ----------------------------------------------------------------------

    def jinja2_network_hosts(self, network: str, pfxlen: bool = False) -> list:
        """
        Custom Jinja2 filter that return a list of hosts for a given IP network.

        Args:
            network (str): The network address in CIDR notation.
            pfxlen (bool, optional): If True, include the prefix length
                in the returned host addresses. Defaults to False.

        Returns:
            list: A list of host addresses as strings. If pfxlen is True,
                each address will include the prefix length.
        """
        ret = []
        ip_interface = ipaddress.ip_interface(network)
        prefixlen = ip_interface.network.prefixlen
        for ip in ip_interface.network.hosts():
            ret.append(f"{ip}/{prefixlen}" if pfxlen else str(ip))
        return ret

    def jinja2_nb_create_ip(
        self, prefix: str, device: str = None, interface: str = None, **kwargs
    ) -> str:
        """
        Jinja2 filter to get or create next available IP address from
        prefix using Netbox service.
        """
        kwargs["prefix"] = prefix
        kwargs["device"] = device
        kwargs["interface"] = interface
        reply = self.client.run_job(
            "netbox",
            "create_ip",
            kwargs=kwargs,
            workers="any",
            timeout=30,
        )
        # reply is a dict of {worker_name: results_dict}
        res = list(reply.values())[0]
        if res["failed"]:
            raise RuntimeError(res["messages"])
        return res["result"]["address"]

    def jinja2_nb_create_prefix(
        self, parent: str, description: str, prefixlen: int = 30, **kwargs
    ) -> str:
        """
        Jinja2 filter to get or create next available prefix from
        parent prefix using Netbox service.
        """
        kwargs["parent"] = parent
        kwargs["description"] = description
        kwargs["prefixlen"] = prefixlen
        reply = self.client.run_job(
            "netbox",
            "create_prefix",
            kwargs=kwargs,
            workers="any",
            timeout=30,
        )
        # reply is a dict of {worker_name: results_dict}
        res = list(reply.values())[0]
        if res["failed"]:
            raise RuntimeError(res["messages"])

        return res["result"]["prefix"]

    def jinja2_call_netbox(self, netbox_task: str) -> callable:
        """
        Returns a callable function to execute arbitrary NetBox service task.
        """

        def call_netbox(*args, **kwargs) -> dict:
            reply = self.client.run_job(
                "netbox",
                netbox_task,
                args=args,
                kwargs=kwargs,
                workers="any",
                timeout=300,
            )
            res = list(reply.values())[0]

            # check if has an error
            if res["failed"]:
                raise RuntimeError(res["messages"])

            # return result for single host only
            if len(kwargs.get("devices", [])) == 1:
                return res["result"][kwargs["devices"][0]]
            # return full results
            else:
                return res["result"]

        return call_netbox

    def add_jinja2_netbox(self) -> Dict:
        """
        Aggregates Jinja2 NetBox-related methods and functions into a dictionary
        for the ease of use within Jinja2 templates.
        """
        return {
            "get_connections": self.jinja2_call_netbox("get_connections"),
            "get_interfaces": self.jinja2_call_netbox("get_interfaces"),
            "get_circuits": self.jinja2_call_netbox("get_circuits"),
            "get_devices": self.jinja2_call_netbox("get_devices"),
            "rest": self.jinja2_call_netbox("rest"),
            "graphql": self.jinja2_call_netbox("graphql"),
            "create_ip": self.jinja2_nb_create_ip,
            "create_prefix": self.jinja2_nb_create_prefix,
        }

    def add_jinja2_filters(self) -> Dict:
        """
        Adds custom filters for use in Jinja2 templates using `|` syntaxis.

        Returns:
            dict (Dict): A dictionary where the keys are the names of the filters
                and the values are the corresponding filter functions.

                - "nb_create_ip": Method to get the next IP address.
                - "nb_create_prefix": Method to get next available prefix.
                - "network_hosts": Method to get IP network hosts.
        """
        return {
            "netbox.create_ip": self.jinja2_nb_create_ip,
            "netbox.create_prefix": self.jinja2_nb_create_prefix,
            "network_hosts": self.jinja2_network_hosts,
        }

    # ----------------------------------------------------------------------
    # Nornir Service Functions that exposed for calling
    # ----------------------------------------------------------------------

    @Task(
        fastapi={"methods": ["GET"]},
        input=GetNornirHosts,
        output=GetNornirHostsResponse,
    )
    def get_nornir_hosts(self, details: bool = False, **kwargs: dict) -> Result:
        """
        Retrieve a list of Nornir hosts managed by this worker.

        Args:
            job: NorFab Job object containing relevant metadata
            details (bool): If True, returns detailed information about each host.
            **kwargs (dict): Hosts filters to apply when retrieving hosts.

        Returns:
            List[Dict]: A list of hosts with optional detailed information.
        """
        filters = {k: kwargs.pop(k) for k in list(kwargs.keys()) if k in FFun_functions}
        filtered_nornir = FFun(self.nr, **filters)
        if details:
            return Result(
                result={
                    host_name: {
                        "platform": str(host.platform),
                        "hostname": str(host.hostname),
                        "port": str(host.port),
                        "groups": [str(g) for g in host.groups],
                        "username": str(host.username),
                    }
                    for host_name, host in filtered_nornir.inventory.hosts.items()
                }
            )
        else:
            return Result(result=list(filtered_nornir.inventory.hosts))

    @Task(fastapi={"methods": ["GET"]})
    def get_inventory(self, **kwargs: dict) -> Result:
        """
        Retrieve running Nornir inventory for requested hosts

        Args:
            job: NorFab Job object containing relevant metadata
            **kwargs (dict): Fx filters used to filter the inventory.

        Returns:
            Dict: A dictionary representation of the filtered inventory.
        """
        filters = {k: kwargs.pop(k) for k in list(kwargs.keys()) if k in FFun_functions}
        filtered_nornir = FFun(self.nr, **filters)
        return Result(result=filtered_nornir.inventory.dict(), task="get_inventory")

    @Task(fastapi={"methods": ["GET"]})
    def get_version(self) -> Result:
        """
        Retrieve the versions of various libraries and system information.

        This method collects the version information of a predefined set of libraries
        and system details such as the Python version and platform. It attempts to
        import each library and fetch its version. If a library is not found, it is
        skipped.

        Args:
            job: NorFab Job object containing relevant metadata

        Returns:
            dict: a dictionary with the library names as keys and their respective
                version numbers as values. If a library is not found, its value will be
                an empty string.
        """
        libs = {
            "norfab": "",
            "scrapli": "",
            "scrapli-netconf": "",
            "scrapli-community": "",
            "paramiko": "",
            "netmiko": "",
            "napalm": "",
            "nornir": "",
            "ncclient": "",
            "nornir-netmiko": "",
            "nornir-napalm": "",
            "nornir-scrapli": "",
            "nornir-utils": "",
            "tabulate": "",
            "xmltodict": "",
            "puresnmp": "",
            "pygnmi": "",
            "pyyaml": "",
            "jmespath": "",
            "jinja2": "",
            "ttp": "",
            "nornir-salt": "",
            "lxml": "",
            "ttp-templates": "",
            "ntc-templates": "",
            "cerberus": "",
            "pydantic": "",
            "requests": "",
            "textfsm": "",
            "N2G": "",
            "dnspython": "",
            "pythonping": "",
            "python": sys.version.split(" ")[0],
            "platform": sys.platform,
        }
        # get version of packages installed
        for pkg in libs.keys():
            try:
                libs[pkg] = importlib.metadata.version(pkg)
            except importlib.metadata.PackageNotFoundError:
                pass

        return Result(result=libs)

    @Task(fastapi={"methods": ["GET"]})
    def get_watchdog_stats(self) -> Result:
        """
        Retrieve the statistics from the watchdog.

        Args:
            job: NorFab Job object containing relevant metadata

        Returns:
            Result: An object containing the statistics from the watchdog.
        """
        return Result(result=self.watchdog.stats())

    @Task(fastapi={"methods": ["GET"]})
    def get_watchdog_configuration(self) -> Result:
        """
        Retrieves the current configuration of the watchdog.

        Args:
            job: NorFab Job object containing relevant metadata

        Returns:
            Result: An object containing the watchdog configuration.
        """
        return Result(result=self.watchdog.configuration())

    @Task(fastapi={"methods": ["GET"]})
    def get_watchdog_connections(self) -> Result:
        """
        Retrieve the list of connections curently managed by watchdog.

        Args:
            job: NorFab Job object containing relevant metadata

        Returns:
            Result: An instance of the Result class containing the current
                watchdog connections.
        """
        return Result(result=self.watchdog.connections_get())

    @Task(fastapi={"methods": ["POST"]})
    def task(self, job: Job, plugin: str, **kwargs) -> Result:
        """
        Execute a Nornir task plugin.

        This method dynamically imports and executes a specified Nornir task plugin,
        using the provided arguments and keyword arguments. The `plugin` attribute
        can refer to a file to fetch from a file service, which must contain a function
        named `task` that accepts a Nornir task object as the first positional argument.

        Example of a custom task function file:

        ```python
        # define connection name for RetryRunner to properly detect it
        CONNECTION_NAME = "netmiko"

        # create task function
        def task(nornir_task_object, **kwargs):
            pass
        ```

        Note:
            The `CONNECTION_NAME` must be defined within the custom task function file if
            RetryRunner is in use. Otherwise, the connection retry logic is skipped, and
            connections to all hosts are initiated simultaneously up to the number of `num_workers`.

        Args:
            job: NorFab Job object containing relevant metadata
            plugin (str): The path to the plugin function to import, or a NorFab
                URL to download a custom task or template URL that resolves to a file.
            **kwargs: Additional arguments to pass to the specified task plugin.

        Keyword Args:
            add_details (bool): If True, adds task execution details to the results.
            to_dict (bool): If True, returns results as a dictionary. Defaults to True.
            Filters: Any additional keyword arguments that match FFun_functions will be used as filters.

        Returns:
            Result: An instance of the Result class containing the task execution results.

        Raises:
            FileNotFoundError: If the specified plugin file cannot be downloaded.
        """
        # extract attributes
        add_details = kwargs.pop("add_details", False)  # ResultSerializer
        to_dict = kwargs.pop("to_dict", True)  # ResultSerializer
        filters = {k: kwargs.pop(k) for k in list(kwargs.keys()) if k in FFun_functions}
        ret = Result(task=f"{self.name}:task", result={} if to_dict else [])

        # download task from broker and load it
        if plugin.startswith("nf://"):
            function_text = self.fetch_file(plugin)
            if function_text is None:
                raise FileNotFoundError(
                    f"{self.name} - '{plugin}' task plugin download failed"
                )

            # load task function running exec
            globals_dict = {}
            exec(function_text, globals_dict, globals_dict)
            task_function = globals_dict["task"]
        # import task function
        else:
            # below same as "from nornir.plugins.tasks import task_fun as task_function"
            task_fun = plugin.split(".")[-1]
            module = __import__(plugin, fromlist=[""])
            task_function = getattr(module, task_fun)

        self.nr.data.reset_failed_hosts()  # reset failed hosts
        filtered_nornir = FFun(self.nr, **filters)  # filter hosts

        # check if no hosts matched
        if not filtered_nornir.inventory.hosts:
            msg = (
                f"{self.name} - nothing to do, no hosts matched by filters '{filters}'"
            )
            log.debug(msg)
            ret.messages.append(msg)
            ret.status = "no_match"
            return ret

        nr = self._add_processors(filtered_nornir, kwargs, job)  # add processors

        # run task
        log.debug(f"{self.name} - running Nornir task '{plugin}', kwargs '{kwargs}'")
        with self.connections_lock:
            result = nr.run(task=task_function, **kwargs)

        ret.failed = result.failed  # failed is true if any of the hosts failed
        ret.result = ResultSerializer(result, to_dict=to_dict, add_details=add_details)

        self.watchdog.connections_clean()

        return ret

    @Task(
        fastapi={"methods": ["POST"]},
        input=NorniCliInput,
        mcp={"name": "send_show_commands"},
    )
    def cli(
        self,
        job: Job,
        commands: Union[str, list] = None,
        plugin: str = "netmiko",
        dry_run: bool = False,
        run_ttp: str = None,
        job_data: Any = None,
        to_dict: bool = True,
        add_details: bool = False,
        **kwargs,
    ) -> Result:
        """
        Task to collect/retrieve show commands output from network devices using
        Command Line Interface (CLI).

        Args:
            job: NorFab Job object containing relevant metadata
            commands (list, optional): List of commands to send to devices or URL to a file or template
                URL that resolves to a file.
            plugin (str, optional): Plugin name to use. Valid options are
                ``netmiko``, ``scrapli``, ``napalm``.
            dry_run (bool, optional): If True, do not send commands to devices,
                just return them.
            run_ttp (str, optional): TTP Template to run.
            job_data (str, optional): URL to YAML file with data or dictionary/list
                of data to pass on to Jinja2 rendering context.
            to_dict (bool, optional): If True, returns results as a dictionary.
            add_details (bool, optional): If True, adds task execution details
                to the results.
            **kwargs: Additional arguments to pass to the specified task plugin.

        Returns:
            dict: A dictionary with the results of the CLI task.

        Raises:
            UnsupportedPluginError: If the specified plugin is not supported.
            FileNotFoundError: If the specified TTP template or job data file
            cannot be downloaded.
        """
        job_data = job_data or {}
        filters = {k: kwargs.pop(k) for k in list(kwargs.keys()) if k in FFun_functions}
        timeout = job.timeout * 0.9
        ret = Result(task=f"{self.name}:cli", result={} if to_dict else [])

        # decide on what send commands task plugin to use
        if plugin == "netmiko":
            task_plugin = netmiko_send_commands
            if kwargs.get("use_ps"):
                kwargs.setdefault("timeout", timeout)
            else:
                kwargs.setdefault("read_timeout", timeout)
        elif plugin == "scrapli":
            task_plugin = scrapli_send_commands
            kwargs.setdefault("timeout_ops", timeout)
        elif plugin == "napalm":
            task_plugin = napalm_send_commands
        else:
            raise UnsupportedPluginError(f"Plugin '{plugin}' not supported")

        self.nr.data.reset_failed_hosts()  # reset failed hosts
        filtered_nornir = FFun(self.nr, **filters)  # filter hosts

        # check if no hosts matched
        if not filtered_nornir.inventory.hosts:
            msg = (
                f"{self.name} - nothing to do, no hosts matched by filters '{filters}'"
            )
            log.debug(msg)
            ret.messages.append(msg)
            ret.status = "no_match"
            return ret

        # download TTP template
        if self.is_url(run_ttp):
            downloaded = self.fetch_file(run_ttp)
            kwargs["run_ttp"] = downloaded
            if downloaded is None:
                msg = f"{self.name} - TTP template download failed '{run_ttp}'"
                raise FileNotFoundError(msg)
        # use TTP template as is - inline template or ttp://xyz path
        elif run_ttp:
            kwargs["run_ttp"] = run_ttp

        # download job data
        job_data = self.load_job_data(job_data)

        nr = self._add_processors(filtered_nornir, kwargs, job)  # add processors

        # render commands using Jinja2 on a per-host basis
        if commands:
            commands = commands if isinstance(commands, list) else [commands]
            for host in nr.inventory.hosts.values():
                rendered = self.jinja2_render_templates(
                    templates=commands,
                    context={
                        "host": host,
                        "norfab": self.client,
                        "job_data": job_data,
                        "netbox": self.add_jinja2_netbox(),
                    },
                    filters=self.add_jinja2_filters(),
                )
                host.data["__task__"] = {"commands": rendered}

        # run task
        log.debug(
            f"{self.name} - running cli commands '{commands}', kwargs '{kwargs}', is cli dry run - '{dry_run}'"
        )
        if dry_run is True:
            result = nr.run(
                task=nr_test, use_task_data="commands", name="dry_run", **kwargs
            )
        else:
            with self.connections_lock:
                result = nr.run(task=task_plugin, **kwargs)

        ret.failed = result.failed  # failed is true if any of the hosts failed
        ret.result = ResultSerializer(result, to_dict=to_dict, add_details=add_details)

        # remove __task__ data
        for host_name, host_object in nr.inventory.hosts.items():
            _ = host_object.data.pop("__task__", None)

        self.watchdog.connections_update(nr, plugin)
        self.watchdog.connections_clean()

        return ret

    @Task(
        fastapi={"methods": ["POST"]},
        mcp={"name": "configure_devices"},
    )
    def cfg(
        self,
        job: Job,
        config: Union[str, list],
        plugin: str = "netmiko",
        dry_run: bool = False,
        to_dict: bool = True,
        add_details: bool = False,
        job_data: Any = None,
        **kwargs,
    ) -> Result:
        """
        Task to send configuration commands to devices using Command Line Interface (CLI).

        Args:
            job: NorFab Job object containing relevant metadata
            config (list): List of commands to send to devices or URL to a file or template
                URL that resolves to a file.
            plugin (str, optional): Plugin name to use. Valid options are:

                - netmiko - use Netmiko to configure devices
                - scrapli - use Scrapli to configure devices
                - napalm - use NAPALM to configure devices

            dry_run (bool, optional): If True, will not send commands to devices but just return them.
            to_dict (bool, optional): If True, returns results as a dictionary. Defaults to True.
            add_details (bool, optional): If True, adds task execution details to the results.
            job_data (str, optional): URL to YAML file with data or dictionary/list of data to pass on to Jinja2 rendering context.
            **kwargs: Additional arguments to pass to the task plugin.

        Returns:
            dict: A dictionary with the results of the configuration task.

        Raises:
            UnsupportedPluginError: If the specified plugin is not supported.
            FileNotFoundError: If the specified job data file cannot be downloaded.
        """
        config = config if isinstance(config, list) else [config]
        filters = {k: kwargs.pop(k) for k in list(kwargs.keys()) if k in FFun_functions}
        ret = Result(task=f"{self.name}:cfg", result={} if to_dict else [])

        # decide on what send commands task plugin to use
        if plugin == "netmiko":
            task_plugin = netmiko_send_config
        elif plugin == "scrapli":
            task_plugin = scrapli_send_config
        elif plugin == "napalm":
            task_plugin = napalm_configure
        else:
            raise UnsupportedPluginError(f"Plugin '{plugin}' not supported")

        self.nr.data.reset_failed_hosts()  # reset failed hosts
        filtered_nornir = FFun(self.nr, **filters)  # filter hosts

        # check if no hosts matched
        if not filtered_nornir.inventory.hosts:
            msg = (
                f"{self.name} - nothing to do, no hosts matched by filters '{filters}'"
            )
            log.debug(msg)
            ret.messages.append(msg)
            ret.status = "no_match"
            return ret

        job_data = self.load_job_data(job_data)

        nr = self._add_processors(filtered_nornir, kwargs, job)  # add processors

        # render config using Jinja2 on a per-host basis
        for host in nr.inventory.hosts.values():
            rendered = self.jinja2_render_templates(
                templates=config,
                context={
                    "host": host,
                    "norfab": self.client,
                    "job_data": job_data,
                    "netbox": self.add_jinja2_netbox(),
                },
                filters=self.add_jinja2_filters(),
            )
            host.data["__task__"] = {"config": rendered}

        # run task
        log.debug(
            f"{self.name} - sending config commands '{config}', kwargs '{kwargs}', is dry_run - '{dry_run}'"
        )
        if dry_run is True:
            result = nr.run(
                task=nr_test, use_task_data="config", name="dry_run", **kwargs
            )
        else:
            with self.connections_lock:
                result = nr.run(task=task_plugin, **kwargs)

        ret.failed = result.failed  # failed is true if any of the hosts failed
        ret.result = ResultSerializer(result, to_dict=to_dict, add_details=add_details)

        # remove __task__ data
        for host_name, host_object in nr.inventory.hosts.items():
            _ = host_object.data.pop("__task__", None)

        self.watchdog.connections_update(nr, plugin)
        self.watchdog.connections_clean()

        return ret

    @Task(fastapi={"methods": ["POST"]})
    def test(
        self,
        job: Job,
        suite: Union[list, str],
        subset: str = None,
        dry_run: bool = False,
        remove_tasks: bool = True,
        failed_only: bool = False,
        return_tests_suite: bool = False,
        job_data: Any = None,
        **kwargs,
    ) -> Result:
        """
        Function to test networks using a suite of tests.

        Args:
            job: NorFab Job object containing relevant metadata
            suite (Union[list, str]): URL Path to YAML file with tests or a list of test definitions
                or template URL that resolves to a file path.
            subset (str, optional): List or string with comma-separated non-case-sensitive glob
                patterns to filter tests by name. Ignored if dry_run is True.
            dry_run (bool, optional): If True, returns produced per-host tests suite content only.
            remove_tasks (bool, optional): If False, results will include other tasks output.
            failed_only (bool, optional): If True, returns test results for failed tests only.
            return_tests_suite (bool, optional): If True, returns rendered per-host tests suite
                content in addition to test results using a dictionary with ``results`` and ``suite`` keys.
            job_data (str, optional): URL to YAML file with data or dictionary/list of data
                to pass on to Jinja2 rendering context.
            **kwargs: Any additional arguments to pass on to the Nornir service task.

        Returns:
            dict: A dictionary containing the test results. If `return_tests_suite` is True,
                the dictionary will contain both the test results and the rendered test suite.

        Note:
            Result `failed` attribute is set to True if any of the tests failed for any of the hosts.

        Raises:
            RuntimeError: If there is an error in rendering the Jinja2 templates or loading the YAML.
        """
        tests = {}  # dictionary to hold per-host test suites
        add_details = kwargs.get("add_details", False)  # ResultSerializer
        to_dict = kwargs.get("to_dict", True)  # ResultSerializer
        filters = {k: kwargs.pop(k) for k in list(kwargs.keys()) if k in FFun_functions}
        ret = Result(task=f"{self.name}:test", result={} if to_dict else [])
        suites = {}  # dictionary to hold combined test suites

        self.nr.data.reset_failed_hosts()  # reset failed hosts
        filtered_nornir = FFun(self.nr, **filters)  # filter hosts

        # check if no hosts matched
        if not filtered_nornir.inventory.hosts:
            msg = (
                f"{self.name} - nothing to do, no hosts matched by filters '{filters}'"
            )
            log.debug(msg)
            ret.messages.append(msg)
            ret.status = "no_match"
            if return_tests_suite is True:
                ret.result = {"test_results": [], "suite": {}}
            return ret

        # download job data
        job_data = self.load_job_data(job_data)

        # generate per-host test suites
        for host_name, host in filtered_nornir.inventory.hosts.items():
            # render suite using Jinja2
            try:
                rendered_suite = self.jinja2_render_templates(
                    templates=[suite],
                    context={
                        "host": host,
                        "norfab": self.client,
                        "job_data": job_data,
                        "netbox": self.add_jinja2_netbox(),
                    },
                    filters=self.add_jinja2_filters(),
                )
            except Exception as e:
                msg = f"{self.name} - '{suite}' Jinja2 rendering failed: '{e}'"
                raise RuntimeError(msg)
            # load suit using YAML
            try:
                tests[host_name] = yaml.safe_load(rendered_suite) or []
            except Exception as e:
                msg = f"{self.name} - '{suite}' YAML load failed: '{e}'"
                raise RuntimeError(msg)

        # validate tests suite
        try:
            _ = modelTestsProcessorSuite(tests=tests)
        except Exception as e:
            msg = f"{self.name} - '{suite}' suite validation failed: '{e}'"
            raise RuntimeError(msg)

        # download pattern, schema and custom function files
        for host_name in tests.keys():
            for index, item in enumerate(tests[host_name]):
                for k in ["pattern", "schema", "function_file"]:
                    if self.is_url(item.get(k)):
                        item[k] = self.fetch_file(
                            item[k], raise_on_fail=True, read=True
                        )
                        if k == "function_file":
                            item["function_text"] = item.pop(k)
                tests[host_name][index] = item

        # save per-host tests suite content before mutating it
        if return_tests_suite is True:
            return_suite = copy.deepcopy(tests)

        log.debug(f"{self.name} - running test '{suite}', is dry run - '{dry_run}'")
        # run dry run task
        if dry_run is True:
            result = filtered_nornir.run(
                task=nr_test, name="tests_dry_run", ret_data_per_host=tests
            )
            ret.result = ResultSerializer(
                result, to_dict=to_dict, add_details=add_details
            )
        # combine per-host tests in suites based on task and arguments
        # Why - to run tests using any nornir service tasks with various arguments
        else:
            for host_name, host_tests in tests.items():
                for test in host_tests:
                    dhash = hashlib.md5()
                    test_args = test.pop("norfab", {})
                    nrtask = test_args.get("nrtask", "cli")
                    assert nrtask in [
                        "cli",
                        "network",
                        "cfg",
                        "task",
                    ], f"{self.name} - unsupported NorFab Nornir Service task '{nrtask}'"
                    test_json = json.dumps(test_args, sort_keys=True).encode()
                    dhash.update(test_json)
                    test_hash = dhash.hexdigest()
                    suites.setdefault(test_hash, {"params": test_args, "tests": {}})
                    suites[test_hash]["tests"].setdefault(host_name, [])
                    suites[test_hash]["tests"][host_name].append(test)
            log.debug(
                f"{self.name} - combined per-host tests suites based on NorFab Nornir Service task and arguments:\n{suites}"
            )
            # run test suites collecting output from devices
            for tests_suite in suites.values():
                nrtask = tests_suite["params"].pop("nrtask", "cli")
                function_kwargs = {
                    **tests_suite["params"],
                    **kwargs,
                    **filters,
                    "tests": tests_suite["tests"],
                    "remove_tasks": remove_tasks,
                    "failed_only": failed_only,
                    "subset": subset,
                }
                result = getattr(self, nrtask)(
                    job=job, **function_kwargs
                )  # returns Result object
                # save test results into overall results
                if to_dict == True:
                    for host_name, host_res in result.result.items():
                        ret.result.setdefault(host_name, {})
                        ret.result[host_name].update(host_res)
                        # set return result failed to true if any of the tests failed
                        for test_res in host_res.values():
                            if add_details:
                                if test_res["result"] != "PASS":
                                    ret.failed = True
                            elif test_res != "PASS":
                                ret.failed = True
                else:
                    ret.result.extend(result.result)
                    # set return result failed to true if any of the tests failed
                    if any(r["result"] != "PASS" for r in result.result):
                        ret.failed = True

        # check if need to return tests suite content
        if return_tests_suite is True:
            ret.result = {"test_results": ret.result, "suite": return_suite}

        return ret

    def netconf(self) -> dict:
        raise NotImplementedError("NETCONF task is not implemented yet")

    def gnmi(self) -> dict:
        raise NotImplementedError("GNMI task is not implemented yet")

    def snmp(self) -> dict:
        raise NotImplementedError("SNMP task is not implemented yet")

    @Task(fastapi={"methods": ["POST"]})
    def network(self, job: Job, fun: str, **kwargs) -> Result:
        """
        Task to call various network-related utility functions.

        Args:
            job: NorFab Job object containing relevant metadata
            fun (str): The name of the utility function to call.
            kwargs (dict): Arguments to pass to the utility function.

        Available utility functions:

        - **resolve_dns** Resolves hosts' hostname DNS, returning IP addresses using
            `nornir_salt.plugins.tasks.network.resolve_dns` Nornir-Salt function.
        - **ping** Executes ICMP ping to host using `nornir_salt.plugins.tasks.network.ping`
            Nornir-Salt function.

        Returns:
            dict: A dictionary containing the results of the network utility function.

        Raises:
            UnsupportedPluginError: If the specified utility function is not supported.
        """
        kwargs["call"] = fun
        return self.task(
            job=job,
            plugin="nornir_salt.plugins.tasks.network",
            **kwargs,
        )

    @Task(fastapi={"methods": ["POST"]})
    def parse(
        self,
        job: Job,
        plugin: str = "napalm",
        getters: Union[str, list] = "get_facts",
        template: str = None,
        commands: Union[str, list] = None,
        to_dict: bool = True,
        add_details: bool = False,
        **kwargs,
    ) -> Result:
        """
        Parse network device output using specified plugin and options.

        Args:
            job: NorFab Job object containing relevant metadata
            plugin (str): The plugin to use for parsing. Options are:

                - napalm - parse devices output using NAPALM getters
                - ttp - use TTP Templates to parse devices output
                - textfsm - use TextFSM templates to parse devices output

            getters (str): The getters to use with the "napalm" plugin.
            template (str): The template to use with the "ttp" or "textfsm" plugin.
            commands (list): The list of commands to run with the "ttp" or "textfsm" plugin.
            to_dict (bool): Whether to convert the result to a dictionary.
            add_details (bool): Whether to add details to the result.
            **kwargs: Additional keyword arguments to pass to the plugin.

        Returns:
            Result: A Result object containing the parsed data.

        Raises:
            UnsupportedPluginError: If the specified plugin is not supported.
        """
        filters = {k: kwargs.pop(k) for k in list(kwargs.keys()) if k in FFun_functions}
        ret = Result(task=f"{self.name}:parse", result={} if to_dict else [])

        self.nr.data.reset_failed_hosts()  # reset failed hosts
        filtered_nornir = FFun(self.nr, **filters)  # filter hosts

        # check if no hosts matched
        if not filtered_nornir.inventory.hosts:
            msg = (
                f"{self.name} - nothing to do, no hosts matched by filters '{filters}'"
            )
            log.debug(msg)
            ret.messages.append(msg)
            ret.status = "no_match"
            return ret

        if plugin == "napalm":
            nr = self._add_processors(filtered_nornir, kwargs, job)  # add processors
            result = nr.run(task=napalm_get, getters=getters, **kwargs)
            ret.result = ResultSerializer(
                result, to_dict=to_dict, add_details=add_details
            )
            ret.failed = result.failed  # failed is true if any of the hosts failed
        elif plugin == "ttp":
            result = self.cli(
                job=job,
                commands=commands or [],
                run_ttp=template,
                **filters,
                **kwargs,
                to_dict=to_dict,
                add_details=add_details,
                plugin="netmiko",
            )
            ret.result = result.result
        elif plugin == "textfsm":
            result = self.cli(
                job=job,
                commands=commands,
                **filters,
                **kwargs,
                to_dict=to_dict,
                add_details=add_details,
                use_textfsm=True,
                textfsm_template=template,
                plugin="netmiko",
            )
            ret.result = result.result
        else:
            raise UnsupportedPluginError(f"Plugin '{plugin}' not supported")

        return ret

    @Task(fastapi={"methods": ["POST"]})
    def file_copy(
        self,
        job: Job,
        source_file: str,
        plugin: str = "netmiko",
        to_dict: bool = True,
        add_details: bool = False,
        dry_run: bool = False,
        **kwargs,
    ) -> Result:
        """
        Task to transfer files to and from hosts using SCP.

        Args:
            job: NorFab Job object containing relevant metadata
            source_file (str): The path or URL of the source file to be copied in
                ``nf://path/to/file`` format
            plugin (str, optional): The plugin to use for file transfer. Supported plugins:

                - netmiko - uses `netmiko_file_transfer` task plugin.

            to_dict (bool, optional): Whether to return the result as a dictionary. Defaults to True.
            add_details (bool, optional): Whether to add detailed information to the result. Defaults to False.
            dry_run (bool, optional): If True, performs a dry run without making any changes. Defaults to False.
            **kwargs: Additional arguments to pass to the file transfer plugin.

        Returns:
            dict: The result of the file copy operation.

        Raises:
            UnsupportedPluginError: If the specified plugin is not supported.
        """
        filters = {k: kwargs.pop(k) for k in list(kwargs.keys()) if k in FFun_functions}
        timeout = job.timeout * 0.9
        ret = Result(task=f"{self.name}:file_copy", result={} if to_dict else [])

        # download file from broker
        if self.is_url(source_file):
            source_file_local = self.fetch_file(
                source_file, raise_on_fail=True, read=False
            )

        # decide on what send commands task plugin to use
        if plugin == "netmiko":
            task_plugin = netmiko_file_transfer
            kwargs["source_file"] = source_file_local
            kwargs.setdefault("socket_timeout", timeout / 5)
            kwargs.setdefault("dest_file", os.path.split(source_file_local)[-1])
        else:
            raise UnsupportedPluginError(f"Plugin '{plugin}' not supported")

        self.nr.data.reset_failed_hosts()  # reset failed hosts
        filtered_nornir = FFun(self.nr, **filters)  # filter hosts

        # check if no hosts matched
        if not filtered_nornir.inventory.hosts:
            msg = (
                f"{self.name} - nothing to do, no hosts matched by filters '{filters}'"
            )
            log.debug(msg)
            ret.messages.append(msg)
            ret.status = "no_match"
            return ret

        nr = self._add_processors(filtered_nornir, kwargs, job)  # add processors

        # run task
        log.debug(
            f"{self.name} - running file copy with arguments '{kwargs}', is dry run - '{dry_run}'"
        )
        if dry_run is True:
            result = nr.run(task=nr_test, name="file_copy_dry_run", **kwargs)
        else:
            with self.connections_lock:
                result = nr.run(task=task_plugin, **kwargs)

        ret.failed = result.failed  # failed is true if any of the hosts failed
        ret.result = ResultSerializer(result, to_dict=to_dict, add_details=add_details)

        self.watchdog.connections_update(nr, plugin)
        self.watchdog.connections_clean()

        return ret

    @Task(fastapi={"methods": ["POST"]})
    def runtime_inventory(self, job: Job, action: str, **kwargs) -> Result:
        """
        Task to work with Nornir runtime (in-memory) inventory.

        Supported actions:

        - `create_host` or `create` - creates new host or replaces existing host object
        - `read_host` or `read` - read host inventory content
        - `update_host` or `update` - non recursively update host attributes if host exists
            in Nornir inventory, do not create host if it does not exist
        - `delete_host` or `delete` - deletes host object from Nornir Inventory
        - `load` - to simplify calling multiple functions
        - `read_inventory` - read inventory content for groups, default and hosts
        - `read_host_data` - to return host's data under provided path keys
        - `list_hosts` - return a list of inventory's host names
        - `list_hosts_platforms` - return a dictionary of hosts' platforms
        - `update_defaults` - non recursively update defaults attributes

        Args:
            job: NorFab Job object containing relevant metadata
            action: action to perform on inventory
            kwargs: argument to use with the calling action
        """
        # clean up kwargs
        _ = kwargs.pop("progress", None)
        job.event(f"Performing '{action}' action")
        return Result(result=InventoryFun(self.nr, call=action, **kwargs))
