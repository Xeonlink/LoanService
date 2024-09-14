from typing import Any, Tuple
import customtkinter as ctk
from components.Input import Input


class FormFieldH(ctk.CTkFrame):
    def __init__(
        self,
        master: Any,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] = "transparent",
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        #
        title_text: str = "",
        sub_text: str | None = None,
        placeholder_text: str = "",
        input_height: int = 30,
        lable_width: int = 100,
        text: str | None = None,
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

        title_label = ctk.CTkLabel(
            self,
            corner_radius=0,
            fg_color="transparent",
            text=title_text,
            font=("Arial", 14),
            anchor="w",
            width=lable_width,
        )
        title_label.pack(side="left", fill="x")

        self._input = Input(
            self,
            corner_radius=0,
            fg_color="transparent",
            placeholder_text=placeholder_text,
            height=input_height,
            text=text,
        )
        self._input.pack(side="top", fill="x", expand=True)

    def clear(self):
        self._input.clear()

    def get(self):
        return self._input.get()

    def set(self, value: str):
        self._input.set(value)
