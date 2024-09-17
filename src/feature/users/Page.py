from typing import Any
import customtkinter as ctk
import widgets
import widgets.Table as table
from feature import users
from db import User
import math


class Page(ctk.CTkFrame):
    def _search(self, page: int) -> None:
        filter = self.search_filter_select.get()
        term = self.search_term_input.get()
        per_page = self.per_page_select.get()

        raw_result: list[User]
        try:
            if not term:
                raw_result = list(User.select())
            else:
                raw_result = list(User.select().where(User[filter].contains(term)))
        except Exception as e:
            raw_result = []

        result: list[User] = raw_result[(page - 1) * per_page : page * per_page]
        total_count: int = len(raw_result)
        total_page: int = math.ceil(total_count / per_page) if total_count > 0 else 1

        self._table.clear()
        for i in range(len(result)):
            user: User = result[i]
            self._table.append(i + per_page * (page - 1), user)

        self.page = page
        self.pagination.set_page(page, total_page)

    def __init__(self, master: Any):
        super().__init__(master, fg_color="transparent")
        self.page = 1

        search_frame = ctk.CTkFrame(self, fg_color="transparent")
        search_frame.pack(side="top", fill="x")

        book_add_btn = widgets.Button(
            search_frame,
            text="회원 추가 ✚",
            text_key="users_page_add_user_button",
            width=100,
            height=30,
            command=lambda: users.AddDialog.show(
                on_close=lambda: self._search(self.page)
            ),
        )
        book_add_btn.pack(side="left")

        search_term_frame = ctk.CTkFrame(search_frame)
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
                # "대출코드": "loan_code",
                "users_page_search_filter_select_name": "name",
                "users_page_serach_filter_select_contact": "contact",
            },
        )
        self.search_filter_select.pack(side="left", ipadx=10)

        self.search_term_input = widgets.Input(
            search_term_frame,
            placeholder_text="검색어를 입력하세요",
            height=30,
        )
        self.search_term_input.pack(side="left", fill="x", expand=True)

        search_btn = widgets.Button(
            search_frame,
            text="검색 🔍",
            text_key="users_page_search_button",
            width=100,
            height=30,
            command=lambda: self._search(1),
        )
        search_btn.pack(side="left")

        # --------------------------------------------
        self._table = table.Table[User](
            self,
            column_def=[
                table.Column(
                    widget=table.Widget.LABEL,
                    text="대출코드",
                    width=120,
                    anchor=table.Anchor.W,
                    getter=lambda user: str(user.loan_code),
                ),
                table.Column(
                    text="이름",
                    width=150,
                    anchor=table.Anchor.W,
                    getter=lambda user: str(user.name),
                ),
                table.Column(
                    text="연락처",
                    width=120,
                    anchor=table.Anchor.W,
                    getter=lambda user: str(user.contact),
                    expand=True,
                ),
                table.Column(
                    widget=table.Widget.BUTTON,
                    text="수정",
                    width=40,
                    getter=lambda _: "📝",
                    command=lambda user: users.EditDialog.show(
                        user=user,
                        on_close=lambda: self._search(self.page),
                    ),
                ),
                table.Column(
                    widget=table.Widget.BUTTON,
                    text="삭제",
                    width=40,
                    getter=lambda _: "🗑️",
                    command=lambda user: users.DeleteDialog.show(
                        user=user,
                        on_close=lambda: self._search(self.page),
                    ),
                ),
            ],
        )
        self._table.pack(expand=True, fill="both", pady=10)

        # --------------------------------------------
        footer_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )
        footer_frame.pack(fill="x")

        self.per_page_select = widgets.Select(
            footer_frame,
            width=120,
            height=30,
            anchor="center",
            command=lambda _: self._search(self.page),
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
