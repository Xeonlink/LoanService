from typing import Any, Callable, Tuple, Generic, TypeVar
import tkinter
import customtkinter as ctk
from utils import LangManager

T = TypeVar("T")


class Select(ctk.CTkOptionMenu, Generic[T]):
    """
    CTkOptionMenu에서 values속성의 기능을 없애고, options속성을 추가한 컴포넌트.

    :param options: { "밝은": "light", "어두운": "dark" }와 같이 텍스트와 값의 매핑을 설정한다.,
    """

    def get(self) -> T:
        """현재 선택된 옵션의 값을 반환, 옵션의 글자가 아닌 그에 해당하는 값을 반환한다."""
        text = super().get()
        value = self._options_map[text]
        return value

    def __init__(
        self,
        master: Any,
        width: int = 140,
        height: int = 28,
        corner_radius: int | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        button_color: str | Tuple[str, str] | None = None,
        button_hover_color: str | Tuple[str, str] | None = None,
        text_color: str | Tuple[str, str] | None = None,
        text_color_disabled: str | Tuple[str, str] | None = None,
        dropdown_fg_color: str | Tuple[str, str] | None = None,
        dropdown_hover_color: str | Tuple[str, str] | None = None,
        dropdown_text_color: str | Tuple[str, str] | None = None,
        font: Tuple | ctk.CTkFont | None = None,
        dropdown_font: Tuple | ctk.CTkFont | None = None,
        values: list[str] = [],
        variable: tkinter.Variable | None = None,
        state: str = tkinter.NORMAL,
        hover: bool = True,
        command: Callable[[T], Any] | None = None,
        dynamic_resizing: bool = True,
        anchor: str = "w",
        #
        options: dict[str, T] = {},
        **kwargs
    ):
        values_from_options = list(map(LangManager.get_text, list(options.keys())))
        super().__init__(
            master,
            width=width,
            height=height,
            corner_radius=corner_radius,
            bg_color=bg_color,
            fg_color=fg_color,
            button_color=button_color,
            button_hover_color=button_hover_color,
            text_color=text_color,
            text_color_disabled=text_color_disabled,
            dropdown_fg_color=dropdown_fg_color,
            dropdown_hover_color=dropdown_hover_color,
            dropdown_text_color=dropdown_text_color,
            font=font,
            dropdown_font=dropdown_font,
            values=values_from_options,
            variable=variable,
            state=state,
            hover=hover,
            command=lambda text: command(self._options_map[text]) if command else None,
            dynamic_resizing=dynamic_resizing,
            anchor=anchor,
            **kwargs
        )

        self._raw_options_map = options

        if options is not None:
            self._options_unsubscriber = LangManager.subscribe(
                key="lang_changed",
                callback=lambda _: self._on_language_change(),
            )
            self._options_map = {
                LangManager.get_text(k): v for k, v in self._raw_options_map.items()
            }

    def _on_language_change(self):
        self.configure(
            values=list(map(LangManager.get_text, list(self._options_map.keys())))
        )
        self._options_map = {
            LangManager.get_text(k): v for k, v in self._raw_options_map.items()
        }
