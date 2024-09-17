import customtkinter as ctk
import widgets


class FormField(ctk.CTkFrame):
    """내부 요소들이 세로방향으로 배치되는 FormField 컴포넌트"""

    def __init__(
        self,
        master,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | tuple[str, str] = "transparent",
        fg_color: str | tuple[str, str] = "transparent",
        border_color: str | tuple[str, str] | None = None,
        background_corner_colors: tuple[str | tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        #
        title_text: str = "",
        sub_text: str | None = None,
        placeholder_text: str = "",
        input_height: int = 30,
        **kwargs
    ):
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            **kwargs,
        )

        self._title_label = ctk.CTkLabel(
            self,
            fg_color="transparent",
            text=title_text,
            font=("Arial", 14, "bold"),
            anchor="w",
        )
        self._title_label.pack(side="top", fill="x", padx=2)

        self._input = widgets.Input(
            self,
            placeholder_text=placeholder_text,
        )
        self._input.pack(side="top", fill="both", expand=True)

        self._erase_button = widgets.Button(
            self,
            text="지우기 ⌫",
            text_key="erase_button",
            width=80,
            fg_color=ctk.ThemeManager.theme["CTkEntry"]["fg_color"],
            command=self._input.clear,
        )
        self._erase_button.pack(side="left", fill="y")

        if sub_text:
            self._sub_label = ctk.CTkLabel(
                self,
                fg_color="transparent",
                height=20,
                text=sub_text,
                text_color="gray",
                anchor="w",
                font=("Arial", 12),
            )
            self._sub_label.pack(side="top", fill="x", padx=2)
