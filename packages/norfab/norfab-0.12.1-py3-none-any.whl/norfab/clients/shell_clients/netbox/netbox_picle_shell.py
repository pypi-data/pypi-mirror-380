"""
PICLE Shell CLient
==================

Client that implements interactive shell to work with NorFab.
"""

import logging
import json
import yaml

from rich.console import Console
from picle.models import PipeFunctionsModel, Outputters
from enum import Enum
from pydantic import (
    BaseModel,
    StrictBool,
    StrictInt,
    StrictFloat,
    StrictStr,
    conlist,
    root_validator,
    Field,
)
from typing import Union, Optional, List, Any, Dict, Tuple
from ..common import log_error_or_result
from .netbox_picle_shell_common import NetboxClientRunJobArgs
from .netbox_picle_shell_get_devices import GetDevices
from .netbox_picle_shell_cache import NetboxServiceCache
from .netbox_picle_shell_get_circuits import GetCircuits
from .netbox_picle_shell_update_device import UpdateDeviceCommands
from .netbox_picle_shell_get_connections import GetConnections
from .netbox_picle_shell_get_containerlab_inventory import (
    GetContainerlabInventoryCommand,
)
from .netbox_picle_shell_create_ip import CreateIp
from .netbox_picle_shell_create_ip_bulk import CreateIpBulk
from .netbox_picle_shell_create_prefix import CreatePrefixShell
from norfab.models.netbox import NetboxCommonArgs

RICHCONSOLE = Console()
SERVICE = "netbox"
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------------------------
# NETBOX SERVICE GRAPHQL SHELL MODEL
# ---------------------------------------------------------------------------------------------


class GrapQLCommands(NetboxCommonArgs, NetboxClientRunJobArgs):
    dry_run: Optional[StrictBool] = Field(
        None,
        description="Only return query content, do not run it",
        json_schema_extra={"presence": True},
        alias="dry-run",
    )
    obj: Optional[StrictStr] = Field(
        None,
        description="Object to return data for e.g. device_list, interface, ip_address",
    )
    filters: Optional[StrictStr] = Field(
        None,
        description="Dictionary of key-value pairs to filter by",
    )
    fields: Optional[StrictStr] = Field(
        None,
        description="List of data fields to return",
    )
    queries: Optional[StrictStr] = Field(
        None,
        description="Dictionary keyed by GraphQL aliases with values of obj, filters, fields dictionary",
    )
    query_string: Optional[StrictStr] = Field(
        None,
        description="Complete GraphQL query string to send as is",
        alias="query-string",
    )

    @staticmethod
    def run(*args, **kwargs):
        workers = kwargs.pop("workers", "any")
        timeout = kwargs.pop("timeout", 600)
        verbose_result = kwargs.pop("verbose_result", False)

        ret = NFCLIENT.run_job(
            "netbox",
            "graphql",
            workers=workers,
            args=args,
            kwargs=kwargs,
            timeout=timeout,
        )

        return log_error_or_result(ret, verbose_result=verbose_result)

    class PicleConfig:
        subshell = True
        prompt = "nf[netbox-graphql]#"
        outputter = Outputters.outputter_json


# ---------------------------------------------------------------------------------------------
# NETBOX SERVICE SHELL SHOW COMMANDS MODELS
# ---------------------------------------------------------------------------------------------


class NetboxShowCommandsModel(NetboxCommonArgs, NetboxClientRunJobArgs):
    inventory: Any = Field(
        None,
        description="show Netbox inventory data",
        json_schema_extra={
            "outputter": Outputters.outputter_yaml,
            "function": "get_inventory",
        },
    )
    version: Any = Field(
        None,
        description="show Netbox service version report",
        json_schema_extra={
            "outputter": Outputters.outputter_yaml,
            "absolute_indent": 2,
            "function": "get_version",
        },
    )
    status: Any = Field(
        None,
        description="show Netbox status",
        json_schema_extra={"function": "get_netbox_status"},
    )
    compatibility: Any = Field(
        None,
        description="show Netbox compatibility",
        json_schema_extra={"function": "get_compatibility"},
    )

    class PicleConfig:
        outputter = Outputters.outputter_nested
        pipe = PipeFunctionsModel

    @staticmethod
    def get_inventory(**kwargs):
        workers = kwargs.pop("workers", "all")
        verbose_result = kwargs.pop("verbose_result", False)
        result = NFCLIENT.run_job("netbox", "get_inventory", workers=workers)
        result = log_error_or_result(result, verbose_result=verbose_result)
        return result

    @staticmethod
    def get_version(**kwargs):
        workers = kwargs.pop("workers", "all")
        verbose_result = kwargs.pop("verbose_result", False)
        result = NFCLIENT.run_job("netbox", "get_version", workers=workers)
        result = log_error_or_result(result, verbose_result=verbose_result)
        return result

    @staticmethod
    def get_netbox_status(**kwargs):
        workers = kwargs.pop("workers", "any")
        verbose_result = kwargs.pop("verbose_result", False)
        result = NFCLIENT.run_job(
            "netbox", "get_netbox_status", workers=workers, kwargs=kwargs
        )
        result = log_error_or_result(result, verbose_result=verbose_result)
        return result

    @staticmethod
    def get_compatibility(**kwargs):
        workers = kwargs.pop("workers", "any")
        verbose_result = kwargs.pop("verbose_result", False)
        result = NFCLIENT.run_job(
            "netbox", "get_compatibility", workers=workers, kwargs=kwargs
        )
        result = log_error_or_result(result, verbose_result=verbose_result)
        return result


