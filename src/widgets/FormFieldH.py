import customtkinter as ctk
import widgets


class FormFieldH(ctk.CTkFrame):
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
        lable_width: int = 100,
        text: str | None = None,
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
            **kwargs
        )

        title_label = ctk.CTkLabel(
            self,
            fg_color="transparent",
            text=title_text,
            font=("Arial", 14),
            anchor="w",
            width=lable_width,
        )
        title_label.pack(side="left", fill="x")

        self._input = widgets.Input(
            self,
            placeholder_text=placeholder_text,
        )
        self._input.pack(side="left", fill="both", expand=True)

        self._erase_button = widgets.Button(
            self,
            text="지우기 ⌫",
            text_key="erase_button",
            width=80,
            fg_color=ctk.ThemeManager.theme["CTkEntry"]["fg_color"],
            command=self._input.clear,
        )
        self._erase_button.pack(side="left", fill="y")

    def clear(self):
        self._input.clear()

    def get(self):
        return self._input.get()

    def set(self, value: str):
        self._input.set(value)
