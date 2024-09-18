from utils import I18n
from db import User
import collections.abc as c
import customtkinter as ctk
import widgets
import re
import random


class EditDialog(widgets.Dialog):
    _dialog: widgets.Dialog | None = None

    @classmethod
    def show(cls, user: User, on_destroy: c.Callable[[], None] | None = None) -> None:
        if cls._dialog is not None:
            cls._dialog.destroy()

        cls._dialog = cls(user, on_destroy)
        cls._dialog.lift()
        cls._dialog.focus_set()

    def _reset_all(self) -> None:
        self.loan_code_field.set(str(self._user.loan_code))
        self.name_field.set(str(self._user.name))
        self.contact_field.set(str(self._user.contact))

    def _on_update_click(self) -> None:
        self.error_textbox.configure(state="normal")
        self.error_textbox.delete(1.0, "end")

        is_fail = False
        loan_code = self.loan_code_field.get()
        if not loan_code:
            text = I18n.get_text("user_dialog_loan_code_required")
            self.error_textbox.insert("end", text)
            is_fail = True

        if User.is_loan_code_exist(loan_code):
            text = I18n.get_text("user_dialog_loan_code_exist")
            self.error_textbox.insert("end", text)
            is_fail = True

        name = self.name_field.get()
        if not name:
            text = I18n.get_text("user_dialog_name_required")
            self.error_textbox.insert("end", text)
            is_fail = True

        contact = self.contact_field.get()
        if not contact:
            text = I18n.get_text("user_dialog_contact_required")
            self.error_textbox.insert("end", text)
            is_fail = True

        elif not re.match(r"\d{3}-\d{3,4}-\d{4}", contact):
            text = I18n.get_text("user_dialog_contact_invalid")
            self.error_textbox.insert("end", text)
            is_fail = True

        self.error_textbox.configure(state="disabled")
        if is_fail:
            return

        self._user.loan_code = loan_code  # type: ignore
        self._user.name = name  # type: ignore
        self._user.contact = contact  # type: ignore
        self._user.save()
        self.destroy()

    def _debug_fill(self) -> None:
        self.loan_code_field.set(str(random.randrange(100000, 999999)))
        self.name_field.set(["홍길동", "김철수", "이영희"][random.randrange(0, 3)])
        self.contact_field.set(
            f"010-{random.randrange(1000,9999)}-{random.randrange(1000,9999)}"
        )

    def __init__(self, user: User, on_destroy: c.Callable[[], None] | None = None):
        super().__init__(
            title_key="user_edit_dialog_title",
            resizable=(False, False),
            on_destroy=on_destroy,
            pad=(10, 5),
        )
        self._user = user

        # --------------------------------------------------
        ctk.CTkButton(
            self.root_frame,
            text="🔥 테스트용으로 채우기",
            border_width=0,
            command=self._debug_fill,
        ).pack(side="top", fill="x", pady=5)

        # --------------------------------------------------
        self.loan_code_field = widgets.FormFieldH(
            self.root_frame,
            title_text_key="user_dialog_loan_code_label",
            placeholder_text_key="user_dialog_loan_code_placeholder",
            default_text=str(user.loan_code),
        )
        self.loan_code_field.pack(side="top", fill="x", pady=5)

        self.name_field = widgets.FormFieldH(
            self.root_frame,
            title_text_key="user_dialog_name_label",
            placeholder_text_key="user_dialog_name_placeholder",
            default_text=str(user.name),
        )
        self.name_field.pack(side="top", fill="x", pady=5)

        self.contact_field = widgets.FormFieldH(
            self.root_frame,
            title_text_key="user_dialog_contact_label",
            placeholder_text_key="user_dialog_contact_placeholder",
            default_text=str(user.contact),
        )
        self.contact_field.pack(side="top", fill="x", pady=5)

        # --------------------------------------------------
        self.error_textbox = ctk.CTkTextbox(
            self.root_frame,
            height=150,
            fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
            state="disabled",
        )
        self.error_textbox.pack(side="top", fill="x", pady=5, expand=True)

        # --------------------------------------------------
        action_frame = ctk.CTkFrame(self.root_frame)
        action_frame.pack(side="top", fill="x", pady=5)

        widgets.Button(
            action_frame,
            text_key="dialog_close_button",
            border_width=0,
            command=self.destroy,
            fg_color="transparent",
            width=120,
        ).pack(side="left", fill="x", expand=True)

        widgets.Button(
            action_frame,
            text_key="dialog_revert_all_button",
            border_width=0,
            command=self._reset_all,
            fg_color="transparent",
            width=120,
        ).pack(side="left", fill="x", expand=True)

        widgets.Button(
            action_frame,
            text_key="dialog_update_button",
            border_width=0,
            command=self._on_update_click,
            width=120,
        ).pack(side="left", fill="x", expand=True)

    def destroy(self) -> None:
        EditDialog._dialog = None
        return super().destroy()
