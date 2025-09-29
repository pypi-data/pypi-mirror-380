from __future__ import annotations
import typing
from ._base_element import BaseElement
from instaui.event.event_mixin import EventMixin
from typing_extensions import TypedDict, Unpack
from ._utils import handle_props, handle_event_from_props, try_setup_vmodel

if typing.TYPE_CHECKING:
    from instaui.vars.types import TMaybeRef


class Rate(BaseElement):
    def __init__(
        self,
        value: typing.Optional[TMaybeRef[float]] = None,
        *,
        count: typing.Optional[TMaybeRef[float]] = None,
        default_value: typing.Optional[TMaybeRef[float]] = None,
        model_value: typing.Optional[TMaybeRef[float]] = None,
        **kwargs: Unpack[TRateProps],
    ):
        super().__init__("t-rate")

        self.props({"count": count, "default-value": default_value})
        try_setup_vmodel(self, value)
        self.props(handle_props(kwargs, model_value=model_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_change(
        self,
        handler: EventMixin,
        *,
        extends: typing.Optional[typing.List] = None,
    ):
        self.on(
            "change",
            handler,
            extends=extends,
        )
        return self


class TRateProps(TypedDict, total=False):
    allow_half: TMaybeRef[bool]
    clearable: TMaybeRef[bool]
    color: TMaybeRef[typing.Literal["Array"]]
    disabled: TMaybeRef[bool]
    gap: TMaybeRef[float]
    icon: TMaybeRef[str]
    show_text: TMaybeRef[bool]
    size: TMaybeRef[str]
    texts: TMaybeRef[typing.List]
    on_change: EventMixin
