from collections.abc import Callable
import customtkinter as ctk
from utils.I18n import I18n


class SelectButtons[T](ctk.CTkSegmentedButton):
    """
    SegmentedButton에서 values속성의 기능을 없애고, options속성을 추가한 컴포넌트.

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
        border_width: int = 3,
        bg_color: str | tuple[str, str] = "transparent",
        fg_color: str | tuple[str, str] | None = None,
        selected_color: str | tuple[str, str] | None = None,
        selected_hover_color: str | tuple[str, str] | None = None,
        unselected_color: str | tuple[str, str] | None = None,
        unselected_hover_color: str | tuple[str, str] | None = None,
        text_color: str | tuple[str, str] | None = None,
        text_color_disabled: str | tuple[str, str] | None = None,
        background_corner_colors: tuple[str | tuple[str, str]] | None = None,
        font: tuple | ctk.CTkFont | None = None,
        values: list | None = None,
        variable: ctk.Variable | None = None,
        dynamic_resizing: bool = True,
        command: Callable[[T], None] | None = None,
        state: str = "normal",
        #
        options: dict[str, T] = {},
        default_option_key: str | None = None,
    ):
        values_from_options = list(map(I18n.get_text, list(options.keys())))
        super().__init__(
            master=master,
            width=width,
            height=height,
            corner_radius=corner_radius,
            border_width=border_width,
            bg_color=bg_color,
            fg_color=fg_color,
            selected_color=selected_color,
            selected_hover_color=selected_hover_color,
            unselected_color=unselected_color,
            unselected_hover_color=unselected_hover_color,
            text_color=text_color,
            text_color_disabled=text_color_disabled,
            background_corner_colors=background_corner_colors,
            font=font,
            values=values_from_options,
            variable=variable,
            dynamic_resizing=dynamic_resizing,
            command=lambda text: command(self._options_map[text]) if command else None,
            state=state,
        )

        self._raw_options_map = options

        if options is not None:
            self._options_unsubscriber = I18n.subscribe(
                key="lang_changed",
                callback=lambda _: self._on_language_change(),
            )
            self._options_map = {
                I18n.get_text(text): value
                for text, value in self._raw_options_map.items()
            }
        else:
            self._options_unsubscriber = None
            self._options_map = {}

        if default_option_key is not None:
            self.set(I18n.get_text(default_option_key))

    def _on_language_change(self):
        key = self.get_key()
        self.configure(
            values=list(map(I18n.get_text, list(self._raw_options_map.keys())))
        )
        self._options_map = {
            I18n.get_text(text): value for text, value in self._raw_options_map.items()
        }
        self.set_by_key(key)

    def destory(self) -> None:
        if self._options_unsubscriber is not None:
            self._options_unsubscriber()
        super().destroy()
