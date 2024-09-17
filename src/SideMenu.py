import customtkinter as ctk
from typing import Any, Callable, Tuple
import widgets


class SideMenu(ctk.CTkFrame):

    def select_initial(self, btn: ctk.CTkButton):
        btn.configure(fg_color=ctk.ThemeManager.theme["CTkButton"]["fg_color"])
        self.last_selected_btn = btn

    def _select_btn(self, btn: ctk.CTkButton):
        if self.last_selected_btn:
            self.last_selected_btn.configure(fg_color="transparent")
        self.last_selected_btn = btn
        btn.configure(fg_color=ctk.ThemeManager.theme["CTkButton"]["fg_color"])

    def add_btn(
        self,
        text: str = "",
        text_key: str | None = None,
        on_click: Callable[[], None] = lambda: None,
    ) -> ctk.CTkButton:
        btn = widgets.Button(
            self.center_frame,
            text=text,
            text_key=text_key,
            height=50,
            text_color=("#111111", "gray98"),  # TODO: 테마에 맞게 나중에 일괄수정 필요
            font=("Arial", 14),
            fg_color="transparent",
        )

        def command():
            self._select_btn(btn)
            on_click()

        btn.configure(command=command)
        btn.pack()
        return btn

    def __init__(
        self,
        master: Any,
        width: int = 200,
        height: int = 200,
        corner_radius: int = 0,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
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
        self.center_frame.pack(side="left", fill="x")
