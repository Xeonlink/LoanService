from typing import Any, Tuple, Callable
import customtkinter as ctk


class Pagination(ctk.CTkFrame):

    def set_page(self, page: int, total_page: int) -> None:
        """현재 페이지번호와 전체 페이지번호를 설정"""
        if total_page < page:
            print("Invalid page number : total_page < page")
            page = total_page

        self.page = page
        self.total_page = total_page

        self.prev_btn.configure(state="normal" if page > 1 else "disabled")
        self.page_label.configure(text=f"{page} / {total_page}")
        self.next_btn.configure(state="normal" if page < total_page else "disabled")

    def __init__(
        self,
        master: Any,
        page: int = 1,
        total_page: int = 1,
        width: int = 200,
        height: int = 200,
        corner_radius: int = 0,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] = "transparent",
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        #
        label_width: int = 100,
        on_prev_click: Callable[[], Any] | None = None,
        on_next_click: Callable[[], Any] | None = None,
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

        self.page = page
        self.total_page = total_page

        self.prev_btn = ctk.CTkButton(
            self,
            text="◀ 이전",
            width=70,
            height=30,
            corner_radius=0,
            fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
            state="disabled" if page == 1 else "normal",
            command=on_prev_click,
        )
        self.prev_btn.pack(side="left")

        self.page_label = ctk.CTkLabel(
            self,
            text=f"{page} / {total_page}",
            width=label_width,
            height=30,
            corner_radius=0,
        )
        self.page_label.pack(side="left")

        self.next_btn = ctk.CTkButton(
            self,
            text="다음 ▶",
            width=70,
            height=30,
            corner_radius=0,
            fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
            state="disabled" if page == total_page else "normal",
            command=on_next_click,
        )
        self.next_btn.pack(side="left")
