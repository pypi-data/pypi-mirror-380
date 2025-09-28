import inspect
from dataclasses import dataclass
from enum import Enum, auto

from ._type import Type, typeof

__all__ = [
    "Unspecified",
    "ParameterKind",
    "Parameter",
    "Signature",
    "ComplicatedSignatureError",
    "signatureof",
]


class Unspecified: ...


class ParameterKind(Enum):
    positional = auto()
    keyword = auto()


@dataclass(frozen=True)
class Parameter(object):
    typ: Type
    name: str
    default_value: object
    kind: ParameterKind


@dataclass(frozen=True)
class Signature(object):
    parameters: list[Parameter]
    returns: Type | None


class ComplicatedSignatureError(Exception):
    argument_name: str

    def __init__(self, argument_name: str) -> None:
        super().__init__(f"Argument `{argument_name}` is too complicated to get signature of")
        self.argument_name = argument_name


def signatureof(obj: object) -> Signature:
    returns: Type | None = None

    if isinstance(obj, type):
        returns = typeof(obj)
        obj = obj.__init__
    if not callable(obj):
        raise TypeError(f"Expected a callable, got `{type(obj)}`")

    function_signature = inspect.signature(obj)

    # Parse parameters
    parameters: list[Parameter] = []
    for parameter in function_signature.parameters.values():
        if parameter.kind == inspect.Parameter.VAR_POSITIONAL or parameter.kind == inspect.Parameter.VAR_KEYWORD:
            raise ComplicatedSignatureError(parameter.name)
        if parameter.name == "self":
            continue

        parameter_type = typeof(parameter.annotation)
        default_value: object | Unspecified = Unspecified
        kind: ParameterKind = ParameterKind.keyword
        if parameter.default is not inspect.Parameter.empty:
            default_value = parameter.default
        if parameter.kind == inspect.Parameter.POSITIONAL_ONLY:
            kind = ParameterKind.positional
        parameters.append(Parameter(parameter_type, parameter.name, default_value, kind))

    if (
        returns is None
        and function_signature.return_annotation is not inspect.Parameter.empty
        and function_signature.return_annotation is not None
    ):
        returns = typeof(function_signature.return_annotation)
    return Signature(parameters, returns)
