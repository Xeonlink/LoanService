from utils.I18n import I18n
from tkinter.filedialog import askdirectory
from shutil import copyfile
from constants import (
    DB_PATH,
    BACKUP_FILE_NAME_SQLITE,
    BACKUP_FILE_NAME_EXCEL,
    LICENSE_PATH,
    TERMS_OF_SERVICE_PATH,
    PRIVACY_POLICY_PATH,
    DEBUG,
)
import customtkinter as ctk
import widgets
import utils
import os


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
        if DEBUG:
            self._debug_section(root_frame)

        copyright_label = widgets.Label(
            root_frame,
            text="© 2021-2022, All rights reserved.",
            font=("Arial", 12),
            text_color="gray",
            fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
            anchor="center",
        )
        copyright_label.pack(side="top", fill="x", expand=True, pady=5)

    def _init_section1(self, root_frame: ctk.CTkFrame):
        section_frame = widgets.Frame(root_frame).pack(
            fill="x", expand=True, pady=5, ipadx=10, ipady=5
        )

        # ---------------------------------------------------------------
        theme_mode_frame = ctk.CTkFrame(section_frame, fg_color="transparent")
        theme_mode_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            theme_mode_frame,
            text="🌓 화면 모드",
            text_key="settings_page_theme_mode",
            font=("Arial", 14),
            anchor="w",
            width=170,
        ).pack(side="left", fill="x", expand=True, padx=2)

        appearance_mode_options = {
            "settings_page_theme_mode_light": "light",
            "settings_page_theme_mode_dark": "dark",
            "settings_page_theme_mode_system": "system",
        }
        widgets.SelectButtons(
            theme_mode_frame,
            width=240,
            options=appearance_mode_options,
            command=ctk.set_appearance_mode,
            dynamic_resizing=False,
            border_width=0,
            default_option_key=utils.swapkv(appearance_mode_options).get(
                ctk.get_appearance_mode().lower(),
                "settings_page_theme_mode_system",
            ),
        ).pack(side="left")

        # ---------------------------------------------------------------
        theme_frame = ctk.CTkFrame(section_frame, fg_color="transparent")
        theme_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            theme_frame,
            text_key="settings_page_theme_color",
            font=("Arial", 14),
            anchor="w",
            width=170,
        ).pack(side="left", fill="x", expand=True, padx=2)

        self.theme_buttons = widgets.SelectButtons(
            theme_frame,
            width=240,
            options={
                "settings_page_theme_color_blue": "blue",
                "settings_page_theme_color_green": "green",
            },
            command=lambda _: self.theme_buttons.set(
                I18n.get_text("settings_page_theme_color_green")
            ),
            dynamic_resizing=False,
            border_width=0,
            default_option_key="settings_page_theme_color_green",
        )
        self.theme_buttons.pack(side="left")

        # ---------------------------------------------------------------
        language_frame = ctk.CTkFrame(section_frame, fg_color="transparent")
        language_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            language_frame,
            text="🌐 언어 설정",
            text_key="settings_page_language",
            font=("Arial", 14),
            anchor="w",
            width=170,
        ).pack(side="left", fill="x", expand=True, padx=2)

        language_options = {
            "settings_page_language_korean": "ko",
            "settings_page_language_english": "en",
        }
        widgets.SelectButtons(
            language_frame,
            width=240,
            options=language_options,
            command=I18n.set_language,
            dynamic_resizing=False,
            border_width=0,
            default_option_key=utils.swapkv(language_options).get(
                I18n.lang,
                "settings_page_language_korean",
            ),
        ).pack(side="left")

    def _init_section2(self, root_frame: ctk.CTkFrame):
        section_frame = widgets.Frame(root_frame).pack(
            fill="x", expand=True, pady=5, ipadx=10, ipady=5
        )

        # ---------------------------------------------------------------
        self.license_frame = ctk.CTkFrame(section_frame, fg_color="transparent")
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
            section_frame,
            wrap="word",
            default_text=utils.readall(LICENSE_PATH),
            state="disabled",
        )

        # ---------------------------------------------------------------
        self.terms_of_service_frame = ctk.CTkFrame(
            section_frame, fg_color="transparent"
        )
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
            section_frame,
            wrap="word",
            default_text=utils.readall(TERMS_OF_SERVICE_PATH),
            state="disabled",
        )

        # ---------------------------------------------------------------
        self.privacy_policy_frame = ctk.CTkFrame(section_frame, fg_color="transparent")
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
            section_frame,
            wrap="word",
            default_text=utils.readall(PRIVACY_POLICY_PATH),
            state="disabled",
        )

    def _init_section3(self, root_frame: ctk.CTkFrame):
        section_frame = widgets.Frame(root_frame).pack(
            fill="x", expand=True, pady=5, ipadx=10, ipady=5
        )

        # ---------------------------------------------------------------
        self.warning_test_frame = ctk.CTkFrame(section_frame, fg_color="transparent")
        self.warning_test_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            self.warning_test_frame,
            text_key="settings_page_update",
            font=("Arial", 14),
            width=170,
            anchor="w",
        ).pack(side="left", padx=2)

        widgets.Button(
            self.warning_test_frame,
            text_key="settings_page_update_check",
            width=240,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            # command=Utils.update,
        ).pack(side="left", fill="x", expand=True)

        # ---------------------------------------------------------------
        self.backup_frame = ctk.CTkFrame(section_frame, fg_color="transparent")
        self.backup_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            self.backup_frame,
            text_key="settings_page_backup",
            font=("Arial", 14),
            width=170,
            anchor="w",
        ).pack(side="left", padx=2)

        def backup_sqlite():
            des = os.path.join(askdirectory(), BACKUP_FILE_NAME_SQLITE)
            copyfile(DB_PATH, des)

        widgets.Button(
            self.backup_frame,
            text_key="settings_page_backup_sqlite",
            width=120,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            command=backup_sqlite,
        ).pack(side="left")

        ctk.CTkFrame(self.backup_frame, width=10, height=10).pack(side="left")

        def backup_excel():
            des = os.path.join(askdirectory(), BACKUP_FILE_NAME_EXCEL)
            utils.sqlite2excel(DB_PATH, des)

        widgets.Button(
            self.backup_frame,
            text_key="settings_page_backup_excel",
            width=120,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            command=backup_excel,
        ).pack(side="left")

        # ---------------------------------------------------------------
        self.restore_frame = ctk.CTkFrame(section_frame, fg_color="transparent")
        self.restore_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            self.restore_frame,
            text_key="settings_page_restore",
            font=("Arial", 14),
            width=170,
            anchor="w",
        ).pack(side="left", padx=2)

        widgets.Button(
            self.restore_frame,
            text_key="settings_page_restore_do",
            width=240,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            # command=Utils.restore,
        ).pack(side="left", fill="x", expand=True)

        # ---------------------------------------------------------------
        self.init_language_frame = ctk.CTkFrame(section_frame, fg_color="transparent")
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
        self.reset_frame = ctk.CTkFrame(section_frame, fg_color="transparent")
        self.reset_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            self.reset_frame,
            text_key="settings_page_factory_reset",
            font=("Arial", 14),
            width=170,
            anchor="w",
        ).pack(side="left", padx=2)

        widgets.Button(
            self.reset_frame,
            text_key="settings_page_factory_reset_all_data",
            width=240,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            # command=Utils.reset,
        ).pack(side="left", fill="x", expand=True)

    def _debug_section(self, root_frame: ctk.CTkFrame):
        section_frame = widgets.Frame(root_frame).pack(
            fill="x", expand=True, pady=5, ipadx=10, ipady=5
        )

        # ---------------------------------------------------------------
        self.warning_test_frame = ctk.CTkFrame(section_frame, fg_color="transparent")
        self.warning_test_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            self.warning_test_frame,
            text="⚠️ 경고 테스트",
            font=("Arial", 14),
            width=170,
            anchor="w",
        ).pack(side="left", padx=2)

        def show_warning():
            widgets.Warning(message="경고 메시지 내용입니다.")

        widgets.Button(
            self.warning_test_frame,
            text="경고 메시지",
            width=240,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            command=show_warning,
        ).pack(side="left", fill="x", expand=True)

        # ---------------------------------------------------------------
        self.alert_test_frame = ctk.CTkFrame(section_frame, fg_color="transparent")
        self.alert_test_frame.pack(side="top", fill="x", pady=5)

        widgets.Label(
            self.alert_test_frame,
            text="🔔 알림 테스트",
            font=("Arial", 14),
            width=170,
            anchor="w",
        ).pack(side="left", padx=2)

        def show_alert():
            widgets.Alert(message="대출불가.\n연체된 도서가 있어 대출할 수 없습니다.")

        widgets.Button(
            self.alert_test_frame,
            text="알림 메시지",
            width=240,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkTextbox"]["fg_color"],
            command=show_alert,
        ).pack(side="left", fill="x", expand=True)
