import collections.abc as c
import customtkinter as ctk


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
        command: c.Callable[[T], None] | None = None,
        state: str = "normal",
        #
        options: dict[str, T] = {},
        default_option: str | None = None,
    ):
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
            values=list(options.keys()),
            variable=variable,
            dynamic_resizing=dynamic_resizing,
            command=lambda text: command(self._options_map[text]) if command else None,
            state=state,
        )

        self._options_map = options

        if default_option:
            self.set(default_option)
