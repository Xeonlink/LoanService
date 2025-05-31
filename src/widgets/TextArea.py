import customtkinter as ctk


class TextArea(ctk.CTkTextbox):
    """
    customtkinter.CTkTextbox에서 default_text속성을 추가한 컴포넌트.

    CTkTextBox에서는 기본 state를 "disabled"로 설정하면 아무리 insert()를 해도 텍스트가 입력되지 않는다.
    이 문제를 해결하기 위해 default_text속성을 추가하여, state가 "disabled"일 때에도 텍스트가 입력할 될 수 있도록 한다.

    :param default_text: 텍스트박스에 아무것도 입력되지 않았을 때 보여질 기본 텍스트.
    """

    def __init__(
        self,
        master,
        width: int = 200,
        height: int = 200,
        corner_radius: int | None = None,
        border_width: int | None = None,
        border_spacing: int = 3,
        bg_color: str | tuple[str, str] = "transparent",
        fg_color: str | tuple[str, str] | None = None,
        border_color: str | tuple[str, str] | None = None,
        text_color: str | None = None,
        scrollbar_button_color: str | tuple[str, str] | None = None,
        scrollbar_button_hover_color: str | tuple[str, str] | None = None,
        font: tuple | ctk.CTkFont | None = None,
        activate_scrollbars: bool = True,
        #
        default_text: str = "",
        **kwargs,
    ):
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            border_spacing,
            bg_color,
            fg_color,
            border_color,
            text_color,
            scrollbar_button_color,
            scrollbar_button_hover_color,
            font,
            activate_scrollbars,
            **kwargs,
        )

        state = kwargs.get("state", "normal")
        self._state = state
        self.configure(state="normal")
        self.insert("1.0", default_text)
        self.configure(state=state)
