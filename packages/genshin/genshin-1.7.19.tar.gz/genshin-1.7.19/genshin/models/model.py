"""Modified pydantic model."""

from __future__ import annotations

import abc
import datetime
import enum
import logging
import typing
from typing import Annotated

import pydantic

from genshin.constants import CN_TIMEZONE

__all__ = ["APIModel", "Aliased", "Unique"]

logger: logging.Logger = logging.getLogger(__name__)


class APIModel(pydantic.BaseModel):
    """Modified pydantic model."""

    model_config: pydantic.ConfigDict = pydantic.ConfigDict(arbitrary_types_allowed=True)  # type: ignore


class Unique(abc.ABC):
    """A hashable model with an id."""

    id: int

    def __int__(self) -> int:
        return hash(self.id)

    def __hash__(self) -> int:
        return hash(self.id)


def Aliased(
    alias: typing.Optional[str] = None,
    default: typing.Any = ...,
    **kwargs: typing.Any,
) -> typing.Any:
    """Create an aliased field."""
    return pydantic.Field(default, alias=alias, **kwargs)


def add_timezone(value: datetime.datetime) -> datetime.datetime:
    return value.replace(tzinfo=CN_TIMEZONE)


def convert_datetime(value: typing.Optional[typing.Mapping[str, typing.Any]]) -> datetime.datetime:
    if value:
        value = typing.cast(typing.Dict[str, typing.Any], value)
        tzinfo = value.pop("tzinfo", None)
        if tzinfo is not None:
            tz = datetime.timezone(datetime.timedelta(hours=tzinfo))
        else:
            tz = None

        return datetime.datetime(tzinfo=tz, **value)

    msg = f"Invalid datetime value provided: {value!r}"
    raise ValueError(msg)


def parse_timestamp(value: typing.Optional[typing.Union[str, int]]) -> datetime.datetime:
    """Parse a timestamp into a datetime object."""
    if isinstance(value, str):
        value = int(value)
    if isinstance(value, int):
        return datetime.datetime.fromtimestamp(value).replace(tzinfo=datetime.timezone.utc)
    raise ValueError(f"Invalid timestamp value provided: {value!r}")


InputValue = typing.TypeVar("InputValue", str, int, enum.Enum)
EnumType = typing.TypeVar("EnumType", bound=enum.Enum)


def prevent_enum_error(value: InputValue, cls: typing.Type[EnumType]) -> typing.Union[EnumType, InputValue]:
    """Prevent enum error by returning the value as is."""
    try:
        return cls(value)
    except ValueError:
        logger.warning("Unknown %s: %r, please report to developer", cls.__name__, value)
        return value


TZDateTime = Annotated[datetime.datetime, pydantic.AfterValidator(add_timezone)]
DateTime = Annotated[datetime.datetime, pydantic.BeforeValidator(convert_datetime)]
UnixDateTime = Annotated[datetime.datetime, pydantic.BeforeValidator(parse_timestamp)]
LevelField = Annotated[int, pydantic.Field(ge=1)]
