import customtkinter as ctk
import widgets
from utils import Utils, I18n


class Page(ctk.CTkFrame):
    def _toggle_license(self):
        visibility = False

        def toggle():
            nonlocal visibility
            nonlocal self
            if visibility:
                self.license_textbox.pack_forget()
                self.license_button.set_text_key("view_detail_open")
                visibility = False
            else:
                after = self.license_frame
                self.license_textbox.pack(fill="both", after=after, pady=5)
                self.license_button.set_text_key("view_detail_close")
                visibility = True

        return toggle

    def _toggle_terms_of_service(self):
        visuability = False

        def toggle():
            nonlocal visuability
            nonlocal self

            if visuability:
                self.terms_of_service_textbox.pack_forget()
                self.terms_of_service_button.set_text_key("view_detail_open")
                visuability = False
            else:
                after = self.terms_of_service_frame
                self.terms_of_service_textbox.pack(fill="both", after=after, pady=5)
                self.terms_of_service_button.set_text_key("view_detail_close")
                visuability = True

        return toggle

    def _toggle_privacy_policy(self):
        visuability = False

        def toggle():
            nonlocal visuability
            nonlocal self

            if visuability:
                self.privacy_policy_textbox.pack_forget()
                self.privacy_policy_button.set_text_key("view_detail_open")
                visuability = False
            else:
                after = self.privacy_policy_frame
                self.privacy_policy_textbox.pack(fill="both", after=after, pady=5)
                self.privacy_policy_button.set_text_key("view_detail_close")
                visuability = True

        return toggle

    def __init__(
        self,
        master,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | tuple[str, str] = "transparent",
        fg_color: str | tuple[str, str] | None = "transparent",
        border_color: str | tuple[str, str] | None = None,
        background_corner_colors: tuple[str | tuple[str, str]] | None = None,
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
        theme_mode_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        theme_mode_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            theme_mode_frame,
            text="🌓 화면 모드",
            text_key="settings_page_theme_mode",
            font=("Arial", 14),
            anchor="w",
            width=170,
        ).pack(side="left", fill="x", expand=True, padx=2)

        widgets.SelectButtons(
            theme_mode_frame,
            width=240,
            options={
                "settings_page_theme_mode_light": "light",
                "settings_page_theme_mode_dark": "dark",
                "settings_page_theme_mode_system": "system",
            },
            command=ctk.set_appearance_mode,
            dynamic_resizing=False,
            border_width=0,
            default_option_key="settings_page_theme_mode_system",
        ).pack(side="left")

        # ---------------------------------------------------------------
        theme_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        theme_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            theme_frame,
            text_key="settings_page_theme_color",
            font=("Arial", 14),
            anchor="w",
            width=170,
        ).pack(side="left", fill="x", expand=True, padx=2)

        theme_buttons = widgets.SelectButtons(
            theme_frame,
            width=240,
            options={
                "settings_page_theme_color_blue": "blue",
                "settings_page_theme_color_green": "green",
            },
            command=lambda _: theme_buttons.set(
                I18n.get_text("settings_page_theme_color_green")
            ),
            dynamic_resizing=False,
            border_width=0,
            default_option_key="settings_page_theme_color_green",
        )
        theme_buttons.pack(side="left")

        # ---------------------------------------------------------------
        language_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        language_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            language_frame,
            text="🌐 언어 설정",
            text_key="settings_page_language",
            font=("Arial", 14),
            anchor="w",
            width=170,
        ).pack(side="left", fill="x", expand=True, padx=2)

        widgets.SelectButtons(
            language_frame,
            width=240,
            options={
                "settings_page_language_korean": "ko",
                "settings_page_language_english": "en",
            },
            command=I18n.set_language,
            dynamic_resizing=False,
            border_width=0,
            default_option_key="settings_page_language_korean",
        ).pack(side="left")

    def _init_section2(self, root_frame: ctk.CTkFrame):
        section_div = widgets.Div.create(root_frame, side="top", my=5, px=10, py=5)

        # ---------------------------------------------------------------
        self.license_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        self.license_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            self.license_frame,
            text="📜 오픈소스 라이센스",
            text_key="settings_page_open_source",
            font=("Arial", 14),
            width=170,
            anchor="w",
        ).pack(side="left", padx=2)

        self.license_button = widgets.Button(
            self.license_frame,
            text="전문 보기 ◀︎",
            text_key="view_detail_open",
            width=240,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            command=self._toggle_license(),
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

        widgets.Label(
            self.terms_of_service_frame,
            text="📝 이용약관",
            text_key="settings_page_terms_of_service",
            anchor="w",
            font=("Arial", 14),
            width=170,
        ).pack(side="left", padx=2)

        self.terms_of_service_button = widgets.Button(
            self.terms_of_service_frame,
            text="전문 보기 ◀︎",
            text_key="view_detail_open",
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            command=self._toggle_terms_of_service(),
        )
        self.terms_of_service_button.pack(side="left", fill="x", expand=True)

        self.terms_of_service_textbox = widgets.TextArea(
            section_div,
            wrap="word",
            default_text=Utils.readlines("assets", "이용약관.txt"),
            state="disabled",
        )

        # ---------------------------------------------------------------
        self.privacy_policy_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        self.privacy_policy_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            self.privacy_policy_frame,
            text="🔒 개인정보 처리방침",
            text_key="settings_page_privacy_policy",
            font=("Arial", 14),
            width=170,
            anchor="w",
        ).pack(side="left", padx=2)

        self.privacy_policy_button = widgets.Button(
            self.privacy_policy_frame,
            text="전문 보기 ◀︎",
            text_key="view_detail_open",
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            command=self._toggle_privacy_policy(),
        )
        self.privacy_policy_button.pack(side="left", fill="x", expand=True)

        self.privacy_policy_textbox = widgets.TextArea(
            section_div,
            wrap="word",
            default_text=Utils.readlines("assets", "개인정보처리방침.txt"),
            state="disabled",
        )

    def _init_section3(self, root_frame: ctk.CTkFrame):
        section_div = widgets.Div.create(root_frame, side="top", my=5, px=10, py=5)

        # ---------------------------------------------------------------
        self.update_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        self.update_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            self.update_frame,
            text="🔄 업데이트",
            text_key="settings_page_update",
            font=("Arial", 14),
            width=170,
            anchor="w",
        ).pack(side="left", padx=2)

        widgets.Button(
            self.update_frame,
            text="업데이트 확인",
            text_key="settings_page_update_check",
            width=240,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            # command=Utils.update,
        ).pack(side="left", fill="x", expand=True)

        # ---------------------------------------------------------------
        self.backup_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        self.backup_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            self.backup_frame,
            text="💾 백업",
            text_key="settings_page_backup",
            font=("Arial", 14),
            width=170,
            anchor="w",
        ).pack(side="left", padx=2)

        widgets.Button(
            self.backup_frame,
            text="백업 파일 생성",
            text_key="settings_page_backup_create",
            width=240,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            # command=Utils.backup,
        ).pack(side="left", fill="x", expand=True)

        # ---------------------------------------------------------------
        self.restore_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        self.restore_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            self.restore_frame,
            text="🔄 복원",
            text_key="settings_page_restore",
            font=("Arial", 14),
            width=170,
            anchor="w",
        ).pack(side="left", padx=2)

        widgets.Button(
            self.restore_frame,
            text="백업 파일 복원",
            text_key="settings_page_restore_do",
            width=240,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            # command=Utils.restore,
        ).pack(side="left", fill="x", expand=True)

        # ---------------------------------------------------------------
        self.init_language_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        self.init_language_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            self.init_language_frame,
            text_key="settings_page_init_language",
            font=("Arial", 14),
            width=170,
            anchor="w",
        ).pack(side="left", padx=2)

        def reload_language():
            I18n.init()

        widgets.Button(
            self.init_language_frame,
            text_key="settings_page_init_language_do",
            width=240,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            command=reload_language,
        ).pack(side="left", fill="x", expand=True)

        # ---------------------------------------------------------------
        self.reset_frame = ctk.CTkFrame(section_div, fg_color="transparent")
        self.reset_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            self.reset_frame,
            text="🔨 초기화",
            text_key="settings_page_factory_reset",
            font=("Arial", 14),
            width=170,
            anchor="w",
        ).pack(side="left", padx=2)

        widgets.Button(
            self.reset_frame,
            text="모든 데이터 초기화",
            text_key="settings_page_factory_reset_all_data",
            width=240,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            # command=Utils.reset,
        ).pack(side="left", fill="x", expand=True)
