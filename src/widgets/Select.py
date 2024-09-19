from collections.abc import Callable
import customtkinter as ctk
import tkinter
from utils.I18n import I18n


class Select[T](ctk.CTkOptionMenu):
    """
    CTkOptionMenu에서 values속성의 기능을 없애고, options속성을 추가한 컴포넌트.

    :param options: { "밝은": "light", "어두운": "dark" }와 같이 텍스트와 값의 매핑을 설정한다.,
    """

    def get(self) -> T:
        """현재 선택된 옵션의 값을 반환, 옵션의 글자가 아닌 그에 해당하는 값을 반환한다."""
        text = super().get()
        value = self._options_map[text]
        return value

    def get_key(self) -> str:
        """현재 선택된 옵션의 키를 반환한다."""
        value = self.get()
        for k, v in self._raw_options_map.items():
            if v == value:
                return k
        raise ValueError(f"Value {value} not found in options")

    def set_by_key(self, key: str):
        """옵션의 키를 통해 값을 설정한다."""
        value = I18n.get_text(key)
        return super().set(value)

    def __init__(
        self,
        master,
        width: int = 140,
        height: int = 28,
        corner_radius: int | None = None,
        bg_color: str | tuple[str, str] = "transparent",
        fg_color: str | tuple[str, str] | None = None,
        button_color: str | tuple[str, str] | None = None,
        button_hover_color: str | tuple[str, str] | None = None,
        text_color: str | tuple[str, str] | None = None,
        text_color_disabled: str | tuple[str, str] | None = None,
        dropdown_fg_color: str | tuple[str, str] | None = None,
        dropdown_hover_color: str | tuple[str, str] | None = None,
        dropdown_text_color: str | tuple[str, str] | None = None,
        font: tuple | ctk.CTkFont | None = None,
        dropdown_font: tuple | ctk.CTkFont | None = None,
        values: list[str] = [],
        variable: tkinter.Variable | None = None,
        state: str = tkinter.NORMAL,
        hover: bool = True,
        command: Callable[[T], None] | None = None,
        dynamic_resizing: bool = True,
        anchor: str = "w",
        #
        options: dict[str, T] = {},
        default_option_key: str | None = None,
        **kwargs,
    ):
        values_from_options = list(map(I18n.get_text, list(options.keys())))
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
            **kwargs,
        )

        self._raw_options_map = options

        if options is not None:
            self._options_unsubscriber = I18n.subscribe(
                key="lang_changed",
                callback=lambda _: self._on_language_change(),
            )
            self._options_map = {
                I18n.get_text(k): v for k, v in self._raw_options_map.items()
            }
        else:
            self._options_unsubscriber = None
            self._options_map = {}

        if default_option_key is not None:
            self.set(I18n.get_text(default_option_key))

    def _on_language_change(self):
        key = self.get_key()
        self.configure(values=list(map(I18n.get_text, list(self._options_map.keys()))))
        self._options_map = {
            I18n.get_text(k): v for k, v in self._raw_options_map.items()
        }
        self.set_by_key(key)

    def destroy(self) -> None:
        if self._options_unsubscriber is not None:
            self._options_unsubscriber()
        super().destroy()
