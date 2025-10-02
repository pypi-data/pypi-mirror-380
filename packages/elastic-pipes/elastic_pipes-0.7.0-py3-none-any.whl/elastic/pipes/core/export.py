# Copyright 2025 Elasticsearch B.V.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Elastic Pipes component to export data from the Pipes state."""

import sys
from logging import Logger
from pathlib import Path

from typing_extensions import Annotated, Any

from . import Pipe
from .util import serialize


class Ctx(Pipe.Context):
    file_name: Annotated[
        str,
        Pipe.Config("file"),
        Pipe.Help("file destination of the data"),
        Pipe.Notes("default: standard output"),
    ] = None
    format: Annotated[
        str,
        Pipe.Config("format"),
        Pipe.Help("data format of the file content (ex. yaml, json, ndjson)"),
        Pipe.Notes("default: guessed from the file name extension"),
    ] = None
    state: Annotated[
        Any,
        Pipe.State(None, indirect="node", mutable=True),
        Pipe.Help("state node containing the source data"),
        Pipe.Notes("default: whole state"),
    ]


@Pipe("elastic.pipes.core.export")
def main(ctx: Ctx, log: Logger, dry_run: bool):
    """Export data to file or standard output."""

    format = ctx.format
    if format is None:
        if ctx.file_name:
            format = Path(ctx.file_name).suffix.lower()[1:]
            log.debug(f"export file format guessed from file extension: {format}")
        else:
            format = "yaml"
            log.debug(f"assuming export file format: {format}")

    if dry_run:
        return

    node = ctx.get_binding("state").node
    msg_state = "everything" if node is None else f"'{node}'"
    msg_file_name = f"'{ctx.file_name}'" if ctx.file_name else "standard output"
    log.info(f"exporting {msg_state} to {msg_file_name}...")

    if ctx.file_name:
        with Path(ctx.file_name).expanduser().open("w") as f:
            serialize(f, ctx.state, format=format)
    else:
        serialize(sys.stdout, ctx.state, format=format)


if __name__ == "__main__":
    main()
