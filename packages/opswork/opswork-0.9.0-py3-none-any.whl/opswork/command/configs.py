# MIT License
#
# Copyright (c) 2023 Clivern
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import yaml
import click

from opswork.module.logger import Logger
from opswork.module.output import Output
from opswork.module.database import Database
from opswork.module.file_system import FileSystem
from opswork.module.encrypt import Encrypt


class Configs:
    """Configs Class"""

    FILE = ".opswork.yml"

    def __init__(self):
        self.database = Database()
        self.file_system = FileSystem()
        self.home = os.getenv("HOME", "")
        self.encrypt = Encrypt()
        self.logger = Logger().get_logger(__name__)

    def init(self):
        """Init Configs"""
        if self.home == "":
            raise click.ClickException("User home path is not defined")

        if self.file_system.file_exists("{}/{}".format(self.home, Configs.FILE)):
            raise click.ClickException("Config file exists!")

        base = {
            "database": {
                "type": "file",
                "path": "{}/opswork.db".format(self.home),
                "token": self.encrypt.get_key(),
            },
            "cache": {"path": "/tmp"},
        }

        self.database.connect("{}/opswork.db".format(self.home))
        self.database.migrate()

        self.file_system.write_file(
            "{}/{}".format(self.home, Configs.FILE), yaml.dump(base)
        )

        click.echo(
            "Config file {} got created!".format(
                click.format_filename("{}/{}".format(self.home, Configs.FILE))
            )
        )

    def edit(self):
        """Edit Configs"""
        if self.home == "":
            raise click.ClickException("User home path is not defined")

        if not self.file_system.file_exists("{}/{}".format(self.home, Configs.FILE)):
            raise click.ClickException("Config file is missing")

        click.edit(filename="{}/{}".format(self.home, Configs.FILE))

        click.echo(
            "Config file {} got updated!".format(
                click.format_filename("{}/{}".format(self.home, Configs.FILE))
            )
        )

    def dump(self):
        """Dump Configs"""
        if self.home == "":
            raise click.ClickException("User home path is not defined")

        if not self.file_system.file_exists("{}/{}".format(self.home, Configs.FILE)):
            raise click.ClickException("Config file is missing")

        print("")
        print(self.file_system.read_file("{}/{}".format(self.home, Configs.FILE)))
