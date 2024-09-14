from typing import Tuple, Any
import customtkinter as ctk
import os


class Page(ctk.CTkFrame):
    def _on_theme_click(self, value: str) -> None:
        theme_map = {
            "밝은": "light",
            "어두운": "dark",
            "적응하는": "system",
        }

        appearance_mode = theme_map[value]
        ctk.set_appearance_mode(appearance_mode)

    def __init__(
        self,
        master: Any,
        width: int = 200,
        height: int = 200,
        corner_radius: int = 0,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] = "transparent",
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        **kwargs,
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

        theme_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )
        theme_frame.pack(side="top", fill="x", pady=5)

        theme_label_font = ctk.CTkFont(
            family="Arial",
            size=14,
            weight="bold",
        )
        theme_label = ctk.CTkLabel(
            theme_frame,
            text="🎨 테마 설정",
            font=theme_label_font,
            anchor="w",
        )
        theme_label.pack(side="top", fill="x", expand=True, padx=5)

        theme_segmentedbutton = ctk.CTkSegmentedButton(
            theme_frame,
            corner_radius=0,
            values=["밝은", "어두운", "적응하는"],
            command=self._on_theme_click,
        )
        theme_segmentedbutton.pack(side="top", fill="x", expand=True)
        theme_segmentedbutton.set("적응하는")

        theme_sublabel = ctk.CTkLabel(
            theme_frame,
            text="변경할 테마를 선택할 수 있습니다.",
            anchor="w",
        )
        theme_sublabel.pack(side="top", fill="x", expand=True, padx=5)

        license_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )
        license_frame.pack(side="top", fill="x", pady=5)

        license_label_font = ctk.CTkFont(
            family="Arial",
            size=14,
            weight="bold",
        )
        license_label = ctk.CTkLabel(
            license_frame,
            text="👀 오픈소스 라이센스",
            anchor="w",
            font=license_label_font,
        )
        license_label.pack(side="top", padx=5, fill="x")

        license_textbox_frame = ctk.CTkFrame(
            license_frame,
            corner_radius=0,
        )
        license_textbox_frame.pack(side="top", fill="both", expand=True)

        fd = open(os.path.join("assets/라이센스.txt"), "r")
        license_str = "".join(fd.readlines())
        license_textbox = ctk.CTkTextbox(
            license_textbox_frame,
            corner_radius=0,
            fg_color="transparent",
            wrap="word",
        )
        license_textbox.insert("1.0", license_str + license_str)
        license_textbox.configure(state="disabled")
        license_textbox.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        terms_of_service_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent",
        )
        terms_of_service_frame.pack(side="top", fill="x", pady=5)

        terms_of_service_label_font = ctk.CTkFont(
            family="Arial",
            size=14,
            weight="bold",
        )
        terms_of_service_label = ctk.CTkLabel(
            terms_of_service_frame,
            text="📝 이용약관",
            anchor="w",
            font=terms_of_service_label_font,
        )
        terms_of_service_label.pack(side="top", padx=5, fill="x")

        terms_of_service_textbox_frame = ctk.CTkFrame(
            terms_of_service_frame,
            corner_radius=0,
        )
        terms_of_service_textbox_frame.pack(side="top", fill="both", expand=True)

        fd = open(os.path.join("assets/이용약관.txt"), "r")
        terms_of_service_str = "".join(fd.readlines())
        terms_of_service_textbox = ctk.CTkTextbox(
            terms_of_service_textbox_frame,
            corner_radius=0,
            fg_color="transparent",
            wrap="word",
        )
        terms_of_service_textbox.insert(
            "1.0", terms_of_service_str + terms_of_service_str
        )
        terms_of_service_textbox.configure(state="disabled")
        terms_of_service_textbox.pack(
            side="top", fill="both", expand=True, padx=5, pady=5
        )
