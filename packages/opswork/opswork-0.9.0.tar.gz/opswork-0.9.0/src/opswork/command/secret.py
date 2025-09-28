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

import click

from opswork.module.logger import Logger
from opswork.module.output import Output
from opswork.module.config import Config
from opswork.module.encrypt import Encrypt
from opswork.module.database import Database
from opswork.module.file_system import FileSystem


class Secrets:
    """Secrets Class"""

    def __init__(self):
        self.output = Output()
        self.database = Database()
        self.config = Config()
        self.encrypt = Encrypt()
        self.file_system = FileSystem()
        self.logger = Logger().get_logger(__name__)

    def init(self):
        """Init database and configs"""
        self.configs = self.config.load()
        self.database.connect(self.configs["database"]["path"])
        self.database.migrate()
        return self

    def add(self, secret, force):
        """Add a new secret"""
        if force:
            self.database.delete_secret(secret.name)

        if self.database.get_secret(secret.name) is not None:
            raise click.ClickException(f"Secret with name {secret.name} exists")

        secret.value = self.encrypt.encrypt(
            self.configs["database"]["token"], secret.value
        )

        self.database.insert_secret(secret)

        click.echo(f"Secret with name {secret.name} got created")

    def list(self, tag, output):
        """List secrets"""
        data = []
        secrets = self.database.list_secrets()

        for secret in secrets:
            if tag != "" and tag not in secret.tags:
                continue

            data.append(
                {
                    "ID": secret.id,
                    "Name": secret.name,
                    "Value": self.encrypt.decrypt(
                        self.configs["database"]["token"], secret.value
                    ),
                    "Tags": ", ".join(secret.tags) if len(secret.tags) > 0 else "-",
                    "Created at": secret.created_at,
                    "Updated at": secret.updated_at,
                }
            )

        if len(data) == 0:
            raise click.ClickException(f"No secrets found!")

        print(
            self.output.render(
                data, Output.JSON if output.lower() == "json" else Output.DEFAULT
            )
        )

    def get(self, name, output):
        """Get a secret"""
        secret = self.database.get_secret(name)

        if secret is None:
            raise click.ClickException(f"Secret with name {name} not found")

        data = [
            {
                "ID": secret.id,
                "Name": secret.name,
                "Value": self.encrypt.decrypt(
                    self.configs["database"]["token"], secret.value
                ),
                "Tags": ", ".join(secret.tags) if len(secret.tags) > 0 else "-",
                "Created at": secret.created_at,
                "Updated at": secret.updated_at,
            }
        ]

        print(
            self.output.render(
                data, Output.JSON if output.lower() == "json" else Output.DEFAULT
            )
        )

    def delete(self, name):
        """Delete a secret"""
        self.database.delete_secret(name)

        click.echo(f"Secret with name {name} got deleted")
