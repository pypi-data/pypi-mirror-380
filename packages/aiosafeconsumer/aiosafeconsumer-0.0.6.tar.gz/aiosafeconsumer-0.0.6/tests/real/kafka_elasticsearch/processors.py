from dataclasses import dataclass
from typing import Any, cast

from aiosafeconsumer.datasync import EnumerateIDsRecord, EventType, ObjectID, Version
from aiosafeconsumer.datasync.elasticsearch import (
    Document,
    ElasticsearchWriter,
    ElasticsearchWriterSettings,
)

from ..types import User, UserDeleteRecord, UserEnumerateRecord, UserRecord


@dataclass
class UsersElasticsearchWriterSettings(ElasticsearchWriterSettings):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(
            version_getter=self._version_getter,
            event_type_getter=self._event_type_getter,
            id_getter=self._id_getter,
            enum_getter=self._enum_getter,
            record_serializer=self._record_serializer,
            **kwargs,
        )

    @staticmethod
    def _version_getter(item: User) -> Version:
        return item.ev_time

    @staticmethod
    def _event_type_getter(item: User) -> EventType:
        return item.ev_type

    @staticmethod
    def _id_getter(item: User) -> ObjectID:
        assert isinstance(item, UserRecord) or isinstance(item, UserDeleteRecord)
        return item.id

    @staticmethod
    def _enum_getter(item: User) -> EnumerateIDsRecord:
        assert isinstance(item, UserEnumerateRecord)
        return EnumerateIDsRecord(ids=cast(list[ObjectID], item.ids))

    @staticmethod
    def _record_serializer(item: UserRecord) -> Document:
        return item._asdict()


class UsersElasticsearchWriter(ElasticsearchWriter[User]):
    settings: ElasticsearchWriterSettings
