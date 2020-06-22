from __future__ import annotations
from typing import Union
from typing import Optional
from json import dumps, loads
from json.decoder import JSONDecodeError
from functools import wraps

from .ui import UI


class Button(UI):
    """
    Keyboards button. Aviable for Keyboard and Templates
    """
    def __new__(cls, **info):
        self = object.__new__(cls)
        self.__init__(info)
        return self

    def __init__(self, info) -> None:
        self.info = dict(
            action=info
        )
        self.info = {"action": {**info}}

    def _payload_convert(func):
        """
        Convert payload in button
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            action = func(*args, **kwargs)
            action.update(type=func.__name__)
            if action["payload"]is None:
                del action["payload"]
            else:
                # Dumps to JSON
                if isinstance(action["payload"], dict):
                    action["payload"] = dumps(
                        action["payload"], ensure_ascii=False
                    )
                # Check payload type
                elif not isinstance(action["payload"], str):
                    raise TypeError(
                        "Payload should be "
                        "dumped dict to string "
                        "or dict, not "
                        f"{type(action['payload'])}"
                    )
                # Check payload validations
                try:
                    loads(action["payload"])
                except JSONDecodeError as err:
                    raise ValueError(
                        "Invalid payload struct, "
                        "should be JSON format, "
                        "but get JSONDecodeError: "
                        f"{err}"
                    )
            obj = Button.__new__(Button, **action)
            return obj

        return wrapper

    def _is_text_button(func):
        @wraps(func)
        def wrapper(self):
            if self.info["action"]["type"] == "text":
                self.info["color"] = func.__name__
                return self
            else:
                raise TypeError(
                    "Colors unsupposed "
                    "for button type "
                    f'{self.info["action"]["type"]}'
                )
        return wrapper

    @_is_text_button
    def positive(self) -> Button:
        """
        Green button
        """

    @_is_text_button
    def negative(self) -> Button:
        """
        Red button
        """

    @_is_text_button
    def secondary(self) -> Button:
        """
        White button
        """

    @_is_text_button
    def primary(self) -> Button:
        """
        Blue button
        """

    @classmethod
    def line(cls) -> Button:
        """
        Add Buttons line
        """
        self = object.__new__(cls)
        self.info = None

        return self

    @staticmethod
    @_payload_convert
    def text(
        label: str, *,
        payload: Optional[Union[str, dict]] = None
    ) -> Button:
        return locals()

    @staticmethod
    @_payload_convert
    def open_link(
        label: str, *,
        link: str,
        payload: Optional[Union[str, dict]] = None
    ) -> Button:
        return locals()

    @staticmethod
    @_payload_convert
    def location(*,
        payload: Optional[Union[str, dict]] = None
    ) -> Button:
        return locals()

    @staticmethod
    @_payload_convert
    def vkpay(*,
        hash_: str,
        payload: Optional[Union[str, dict]] = None
    ) -> Button:
        data = locals()
        hash_ = data.pop("hash_")
        data.update(hash=hash_)
        return data

    @staticmethod
    @_payload_convert
    def open_app(
        label: str, *,
        app_id: int,
        owner_id: int,
        hash_: str,
        payload: Optional[Union[str, dict]] = None
    ) -> Button:
        data = locals()
        hash_ = data.pop("hash_")
        data.update(hash=hash_)
        return data
