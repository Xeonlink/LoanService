from typing import Any, Tuple
import customtkinter as ctk
from components.Input import Input


class FormField(ctk.CTkFrame):
    """내부 요소들이 세로방향으로 배치되는 FormField 컴포넌트"""

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

        self._title_label = ctk.CTkLabel(
            self,
            corner_radius=0,
            fg_color="transparent",
            text=title_text,
            font=("Arial", 14, "bold"),
            anchor="w",
        )
        self._title_label.pack(side="top", fill="x", padx=2)

        self._input = Input(
            self,
            corner_radius=0,
            fg_color="transparent",
            placeholder_text=placeholder_text,
            height=input_height,
        )
        self._input.pack(side="top", fill="x")

        if sub_text:
            self._sub_label = ctk.CTkLabel(
                self,
                corner_radius=0,
                fg_color="transparent",
                height=20,
                text=sub_text,
                text_color="gray",
                anchor="w",
                font=("Arial", 12),
            )
            self._sub_label.pack(side="top", fill="x", padx=2)
