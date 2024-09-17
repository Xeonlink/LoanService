from typing import Any
import customtkinter as ctk
import widgets
import widgets.Table as table
from db import Book
import math
from feature import books


class Page(ctk.CTkFrame):
    def _search(self, page: int) -> None:
        filter = self.search_filter_select.get()
        term = self.search_term_input.get()
        per_page = self.per_page_select.get()

        raw_result: list[Book]
        try:
            if not term:
                raw_result = list(Book.select())
            else:
                raw_result = list(Book.select().where(Book[filter].contains(term)))
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

    def __init__(self, master: Any):
        super().__init__(master, fg_color="transparent")
        self.page = 1

        search_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )
        search_frame.pack(side="top", fill="x")

        book_add_btn = ctk.CTkButton(
            search_frame,
            text="도서 추가 ✚",
            width=100,
            height=30,
            command=lambda: books.AddDialog.show(
                on_close=lambda: self._search(self.page)
            ),
        )
        book_add_btn.pack(side="left")

        search_term_frame = ctk.CTkFrame(
            search_frame,
            height=30,
        )
        search_term_frame.pack(
            side="left",
            fill="x",
            expand=True,
            padx=10,
        )

        self.search_filter_select = widgets.Select(
            search_term_frame,
            width=100,
            height=30,
            anchor="center",
            options={
                "도서명": "title",
                "저자": "author",
                "출판사": "publisher",
            },
        )
        self.search_filter_select.pack(side="left", ipadx=10)

        self.search_term_input = widgets.Input(
            search_term_frame,
            placeholder_text="검색어를 입력하세요",
            height=30,
        )
        self.search_term_input.pack(side="left", fill="x", expand=True)

        search_btn = ctk.CTkButton(
            search_frame,
            text="검색 🔍",
            width=100,
            height=30,
            command=lambda: self._search(1),
        )
        search_btn.pack(side="left")

        # --------------------------------------------
        self._table = table.Table[Book](
            self,
            column_def=[
                table.Column(
                    text="제목",
                    width=100,
                    anchor=table.Anchor.W,
                    expand=True,
                    getter=lambda book: str(book.title),
                ),
                table.Column(
                    text="저자",
                    width=120,
                    anchor=table.Anchor.W,
                    getter=lambda book: str(book.author),
                ),
                table.Column(
                    text="출판사",
                    width=120,
                    anchor=table.Anchor.W,
                    getter=lambda book: str(book.publisher),
                ),
                table.Column(
                    text="분류번호",
                    width=80,
                    anchor=table.Anchor.W,
                    getter=lambda book: str(book.classification_num),
                ),
                table.Column(
                    widget=table.Widget.BUTTON,
                    text="수정",
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
                "10개씩 보기": 10,
                "20개씩 보기": 20,
                "30개씩 보기": 30,
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
