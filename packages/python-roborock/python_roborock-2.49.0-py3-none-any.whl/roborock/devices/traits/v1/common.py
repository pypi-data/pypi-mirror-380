"""Module for Roborock V1 devices common trait commands.

This is an internal library and should not be used directly by consumers.
"""

from abc import ABC
from dataclasses import asdict, dataclass, fields
from typing import ClassVar, Self

from roborock.containers import RoborockBase
from roborock.devices.v1_rpc_channel import V1RpcChannel
from roborock.roborock_typing import RoborockCommand

V1ResponseData = dict | list | int | str


@dataclass
class V1TraitMixin(ABC):
    """Base model that supports v1 traits.

    This class provides functioanlity for parsing responses from V1 devices
    into dataclass instances. It also provides a reference to the V1RpcChannel
    used to communicate with the device to execute commands.

    Each trait subclass must define a class variable `command` that specifies
    the RoborockCommand used to fetch the trait data from the device. The
    `refresh()` method can be called to update the contents of the trait data
    from the device. A trait can also support additional commands for updating
    state associated with the trait.

    The traits typically subclass RoborockBase to provide serialization
    and deserialization functionality, but this is not strictly required.
    """

    command: ClassVar[RoborockCommand]

    @classmethod
    def _parse_type_response(cls, response: V1ResponseData) -> Self:
        """Parse the response from the device into a a RoborockBase.

        Subclasses should override this method to implement custom parsing
        logic as needed.
        """
        if not issubclass(cls, RoborockBase):
            raise NotImplementedError(f"Trait {cls} does not implement RoborockBase")
        # Subclasses can override to implement custom parsing logic
        if isinstance(response, list):
            response = response[0]
        if not isinstance(response, dict):
            raise ValueError(f"Unexpected {cls} response format: {response!r}")
        return cls.from_dict(response)

    def _parse_response(self, response: V1ResponseData) -> Self:
        """Parse the response from the device into a a RoborockBase.

        This is used by subclasses that want to override the class
        behavior with instance-specific data.
        """
        return self._parse_type_response(response)

    def __post_init__(self) -> None:
        """Post-initialization to set up the RPC channel.

        This is called automatically after the dataclass is initialized by the
        device setup code.
        """
        self._rpc_channel = None

    @property
    def rpc_channel(self) -> V1RpcChannel:
        """Helper for executing commands, used internally by the trait"""
        if not self._rpc_channel:
            raise ValueError("Device trait in invalid state")
        return self._rpc_channel

    async def refresh(self) -> Self:
        """Refresh the contents of this trait."""
        response = await self.rpc_channel.send_command(self.command)
        new_data = self._parse_response(response)
        for k, v in asdict(new_data).items():
            if v is not None:
                setattr(self, k, v)
        return self


def _get_value_field(clazz: type[V1TraitMixin]) -> str:
    """Get the name of the field marked as the main value of the RoborockValueBase."""
    value_fields = [field.name for field in fields(clazz) if field.metadata.get("roborock_value", False)]
    if len(value_fields) != 1:
        raise ValueError(
            f"RoborockValueBase subclass {clazz} must have exactly one field marked as roborock_value, "
            f" but found: {value_fields}"
        )
    return value_fields[0]


@dataclass(init=False, kw_only=True)
class RoborockValueBase(V1TraitMixin, RoborockBase):
    """Base class for traits that represent a single value.

    This class is intended to be subclassed by traits that represent a single
    value, such as volume or brightness. The subclass should define a single
    field with the metadata `roborock_value=True` to indicate which field
    represents the main value of the trait.
    """

    @classmethod
    def _parse_response(cls, response: V1ResponseData) -> Self:
        """Parse the response from the device into a RoborockValueBase."""
        if isinstance(response, list):
            response = response[0]
        if not isinstance(response, int):
            raise ValueError(f"Unexpected response format: {response!r}")
        value_field = _get_value_field(cls)
        return cls(**{value_field: response})
