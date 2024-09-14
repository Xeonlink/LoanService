from typing import Any
import customtkinter as ctk
import components as cmp
from feature import books
from db import Book
import math


class Page(ctk.CTkFrame):
    def _search(
        self,
        filter: str,
        term: str,
        per_page: int,
        page: int,
    ) -> None:
        raw_result: list[Book]
        try:
            if not term:
                raw_result = list(Book.select())
            else:
                raw_result = list(Book.select().where(Book[filter].contains(term)))
        except Exception as e:
            raw_result = []

        result: list[Book] = raw_result[(page - 1) * per_page : page * per_page]
        total_count: int = len(raw_result)
        total_page: int = math.ceil(total_count / per_page) if total_count > 0 else 1

        self._clear_tbody()
        for i in range(per_page * (page - 1), per_page * (page - 1) + len(result)):
            book: Book = result[i]
            tr_frame = self._create_book_tr(i, book)
            tr_frame.pack(side="top", fill="x")

        self.page = page
        self.pagination.set_page(page, total_page)

    def _create_book_tr(self, index: int, book: Book) -> ctk.CTkFrame:
        tr_frame = ctk.CTkFrame(
            self.tbody_frame,
            corner_radius=0,
            fg_color="transparent",
        )

        index_td_label = ctk.CTkLabel(
            tr_frame,
            text=str(index + 1),
            width=40,
            height=30,
            corner_radius=0,
        )
        index_td_label.pack(side="left")

        title_td_label = ctk.CTkLabel(
            tr_frame,
            text=str(book.title),
            width=100,
            height=30,
            corner_radius=0,
            anchor="w",
        )
        title_td_label.pack(side="left", fill="x", expand=True)

        author_td_label = ctk.CTkLabel(
            tr_frame,
            text=str(book.author),
            width=120,
            height=30,
            corner_radius=0,
            anchor="w",
        )
        author_td_label.pack(side="left")

        publisher_td_label = ctk.CTkLabel(
            tr_frame,
            text=str(book.publisher),
            width=120,
            height=30,
            corner_radius=0,
            anchor="w",
        )
        publisher_td_label.pack(side="left")

        classification_num_td_label = ctk.CTkLabel(
            tr_frame,
            text=str(book.classification_num),
            width=80,
            height=30,
            corner_radius=0,
            anchor="w",
        )
        classification_num_td_label.pack(side="left")

        modifiy_td_label = ctk.CTkButton(
            tr_frame,
            text="📝",
            width=40,
            height=30,
            corner_radius=0,
            fg_color="transparent",
            command=lambda: self._show_book_edit_toplevel(book),
        )
        modifiy_td_label.pack(side="left")

        delete_td_label = ctk.CTkButton(
            tr_frame,
            text="🗑️",
            width=40,
            height=30,
            corner_radius=0,
            fg_color="transparent",
            command=lambda: self._show_book_delete_toplevel(book),
        )
        delete_td_label.pack(side="left")

        return tr_frame

    def _on_book_add_close(self) -> None:
        self.add_dialog = None
        self._re_search()
        return

    def _show_book_add_toplevel(self) -> None:
        if self.add_dialog is None:
            self.add_dialog = books.AddDialog(
                self,
                on_close=self._on_book_add_close,
            )
            return

        self.add_dialog.focus_set()

    def _on_book_edit_close(self) -> None:
        self.edit_dialog = None
        self._re_search()
        return

    def _show_book_edit_toplevel(self, book: Book) -> None:
        if self.edit_dialog is None:
            self.edit_dialog = books.EditDialog(
                self,
                book=book,
                on_close=self._on_book_edit_close,
            )
            return

        self.edit_dialog.destroy()
        self.edit_dialog = books.EditDialog(
            self,
            book=book,
            on_close=self._on_book_edit_close,
        )

    def _on_book_delete_close(self) -> None:
        self.delete_dialog = None
        self._re_search()
        return

    def _show_book_delete_toplevel(self, book: Book) -> None:
        if self.delete_dialog is None:
            self.delete_dialog = books.DeleteDialog(
                self,
                book=book,
                on_close=self._on_book_delete_close,
            )
            return

        self.delete_dialog.destroy()
        self.delete_dialog = books.DeleteDialog(
            self,
            book=book,
            on_close=self._on_book_delete_close,
        )

    def _clear_tbody(self) -> None:
        for widget in self.tbody_frame.winfo_children():
            widget.destroy()

    def __init__(self, master: Any):
        super().__init__(master, corner_radius=0, fg_color="transparent")

        self.add_dialog: books.AddDialog | None = None
        self.edit_dialog: books.EditDialog | None = None
        self.delete_dialog: books.DeleteDialog | None = None
        self.page = 1

        search_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )
        search_frame.pack(side="top", fill="x")

        book_add_btn = ctk.CTkButton(
            search_frame,
            text="도서 추가 ✚",
            width=100,
            height=30,
            corner_radius=0,
            command=self._show_book_add_toplevel,
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

        self.search_filter_map = {
            "도서명": "title",
            "저자": "author",
            "출판사": "publisher",
        }
        self.search_filter_combobox = ctk.CTkOptionMenu(
            search_term_frame,
            width=100,
            height=30,
            values=["도서명", "저자", "출판사"],
            corner_radius=0,
            anchor="center",
        )
        self.search_filter_combobox.pack(side="left", ipadx=10)

        self.search_term_input = cmp.Input(
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
            corner_radius=0,
            command=self._on_search_click,
        )
        search_btn.pack(side="left")

        # --------------------------------------------
        gap_frame = ctk.CTkFrame(self, height=10, fg_color="transparent")
        gap_frame.pack(fill="x")

        # --------------------------------------------
        table_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
        )
        table_frame.pack(expand=True, fill="both")

        thead_frame = ctk.CTkFrame(
            table_frame,
            corner_radius=0,
        )
        thead_frame.pack(side="top", fill="x")

        tr_frame = ctk.CTkFrame(
            thead_frame,
            corner_radius=0,
            fg_color=ctk.ThemeManager.theme["CTkEntry"]["fg_color"],
        )
        tr_frame.pack(side="top", fill="x")

        index_td_label = ctk.CTkLabel(
            tr_frame,
            text="번호",
            width=40,
            height=30,
            corner_radius=0,
        )
        index_td_label.pack(side="left")

        title_td_label = ctk.CTkLabel(
            tr_frame,
            text="제목",
            width=100,
            height=30,
            corner_radius=0,
            anchor="w",
        )
        title_td_label.pack(side="left", fill="x", expand=True)

        author_td_label = ctk.CTkLabel(
            tr_frame,
            text="저자",
            width=120,
            height=30,
            corner_radius=0,
            anchor="w",
        )
        author_td_label.pack(side="left")

        publisher_td_label = ctk.CTkLabel(
            tr_frame,
            text="출판사",
            width=120,
            height=30,
            corner_radius=0,
            anchor="w",
        )
        publisher_td_label.pack(side="left")

        classification_num_td_label = ctk.CTkLabel(
            tr_frame,
            text="분류번호",
            width=80,
            height=30,
            corner_radius=0,
            anchor="w",
        )
        classification_num_td_label.pack(side="left")

        modifiy_td_label = ctk.CTkLabel(
            tr_frame,
            text="수정",
            width=40,
            height=30,
            corner_radius=0,
        )
        modifiy_td_label.pack(side="left")

        delete_td_label = ctk.CTkLabel(
            tr_frame,
            text="삭제",
            width=40,
            height=30,
            corner_radius=0,
        )
        delete_td_label.pack(side="left")

        self.tbody_frame = ctk.CTkFrame(
            table_frame,
            corner_radius=0,
            fg_color="transparent",
        )
        self.tbody_frame.pack(fill="both", expand=True)

        # --------------------------------------------
        gap_frame = ctk.CTkFrame(self, height=10, fg_color="transparent")
        gap_frame.pack(fill="x")

        # --------------------------------------------
        footer_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )
        footer_frame.pack(fill="x")

        footer_left_frame = ctk.CTkFrame(
            footer_frame,
            corner_radius=0,
            fg_color="transparent",
            height=30,
            # width=50,
        )
        footer_left_frame.pack(side="left", fill="x", expand=True)

        self.per_page_map = {
            "10개씩 보기": 10,
            "20개씩 보기": 20,
            "30개씩 보기": 30,
        }
        self.per_page_combobox = ctk.CTkOptionMenu(
            footer_left_frame,
            width=120,
            height=30,
            values=list(self.per_page_map.keys()),
            corner_radius=0,
            anchor="center",
        )
        self.per_page_combobox.pack(side="left")

        self.pagination = cmp.Pagination(
            footer_frame,
            page=self.page,
            total_page=1,
            on_prev_click=self._on_prev_click,
            on_next_click=self._on_next_click,
        )
        self.pagination.pack(side="left")

    def _on_prev_click(self):
        filter = self.search_filter_map[self.search_filter_combobox.get()]
        per_page = self.per_page_map[self.per_page_combobox.get()]
        self._search(
            filter=filter,
            term=self.search_term_input.get(),
            per_page=per_page,
            page=self.page - 1,
        )

    def _on_next_click(self):
        filter = self.search_filter_map[self.search_filter_combobox.get()]
        per_page = self.per_page_map[self.per_page_combobox.get()]
        self._search(
            filter=filter,
            term=self.search_term_input.get(),
            per_page=per_page,
            page=self.page + 1,
        )

    def _on_search_click(self):
        filter = self.search_filter_map[self.search_filter_combobox.get()]
        per_page = self.per_page_map[self.per_page_combobox.get()]
        self._search(
            filter=filter,
            term=self.search_term_input.get(),
            per_page=per_page,
            page=1,
        )

    def _re_search(self):
        filter = self.search_filter_map[self.search_filter_combobox.get()]
        per_page = self.per_page_map[self.per_page_combobox.get()]
        self._search(
            filter=filter,
            term=self.search_term_input.get(),
            per_page=per_page,
            page=self.page,
        )
