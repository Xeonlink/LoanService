from db import User
from collections.abc import Callable
import customtkinter as ctk
import widgets


class DeleteDialog(widgets.Dialog):
    _dialog: widgets.Dialog | None = None

    @classmethod
    def show(cls, user: User, on_destroy: Callable[[], None] | None = None) -> None:
        if cls._dialog is not None:
            cls._dialog.destroy()

        cls._dialog = cls(user, on_destroy)
        cls._dialog.lift()
        cls._dialog.focus_set()

    def _delete(self) -> None:
        self._user.delete_instance()
        self.destroy()

    def __init__(self, user: User, on_destroy: Callable[[], None] | None = None):
        super().__init__(
            title_key="dialog_delete_title",
            resizable=(False, False),
            on_destroy=on_destroy,
            pad=(10, 5),
        )
        self._user = user

        # --------------------------------------------------
        widgets.Label(
            self.root_frame,
            text="정말 삭제하시겠습니까?",
            font=("Arial", 14, "bold"),
            anchor="w",
        ).pack(side="top", fill="x", pady=5)

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
            fg_color="transparent",
            command=self.destroy,
        ).pack(side="left", fill="x", expand=True)

        widgets.Button(
            action_frame,
            text_key="dialog_delete_button",
            border_width=0,
            command=self._delete,
        ).pack(side="left", fill="x", expand=True)

    def destroy(self) -> None:
        DeleteDialog._dialog = None
        return super().destroy()
