from typing import Literal
from db import User
import collections.abc as c
import customtkinter as ctk
import widgets
import re
import random
import widgets


class AddDialog(ctk.CTkToplevel):
    dialog: ctk.CTkToplevel | None = None
    mode: Literal["recreate", "focus"] = "focus"

    @classmethod
    def show(cls, on_close: c.Callable[[], None] | None = None) -> None:

        if cls.dialog is None:
            cls.dialog = cls(on_close=on_close)
            return

        if cls.mode == "recreate":
            cls.dialog.destroy()
            cls.dialog = cls(on_close=on_close)
        elif cls.mode == "focus":
            cls.dialog.focus_set()

    def _reset_all(self) -> None:
        self.loan_code_field.clear()
        self.name_field.clear()
        self.contact_field.clear()

    def _on_add_click(self) -> None:
        self.error_textbox.configure(state="normal")
        self.error_textbox.delete(1.0, "end")

        is_fail = False
        loan_code = self.loan_code_field.get()
        if not loan_code:
            self.error_textbox.insert("end", "대출코드를 입력하세요.\n")
            is_fail = True

        if User.is_loan_code_exist(loan_code):
            self.error_textbox.insert("end", "이미 등록된 대출코드입니다.\n")
            is_fail = True

        name = self.name_field.get()
        if not name:
            self.error_textbox.insert("end", "이름을 입력하세요.\n")
            is_fail = True

        contact = self.contact_field.get()
        if not contact:
            self.error_textbox.insert("end", "전화번호를 입력하세요.\n")
            is_fail = True

        elif not re.match(r"\d{3}-\d{3,4}-\d{4}", contact):
            self.error_textbox.insert("end", "전화번호 형식이 올바르지 않습니다.\n")
            is_fail = True

        self.error_textbox.configure(state="disabled")
        if is_fail:
            return

        User.create(
            loan_code=loan_code,
            name=name,
            contact=contact,
        )
        self._close()

    def _debug_fill(self) -> None:
        self.loan_code_field.set(str(random.randrange(100000, 999999)))
        self.name_field.set(["홍길동", "김철수", "이영희"][random.randrange(0, 3)])
        self.contact_field.set(
            f"010-{random.randrange(1000,9999)}-{random.randrange(1000,9999)}"
        )

    def _close(self) -> None:
        AddDialog.dialog = None
        if self._on_close:
            self._on_close()
        self.destroy()

    def __init__(
        self,
        *args,
        fg_color: str | tuple[str, str] | None = None,
        #
        on_close: c.Callable[[], None] | None = None,
        **kwargs,
    ):
        super().__init__(*args, fg_color=fg_color, **kwargs)

        self._on_close = on_close

        self.title("👨🏼‍🏫 회원 추가")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self._close)

        root_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
            width=500,
        )
        root_frame.pack(padx=10, pady=5, fill="both", expand=True)

        # --------------------------------------------------
        ctk.CTkButton(
            root_frame,
            text="🔥 테스트용으로 채우기",
            border_width=0,
            command=self._debug_fill,
        ).pack(side="top", fill="x", pady=5)

        # --------------------------------------------------
        self.loan_code_field = widgets.FormFieldH(
            root_frame,
            title_text="🪪 대출코드*",
            sub_text="대출코드를 설정해주세요.",
            placeholder_text="ex) 123456",
        )
        self.loan_code_field.pack(side="top", fill="x", pady=5)

        self.name_field = widgets.FormFieldH(
            root_frame,
            title_text="㊔ 이름*",
            sub_text="이름을 입력하세요",
            placeholder_text="ex) 홍길동",
        )
        self.name_field.pack(side="top", fill="x", pady=5)

        self.contact_field = widgets.FormFieldH(
            root_frame,
            title_text="☎ 연락처*",
            sub_text="전화번호를 입력하세요.",
            placeholder_text="ex) 010-1234-5678",
        )
        self.contact_field.pack(side="top", fill="x", pady=5)

        # --------------------------------------------------
        self.error_textbox = ctk.CTkTextbox(
            root_frame,
            height=150,
            fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
            state="disabled",
        )
        self.error_textbox.pack(side="top", fill="x", pady=5, expand=True)

        # --------------------------------------------------
        action_frame = ctk.CTkFrame(root_frame)
        action_frame.pack(side="top", fill="x", pady=5)

        close_btn = ctk.CTkButton(
            action_frame,
            text="닫기 ⛌",
            border_width=0,
            command=self._close,
            fg_color="transparent",
            width=120,
        )
        close_btn.pack(side="left", fill="x", expand=True)

        clear_btn = ctk.CTkButton(
            action_frame,
            text="모두 지우기 ⌫",
            border_width=0,
            command=self._reset_all,
            fg_color="transparent",
            width=120,
        )
        clear_btn.pack(side="left", fill="x", expand=True)

        add_btn = ctk.CTkButton(
            action_frame,
            text="추가하기 ✚",
            border_width=0,
            command=self._on_add_click,
            width=120,
        )
        add_btn.pack(side="left", fill="x", expand=True)
