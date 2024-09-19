from typing import Any, Tuple
from db import Book
import customtkinter as ctk
import widgets
import widgets.Table as table


class Page(ctk.CTkFrame):
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

        loan_code_frame = ctk.CTkFrame(self, fg_color="transparent")
        loan_code_frame.pack(fill="x", pady=5)

        widgets.Button(
            loan_code_frame,
            text_key="loan_return_page_loan_code_label",
            width=180,
            height=30,
        ).pack(side="left")

        loan_code_term_frame = ctk.CTkFrame(loan_code_frame, fg_color="transparent")
        loan_code_term_frame.pack(side="left", fill="x", expand=True, padx=10)

        self.loan_code_term_input = widgets.Input(
            loan_code_term_frame,
            height=30,
            placeholder_text_key="loan_return_page_loan_code_placeholder",
        )
        self.loan_code_term_input.pack(side="left", fill="x", expand=True)

        widgets.Button(
            loan_code_term_frame,
            width=80,
            height=30,
            text_key="erase_button",
            fg_color=ctk.ThemeManager.theme["CTkEntry"]["fg_color"],
            command=self.loan_code_term_input.clear,
        ).pack(side="left")

        widgets.Button(
            loan_code_frame,
            width=100,
            height=30,
            text_key="search_button",
        ).pack(side="left")

        # ----------------------------------------------------------------------
        tables_frame = ctk.CTkFrame(self, fg_color="transparent")
        tables_frame.pack(fill="both", expand=True, pady=5)

        self._loaning_table = table.Table[Book](
            tables_frame,
            column_def=[
                table.Column(
                    text="제목",
                    text_key="books_page_table_column_title",
                    width=100,
                    anchor=table.Anchor.W,
                    expand=True,
                    getter=lambda book: str(book.title),
                ),
                table.Column(
                    text="저자",
                    text_key="books_page_table_column_author",
                    width=120,
                    anchor=table.Anchor.W,
                    getter=lambda book: str(book.author),
                ),
                table.Column(
                    text="출판사",
                    text_key="books_page_table_column_publisher",
                    width=120,
                    anchor=table.Anchor.W,
                    getter=lambda book: str(book.publisher),
                ),
                table.Column(
                    text="분류번호",
                    text_key="books_page_table_column_classification_num",
                    width=80,
                    anchor=table.Anchor.W,
                    getter=lambda book: str(book.classification_num),
                ),
                table.Column(
                    widget=table.Widget.BUTTON,
                    text="수정",
                    text_key="books_page_table_column_edit",
                    width=40,
                    anchor=table.Anchor.CENTER,
                    getter=lambda _: "📝",
                ),
                table.Column(
                    widget=table.Widget.BUTTON,
                    text="삭제",
                    text_key="books_page_table_column_delete",
                    width=40,
                    anchor=table.Anchor.CENTER,
                    getter=lambda _: "🗑️",
                ),
            ],
        )
        self._loaning_table.pack(fill="both", expand=True)

        # ----------------------------------------------------------------------
        self._return_table = table.Table[Book](
            tables_frame,
            column_def=[
                table.Column(
                    text="제목",
                    text_key="books_page_table_column_title",
                    width=100,
                    anchor=table.Anchor.W,
                    expand=True,
                    getter=lambda book: str(book.title),
                ),
                table.Column(
                    text="저자",
                    text_key="books_page_table_column_author",
                    width=120,
                    anchor=table.Anchor.W,
                    getter=lambda book: str(book.author),
                ),
                table.Column(
                    text="출판사",
                    text_key="books_page_table_column_publisher",
                    width=120,
                    anchor=table.Anchor.W,
                    getter=lambda book: str(book.publisher),
                ),
                table.Column(
                    text="분류번호",
                    text_key="books_page_table_column_classification_num",
                    width=80,
                    anchor=table.Anchor.W,
                    getter=lambda book: str(book.classification_num),
                ),
                table.Column(
                    widget=table.Widget.BUTTON,
                    text="수정",
                    text_key="books_page_table_column_edit",
                    width=40,
                    anchor=table.Anchor.CENTER,
                    getter=lambda _: "📝",
                ),
                table.Column(
                    widget=table.Widget.BUTTON,
                    text="삭제",
                    text_key="books_page_table_column_delete",
                    width=40,
                    anchor=table.Anchor.CENTER,
                    getter=lambda _: "🗑️",
                ),
            ],
        )
        self._return_table.pack(fill="both", expand=True)
