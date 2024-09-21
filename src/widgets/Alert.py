from collections.abc import Callable
import customtkinter as ctk
import widgets


class Alert(widgets.Dialog):
    def __init__(
        self,
        on_destroy: Callable[[], None] | None = None,
        #
        message: str = "",
    ):
        super().__init__(
            title="",
            title_key="dialog_warning_title",
            resizable=(False, False),
            on_destroy=on_destroy,
            pad=(10, 5),
        )

        content_frame = ctk.CTkFrame(self.root_frame, fg_color="transparent")
        content_frame.pack(fill="x", expand=True, pady=5)

        widgets.Label(
            content_frame,
            text="⚠️",
            font=("Arial", 30, "bold"),
            anchor="w",
        ).pack(side="left", fill="x", padx=15, pady=5)

        widgets.TextArea(
            content_frame,
            default_text=message,
            fg_color="transparent",
            width=280,
            height=60,
            state="disabled",
        ).pack(side="left", fill="both")

        actions_frame = ctk.CTkFrame(self.root_frame)
        actions_frame.pack(fill="x", pady=5)

        widgets.Button(
            actions_frame,
            width=100,
            height=30,
            text_key="dialog_close_button",
            fg_color="transparent",
            command=self.destroy,
        ).pack(side="left", fill="x", expand=True)
