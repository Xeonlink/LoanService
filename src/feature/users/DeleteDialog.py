from typing import Any, Callable, Tuple, Literal
from typing import Tuple
import customtkinter as ctk
from db import User


class DeleteDialog(ctk.CTkToplevel):
    dialog: ctk.CTkToplevel | None = None
    mode: Literal["recreate", "focus"] = "recreate"

    @classmethod
    def show(cls, user: User, on_close: Callable[[], Any] | None = None) -> None:

        if cls.dialog is None:
            cls.dialog = cls(user=user, on_close=on_close)
            return

        if cls.mode == "recreate":
            cls.dialog.destroy()
            cls.dialog = cls(user=user, on_close=on_close)
        elif cls.mode == "focus":
            cls.dialog.focus_set()

    def _delete(self) -> None:
        self._user.delete_instance()
        self.close()

    def close(self) -> None:
        if self._on_close:
            self._on_close()
        self.destroy()

    def __init__(
        self,
        *args,
        fg_color: str | Tuple[str, str] | None = None,
        #
        user: User,
        on_close: Callable[[], Any] | None = None,
        **kwargs,
    ):
        super().__init__(*args, fg_color=fg_color, **kwargs)

        self._user = user
        self._on_close = on_close

        self.title("👨🏼‍🏫 회원 삭제")

        root_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
            width=300,
        )
        root_frame.pack(padx=10, pady=5, fill="both", expand=True)

        # --------------------------------------------------
        ctk.CTkLabel(
            root_frame,
            text="정말 삭제하시겠습니까?",
            font=("Arial", 14, "bold"),
            anchor="w",
        ).pack(side="top", fill="x", pady=5)

        # --------------------------------------------------
        action_frame = ctk.CTkFrame(root_frame)
        action_frame.pack(side="top", fill="x", pady=5)

        ctk.CTkButton(
            action_frame,
            text="취소",
            border_width=0,
            fg_color="transparent",
            command=self.close,
        ).pack(side="left", fill="x", expand=True)

        ctk.CTkButton(
            action_frame,
            text="삭제",
            border_width=0,
            command=self._delete,
        ).pack(side="left", fill="x", expand=True)