# ---------------------------------------------------------------------------------------------
# NETBOX SERVICE GET SHELL MODEL
# ---------------------------------------------------------------------------------------------


class GetInterfaces(NetboxCommonArgs, NetboxClientRunJobArgs):
    devices: Union[StrictStr, List] = Field(
        ..., description="Devices to retrieve interface for"
    )
    ip_addresses: Optional[StrictBool] = Field(
        None,
        description="Retrieves interface IP addresses",
        json_schema_extra={"presence": True},
        alias="ip-addresses",
    )
    inventory_items: Optional[StrictBool] = Field(
        None,
        description="Retrieves interface inventory items",
        json_schema_extra={"presence": True},
        alias="inventory-items",
    )
    dry_run: Optional[StrictBool] = Field(
        None,
        description="Only return query content, do not run it",
        json_schema_extra={"presence": True},
        alias="dry-run",
    )
    interface_regex: StrictStr = Field(
        None,
        description="Regex patter to match interfaces and ports",
        alias="interface-regex",
    )

    @staticmethod
    def run(*args, **kwargs):
        workers = kwargs.pop("workers", "any")
        timeout = kwargs.pop("timeout", 600)
        verbose_result = kwargs.pop("verbose_result", False)
        if isinstance(kwargs["devices"], str):
            kwargs["devices"] = [kwargs["devices"]]
        with RICHCONSOLE.status("[bold green]Running query", spinner="dots") as status:
            result = NFCLIENT.run_job(
                "netbox",
                "get_interfaces",
                workers=workers,
                args=args,
                kwargs=kwargs,
                timeout=timeout,
            )
        result = log_error_or_result(result, verbose_result=verbose_result)
        return result

    class PicleConfig:
        outputter = Outputters.outputter_json


class GetCommands(BaseModel):
    devices: GetDevices = Field(None, description="Query Netbox devices data")
    interfaces: GetInterfaces = Field(
        None, description="Query Netbox device interfaces data"
    )
    circuits: GetCircuits = Field(
        None, description="Query Netbox circuits data for devices"
    )
    connections: GetConnections = Field(
        None, description="Query Netbox connections data for devices"
    )
    containerlab_inventory: GetContainerlabInventoryCommand = Field(
        None,
        description="Query Netbox and construct Containerlab inventory",
        alias="containerlab-inventory",
    )

    class PicleConfig:
        subshell = True
        prompt = "nf[netbox-get]#"


# ---------------------------------------------------------------------------------------------
# NETBOX SERVICE CREATE SHELL MODEL
# ---------------------------------------------------------------------------------------------


class CreateCommands(BaseModel):
    prefix: CreatePrefixShell = Field(
        None,
        description="Allocate next available prefix from parent prefix",
    )
    ip: CreateIp = Field(
        None,
        description="Allocate next available IP address from prefix",
    )
    ip_bulk: CreateIpBulk = Field(
        None,
        description="Allocate next available IP address from prefix for multiple devices and interfaces",
        alias="ip-bulk",
    )

    class PicleConfig:
        subshell = True
        prompt = "nf[netbox-create]#"


# ---------------------------------------------------------------------------------------------
# NETBOX SERVICE UPDATE SHELL MODEL
# ---------------------------------------------------------------------------------------------


class UpdateCommands(BaseModel):
    device: UpdateDeviceCommands = Field(None, description="Update device data")

    class PicleConfig:
        subshell = True
        prompt = "nf[netbox-update]#"


# ---------------------------------------------------------------------------------------------
# NETBOX SERVICE MAIN SHELL MODEL
# ---------------------------------------------------------------------------------------------


class NetboxServiceCommands(BaseModel):
    graphql: GrapQLCommands = Field(None, description="Query Netbox GrapQL API")
    get: GetCommands = Field(None, description="Query data from Netbox")
    update: UpdateCommands = Field(None, description="Update Netbox data")
    cache: NetboxServiceCache = Field(
        None, description="Work with Netbox service cached data"
    )
    create: CreateCommands = Field(None, description="Create objects in Netbox")

    class PicleConfig:
        subshell = True
        prompt = "nf[netbox]#"
