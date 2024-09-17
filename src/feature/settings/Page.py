from typing import Tuple, Any
import customtkinter as ctk
import widgets
from utils import Utils, LangManager


class Page(ctk.CTkFrame):
    def _toggle_license(self):
        if self._is_license_textbox_visible:
            self.license_textbox.pack_forget()
            self.license_button.configure(text="전문 보기 ◀︎")
        else:
            self.license_textbox.pack(
                side="top",
                fill="both",
                expand=True,
                after=self.license_frame,
                pady=5,
            )
            self.license_button.configure(text="전문 닫기 ▼")
        self._is_license_textbox_visible = not self._is_license_textbox_visible

    def _toggle_terms_of_service(self):
        if self._is_terms_of_service_textbox_visible:
            self.terms_of_service_textbox.pack_forget()
            self.terms_of_service_button.configure(text="전문 보기 ◀︎")
        else:
            self.terms_of_service_textbox.pack(
                side="top",
                fill="both",
                expand=True,
                after=self.terms_of_service_frame,
                pady=5,
            )
            self.terms_of_service_button.configure(text="전문 닫기 ▼")
        self._is_terms_of_service_textbox_visible = (
            not self._is_terms_of_service_textbox_visible
        )

    def __init__(
        self,
        master: Any,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = "transparent",
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
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

        root_of_root_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        root_of_root_frame.pack(side="top", fill="both", expand=True)

        root_frame = ctk.CTkFrame(root_of_root_frame, fg_color="transparent")
        root_frame.pack(side="top", pady=5)

        self._init_section1(root_frame)
        self._init_section2(root_frame)
        self._init_section3(root_frame)

        copyright_label = ctk.CTkLabel(
            root_frame,
            text="© 2021-2022, All rights reserved.",
            font=("Arial", 12),
            text_color="gray",
            fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
            anchor="center",
        )
        copyright_label.pack(side="top", fill="x", expand=True, pady=5)

    def _init_section1(self, root_frame: ctk.CTkFrame):
        section_div = widgets.Div.create(root_frame, side="top", my=5, px=10, py=5)

        # ---------------------------------------------------------------
        appearance_mode_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        appearance_mode_frame.pack(side="top", fill="x", pady=5)

        ctk.CTkLabel(
            appearance_mode_frame,
            text="🖥️ 화면 모드",
            font=("Arial", 14),
            anchor="w",
            width=150,
        ).pack(side="left", fill="x", expand=True, padx=2)

        widgets.SelectButtons(
            appearance_mode_frame,
            width=250,
            options={
                "밝은": "light",
                "어두운": "dark",
                "적응하는": "system",
            },
            command=ctk.set_appearance_mode,
            dynamic_resizing=False,
            border_width=0,
            default_option="적응하는",
        ).pack(side="left")

        # ---------------------------------------------------------------
        theme_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        theme_frame.pack(side="top", fill="x", pady=5)

        ctk.CTkLabel(
            theme_frame,
            text="🎨 테마 설정",
            font=("Arial", 14),
            anchor="w",
            width=150,
        ).pack(side="left", fill="x", expand=True, padx=2)

        widgets.SelectButtons(
            theme_frame,
            width=250,
            options={
                "밝은": "light",
                "어두운": "dark",
                "적응하는": "system",
            },
            command=ctk.set_appearance_mode,
            dynamic_resizing=False,
            border_width=0,
            default_option="적응하는",
        ).pack(side="left")

        # ---------------------------------------------------------------
        language_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        language_frame.pack(side="top", fill="x", pady=5)

        language_label = ctk.CTkLabel(
            language_frame,
            text="🌐 언어 설정",
            font=("Arial", 14),
            anchor="w",
            width=150,
        )
        language_label.pack(side="left", fill="x", expand=True, padx=2)
        LangManager.subscribe(
            key="settings_language_label",
            callback=lambda value: language_label.configure(text=value),
        )

        widgets.SelectButtons(
            language_frame,
            width=250,
            options={
                "한국어": "ko",
                "English": "en",
            },
            command=LangManager.set_language,
            dynamic_resizing=False,
            border_width=0,
            default_option="한국어",
        ).pack(side="left")

    def _init_section2(self, root_frame: ctk.CTkFrame):
        section_div = widgets.Div.create(root_frame, side="top", my=5, px=10, py=5)

        # ---------------------------------------------------------------
        self.license_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        self.license_frame.pack(side="top", fill="x", pady=5)

        ctk.CTkLabel(
            self.license_frame,
            text="📜 오픈소스 라이센스",
            font=("Arial", 14),
            width=150,
            anchor="w",
        ).pack(side="left", padx=2)

        self._is_license_textbox_visible = False

        self.license_button = ctk.CTkButton(
            self.license_frame,
            text="전문 보기 ◀︎",
            width=250,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            command=self._toggle_license,
        )
        self.license_button.pack(side="left", fill="x", expand=True)

        self.license_textbox = widgets.TextArea(
            section_div,
            wrap="word",
            default_text=Utils.readlines("assets", "라이센스.txt"),
            state="disabled",
        )

        # ---------------------------------------------------------------
        self.terms_of_service_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        self.terms_of_service_frame.pack(side="top", fill="x", pady=5)

        ctk.CTkLabel(
            self.terms_of_service_frame,
            text="📝 이용약관",
            anchor="w",
            font=("Arial", 14),
            width=150,
        ).pack(side="left", padx=2)

        self._is_terms_of_service_textbox_visible = False

        self.terms_of_service_button = ctk.CTkButton(
            self.terms_of_service_frame,
            text="전문 보기 ◀︎",
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            command=self._toggle_terms_of_service,
        )
        self.terms_of_service_button.pack(side="left", fill="x", expand=True)

        self.terms_of_service_textbox = widgets.TextArea(
            section_div,
            wrap="word",
            default_text=Utils.readlines("assets", "이용약관.txt"),
            state="disabled",
        )

    def _init_section3(self, root_frame: ctk.CTkFrame):
        section_div = widgets.Div.create(root_frame, side="top", my=5, px=10, py=5)

        # ---------------------------------------------------------------
        self.backup_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        self.backup_frame.pack(side="top", fill="x", pady=5)

        ctk.CTkLabel(
            self.backup_frame,
            text="💾 백업",
            font=("Arial", 14),
            width=150,
            anchor="w",
        ).pack(side="left", padx=2)

        backup_btn = ctk.CTkButton(
            self.backup_frame,
            text="백업 파일 생성",
            width=250,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            # command=Utils.backup,
        )
        backup_btn.pack(side="left", fill="x", expand=True)

        # ---------------------------------------------------------------
        self.restore_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        self.restore_frame.pack(side="top", fill="x", pady=5)

        ctk.CTkLabel(
            self.restore_frame,
            text="🔄 복원",
            font=("Arial", 14),
            width=150,
            anchor="w",
        ).pack(side="left", padx=2)

        restore_btn = ctk.CTkButton(
            self.restore_frame,
            text="백업 파일 복원",
            width=250,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            # command=Utils.restore,
        )
        restore_btn.pack(side="left", fill="x", expand=True)

        # ---------------------------------------------------------------
        self.reset_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        self.reset_frame.pack(side="top", fill="x", pady=5)

        ctk.CTkLabel(
            self.reset_frame,
            text="🔨 초기화",
            font=("Arial", 14),
            width=150,
            anchor="w",
        ).pack(side="left", padx=2)

        reset_btn = ctk.CTkButton(
            self.reset_frame,
            text="모든 데이터 초기화",
            width=250,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            # command=Utils.reset,
        )
        reset_btn.pack(side="left", fill="x", expand=True)

        # ---------------------------------------------------------------
        self.update_frame = ctk.CTkFrame(
            section_div,
            fg_color="transparent",
        )
        self.update_frame.pack(side="top", fill="x", pady=5)

        ctk.CTkLabel(
            self.update_frame,
            text="🔄 업데이트",
            font=("Arial", 14),
            width=150,
            anchor="w",
        ).pack(side="left", padx=2)

        update_btn = ctk.CTkButton(
            self.update_frame,
            text="업데이트 확인",
            width=250,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            # command=Utils.update,
        )
        update_btn.pack(side="left", fill="x", expand=True)
