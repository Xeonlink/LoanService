from collections.abc import Callable
import customtkinter as ctk
import widgets


class ButtonDef:
    def __init__(
        self,
        text: str = "",
        text_key: str | None = None,
        on_click: Callable[[], None] | None = None,
    ):
        self.text = text
        self.text_key = text_key
        self.on_click = on_click


class TopMenu(ctk.CTkFrame):

    def _select_btn(self, btn: ctk.CTkButton):
        if self.last_selected_btn:
            self.last_selected_btn.configure(fg_color="transparent")
        self.last_selected_btn = btn
        btn.configure(fg_color=ctk.ThemeManager.theme["CTkButton"]["fg_color"])

    def _create_btn(self, button_def: ButtonDef) -> ctk.CTkButton:
        def command():
            self._select_btn(btn)
            if button_def.on_click is not None:
                button_def.on_click()

        btn = widgets.Button(
            self.center_frame,
            text=button_def.text,
            text_key=button_def.text_key,
            height=50,
            text_color=("#111111", "gray98"),  # TODO: 테마에 맞게 나중에 일괄수정 필요
            font=("Arial", 14),
            fg_color="transparent",
            command=command,
        )
        btn.pack(side="left")
        return btn

    def __init__(
        self,
        master,
        width: int = 200,
        height: int = 200,
        corner_radius: int = 0,
        border_width: int | str | None = None,
        bg_color: str | tuple[str, str] = "transparent",
        fg_color: str | tuple[str, str] | None = None,
        border_color: str | tuple[str, str] | None = None,
        background_corner_colors: tuple[str | tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        #
        button_defs: list[ButtonDef] | None = None,
        **kwargs
    ):
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            **kwargs
        )

        self.last_selected_btn: ctk.CTkButton | None = None

        self.center_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )
        self.center_frame.pack(side="left", expand=True)

        if button_defs is not None:
            self.buttons: list[ctk.CTkButton] = []
            for button_def in button_defs:
                self.buttons.append(self._create_btn(button_def))
        else:
            self.buttons: list[ctk.CTkButton] = []
