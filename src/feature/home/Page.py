import customtkinter as ctk
import widgets


class Page(ctk.CTkFrame):

    def __init__(
        self,
        master,
        width: int = 200,
        height: int = 200,
        corner_radius: int = 0,
        border_width: int | str | None = None,
        bg_color: str | tuple[str, str] = "transparent",
        fg_color: str | tuple[str, str] = "transparent",
        border_color: str | tuple[str, str] | None = None,
        background_corner_colors: tuple[str | tuple[str, str]] | None = None,
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

        search_frame = ctk.CTkFrame(header_frame, fg_color="transparent", height=30)
        search_frame.pack(side="left", fill="x", expand=True, padx=10)

        widgets.Input(
            search_frame,
            placeholder_text="대출코드를 입력하세요.",
            height=30,
        ).pack(side="left", fill="both", expand=True)

        widgets.Button(
            search_frame,
            fg_color=ctk.ThemeManager.theme["CTkEntry"]["fg_color"],
            text_key="erase_button",
            width=80,
        ).pack(side="left", fill="y")

        ctk.CTkButton(
            header_frame,
            border_width=0,
            text="검색 🔍",
            width=100,
        ).pack(side="left")
