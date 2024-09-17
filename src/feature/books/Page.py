import customtkinter as ctk
import widgets
import widgets.Table as table
from db import Book
import math
from feature import books


class Page(ctk.CTkFrame):
    def _search(self, page: int) -> None:
        filter = self.search_filter_select.get()
        term = self.search_input.get()
        per_page = self.per_page_select.get()

        raw_result: list[Book]
        try:
            if not term:
                raw_result = list(Book.select())
            else:
                raw_result = list(Book.select().where(Book[filter] == term))
        except Exception:
            raw_result = []

        result: list[Book] = raw_result[(page - 1) * per_page : page * per_page]
        total_count: int = len(raw_result)
        total_page: int = math.ceil(total_count / per_page) if total_count > 0 else 1

        self._table.clear()
        for i, book in enumerate(result, per_page * (page - 1)):
            self._table.append(i, book)

        self.page = page
        self.pagination.set_page(page, total_page)

    def __init__(
        self,
        master,
    ):
        super().__init__(master, fg_color="transparent")
        self.page = 1

        search_frame = ctk.CTkFrame(self, fg_color="transparent")
        search_frame.pack(side="top", fill="x")

        book_add_btn = widgets.Button(
            search_frame,
            text="도서 추가 ✚",
            text_key="books_page_add_book_button",
            width=100,
            height=30,
            command=lambda: books.AddDialog.show(
                on_close=lambda: self._search(self.page)
            ),
        )
        book_add_btn.pack(side="left")

        search_term_frame = ctk.CTkFrame(search_frame)
        search_term_frame.pack(side="left", fill="x", expand=True, padx=10)

        self.search_filter_select = widgets.Select(
            search_term_frame,
            width=100,
            height=30,
            anchor="center",
            options={
                "books_page_search_filter_select_title": "title",
                "books_page_search_filter_select_author": "author",
                "books_page_search_filter_select_publisher": "publisher",
            },
        )
        self.search_filter_select.pack(side="left", fill="y")

        self.search_input = widgets.Input(
            search_term_frame,
            height=30,
            placeholder_text_key="search_input_placeholder",
        )
        self.search_input.pack(side="left", fill="both", expand=True)

        self.search_input_erase_button = widgets.Button(
            search_term_frame,
            text_key="erase_button",
            width=80,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkEntry"]["fg_color"],
            command=self.search_input.clear,
        )
        self.search_input_erase_button.pack(side="left")

        search_button = widgets.Button(
            search_frame,
            text="검색 🔍",
            text_key="search_button",
            width=100,
            height=30,
            command=lambda: self._search(1),
        )
        search_button.pack(side="left")

        # --------------------------------------------
        self._table = table.Table[Book](
            self,
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
                    command=lambda book: books.EditDialog.show(
                        book,
                        on_close=lambda: self._search(self.page),
                    ),
                ),
                table.Column(
                    widget=table.Widget.BUTTON,
                    text="삭제",
                    text_key="books_page_table_column_delete",
                    width=40,
                    anchor=table.Anchor.CENTER,
                    getter=lambda _: "🗑️",
                    command=lambda book: books.DeleteDialog.show(
                        book,
                        on_close=lambda: self._search(self.page),
                    ),
                ),
            ],
        )
        self._table.pack(expand=True, fill="both", pady=10)

        # --------------------------------------------
        footer_frame = ctk.CTkFrame(self, fg_color="transparent")
        footer_frame.pack(fill="x")

        self.per_page_select = widgets.Select(
            footer_frame,
            width=120,
            height=30,
            anchor="center",
            options={
                "10_per_page": 10,
                "20_per_page": 20,
                "30_per_page": 30,
            },
        )
        self.per_page_select.pack(side="left")

        self.pagination = widgets.Pagination(
            footer_frame,
            default_page=self.page,
            default_total_page=1,
            on_prev_click=lambda: self._search(self.page - 1),
            on_next_click=lambda: self._search(self.page + 1),
        )
        self.pagination.pack(side="right")
