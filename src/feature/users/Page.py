from db import User
from feature import users
import customtkinter as ctk
import widgets
import widgets.Table as table
import math


class Page(ctk.CTkFrame):
    def _search(self, page: int) -> None:
        filter = self.search_filter_select.get()
        term = self.search_input.get()
        per_page = self.per_page_select.get()

        result = User.select_safe()
        result = [user for user in result if term in getattr(user, filter)]
        result = result[(page - 1) * per_page : page * per_page]
        total_count: int = len(result)
        total_page: int = math.ceil(total_count / per_page) if total_count > 0 else 1

        self._table.clear()
        for i, user in enumerate(result, per_page * (page - 1)):
            self._table.append(i, user)

        self.page = page
        self.pagination.set_page(page, total_page)

    def __init__(self, master):
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
                on_destroy=lambda: self._search(self.page)
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
                # "대출코드": "loan_code",
                "users_page_search_filter_select_name": "name",
                "users_page_serach_filter_select_contact": "contact",
            },
        )
        self.search_filter_select.pack(side="left")

        self.search_input = widgets.Input(
            search_term_frame,
            height=30,
            placeholder_text_key="search_input_placeholder",
        )
        self.search_input.pack(side="left", fill="x", expand=True)

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
            text_key="search_button",
            width=100,
            height=30,
            command=lambda: self._search(1),
        )
        search_button.pack(side="left")

        # --------------------------------------------
        self._table = table.Table[User](
            self,
            column_def=[
                table.Column(
                    widget=table.Widget.LABEL,
                    text="대출코드",
                    text_key="users_page_table_column_loan_code",
                    width=120,
                    anchor=table.Anchor.W,
                    getter=lambda user: str(user.loan_code),
                ),
                table.Column(
                    text="이름",
                    text_key="users_page_table_column_name",
                    width=150,
                    anchor=table.Anchor.W,
                    getter=lambda user: str(user.name),
                ),
                table.Column(
                    text="연락처",
                    text_key="users_page_table_column_contact",
                    width=120,
                    anchor=table.Anchor.W,
                    getter=lambda user: str(user.contact),
                    expand=True,
                ),
                table.Column(
                    widget=table.Widget.BUTTON,
                    text="수정",
                    text_key="users_page_table_column_edit",
                    width=40,
                    getter=lambda _: "📝",
                    command=lambda user: users.EditDialog.show(
                        user=user,
                        on_destroy=lambda: self._search(self.page),
                    ),
                ),
                table.Column(
                    widget=table.Widget.BUTTON,
                    text="삭제",
                    text_key="users_page_table_column_delete",
                    width=40,
                    getter=lambda _: "🗑️",
                    command=lambda user: users.DeleteDialog.show(
                        user=user,
                        on_destroy=lambda: self._search(self.page),
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
            command=lambda _: self._search(self.page),
            options={
                "10_per_page": 10,
                "20_per_page": 20,
                "30_per_page": 30,
            },
            default_option_key="10_per_page",
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
