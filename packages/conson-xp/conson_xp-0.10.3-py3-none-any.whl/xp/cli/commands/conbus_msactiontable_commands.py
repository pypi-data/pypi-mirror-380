"""XP24 Action Table CLI commands."""

import json
from dataclasses import asdict

import click

from xp.cli.commands.conbus import conbus_msactiontable
from xp.cli.utils.decorators import (
    connection_command,
    handle_service_errors,
)
from xp.cli.utils.serial_number_type import SERIAL
from xp.cli.utils.xp_module_type import XP_MODULE_TYPE
from xp.services.actiontable.msactiontable_service import (
    MsActionTableError,
    MsActionTableService,
)


@conbus_msactiontable.command("download", short_help="Download MSActionTable")
@click.argument("serial_number", type=SERIAL)
@click.argument("xpmoduletype", type=XP_MODULE_TYPE)
@connection_command()
@handle_service_errors(MsActionTableError)
def conbus_download_msactiontable(serial_number: str, xpmoduletype: str) -> None:
    """Download MS action table from XP24 module"""
    service = MsActionTableService()

    with service:
        action_table = service.download_action_table(serial_number, xpmoduletype)
        output = {
            "serial_number": serial_number,
            "xpmoduletype": xpmoduletype,
            "action_table": asdict(action_table),
        }

        click.echo(json.dumps(output, indent=2, default=str))
