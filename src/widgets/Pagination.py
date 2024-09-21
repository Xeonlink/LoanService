import collections.abc as c
import customtkinter as ctk
import widgets


class Pagination(ctk.CTkFrame):

    def set_page(self, page: int, total_page: int) -> None:
        """현재 페이지번호와 전체 페이지번호를 설정"""

        if total_page < page:
            print("Invalid page number : total_page < page")
            page = total_page

        self.prev_btn.configure(state="normal" if page > 1 else "disabled")
        self.page_label.configure(text=f"{page} / {total_page}")
        self.next_btn.configure(state="normal" if page < total_page else "disabled")

    def __init__(
        self,
        master,
        width: int = 200,
        height: int = 30,
        corner_radius: int = 0,
        border_width: int | str | None = None,
        bg_color: str | tuple[str, str] = "transparent",
        fg_color: str | tuple[str, str] = "transparent",
        border_color: str | tuple[str, str] | None = None,
        background_corner_colors: tuple[str | tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        #
        label_width: int = 100,
        button_width: int = 70,
        default_page: int = 1,
        default_total_page: int = 1,
        on_prev_click: c.Callable[[], None] | None = None,
        on_next_click: c.Callable[[], None] | None = None,
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

        self.prev_btn = widgets.Button(
            self,
            text="◀ 이전",
            text_key="pagination_prev",
            width=button_width,
            height=height,
            fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
            state="disabled" if default_page == 1 else "normal",
            command=on_prev_click,
        )
        self.prev_btn.pack(side="left")

        self.page_label = ctk.CTkLabel(
            self,
            text=f"{default_page} / {default_total_page}",
            width=label_width,
            height=height,
        )
        self.page_label.pack(side="left")

        self.next_btn = widgets.Button(
            self,
            text="다음 ▶",
            text_key="pagination_next",
            width=button_width,
            height=height,
            fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
            state="disabled" if default_page == default_total_page else "normal",
            command=on_next_click,
        )
        self.next_btn.pack(side="left")
