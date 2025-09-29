from dataclasses import dataclass

import strawberry
from pydantic import Field

from apppy.db.migrations import Migrations
from apppy.env import EnvSettings
from apppy.fastql import FastQL
from apppy.fastql.annotation import fastql_query, fastql_query_field, fastql_type_output
from apppy.logger import WithLogger


class VersionSettings(EnvSettings):
    commit: str = Field(alias="APP_VERSION_COMMIT", default="local")
    release: str = Field(alias="APP_VERSION_RELEASE", default="local")


@dataclass
@fastql_type_output
class VersionApiOutput:
    commit: str
    migration: str | None
    release: str


@fastql_query()
class VersionQuery(WithLogger):
    def __init__(self, settings: VersionSettings, fastql: FastQL, migrations: Migrations) -> None:
        self._settings = settings
        self._migrations = migrations
        fastql.include_in_schema(self)

    @fastql_query_field(
        skip_permission_checks=True,
    )
    async def version(self, info: strawberry.Info) -> VersionApiOutput:
        version_output = VersionApiOutput(
            commit=self._settings.commit,
            migration=(await self._migrations.head()),
            release=self._settings.release,
        )

        return version_output
