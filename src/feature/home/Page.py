from typing import Tuple, Any, Callable
import customtkinter as ctk
import widgets


class Page(ctk.CTkFrame):

    def __init__(
        self,
        master: Any,
        width: int = 200,
        height: int = 200,
        corner_radius: int = 0,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] = "transparent",
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        **kwargs,
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
            **kwargs,
        )

        header_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )
        header_frame.pack(side="top", fill="x")

        ctk.CTkLabel(
            header_frame,
            text="대출코드 🪪",
            width=100,
            fg_color=ctk.ThemeManager.theme["CTkButton"]["fg_color"],
        ).pack(side="left")

        widgets.Input(
            header_frame,
            fg_color="transparent",
            placeholder_text="대출코드를 입력하세요.",
            height=30,
        ).pack(side="left", fill="x", expand=True, padx=10)

        ctk.CTkButton(
            header_frame,
            border_width=0,
            text="검색 🔍",
            width=100,
        ).pack(side="right")
