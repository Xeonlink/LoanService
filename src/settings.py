import customtkinter as ctk
from SideMenu import SideMenu
import os


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")
app = ctk.CTk()
app.geometry("800x600")
# app.resizable(False, False)
app.title("대출반납 관리 시스템")

side_menu = SideMenu(app)
side_menu.pack(side="left", fill="y")

page_frame = ctk.CTkFrame(
    app,
    corner_radius=0,
    fg_color="transparent",
)
page_frame.pack(side="left", fill="both", expand=True, padx=180, pady=10)

theme_frame = ctk.CTkFrame(
    page_frame,
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
    # fg_color="gray10",
    # anchor="e",
    font=theme_label_font,
    anchor="w",
)
theme_label.pack(side="top", fill="x", expand=True, padx=5)

theme_segmentedbutton = ctk.CTkSegmentedButton(
    theme_frame,
    corner_radius=0,
    # fg_color=("#979DA2", "#565B5E"),
    values=["system", "light", "dark"],
)
theme_segmentedbutton.pack(side="top", fill="x", expand=True)
theme_segmentedbutton.set("system")

theme_sublabel = ctk.CTkLabel(
    theme_frame,
    text="변경할 테마를 선택할 수 있습니다.",
    # fg_color="transpa",
    anchor="w",
)
theme_sublabel.pack(side="top", fill="x", expand=True, padx=5)

license_frame = ctk.CTkFrame(
    page_frame,
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
    # fg_color="transparent",
    anchor="w",
    font=license_label_font,
)
license_label.pack(side="top", padx=5, fill="x")

license_textbox_frame = ctk.CTkFrame(
    license_frame,
    corner_radius=0,
    # fg_color="green",
)
license_textbox_frame.pack(side="top", fill="both", expand=True)

fd = open(os.path.join("assets/라이센스.txt"), "r")
license_str = "".join(fd.readlines())
license_textbox = ctk.CTkTextbox(
    license_textbox_frame,
    # width=100,
    # height=300,
    corner_radius=0,
    fg_color="transparent",
    # state="disabled",
    wrap="word",
)
license_textbox.insert("1.0", license_str + license_str)
license_textbox.configure(state="disabled")
license_textbox.pack(side="top", fill="both", expand=True, padx=5, pady=5)
# license_textbox.configure(state="disabled")

terms_of_service_frame = ctk.CTkFrame(
    page_frame,
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
    # fg_color="transparent",
    anchor="w",
    font=terms_of_service_label_font,
)
terms_of_service_label.pack(side="top", padx=5, fill="x")

terms_of_service_textbox_frame = ctk.CTkFrame(
    terms_of_service_frame,
    corner_radius=0,
    # fg_color="green",
)
terms_of_service_textbox_frame.pack(side="top", fill="both", expand=True)

fd = open(os.path.join("assets/이용약관.txt"), "r")
terms_of_service_str = "".join(fd.readlines())
terms_of_service_textbox = ctk.CTkTextbox(
    terms_of_service_textbox_frame,
    # width=100,
    # height=300,
    corner_radius=0,
    fg_color="transparent",
    # state="disabled",
    wrap="word",
)
terms_of_service_textbox.insert("1.0", terms_of_service_str + terms_of_service_str)
terms_of_service_textbox.configure(state="disabled")
terms_of_service_textbox.pack(side="top", fill="both", expand=True, padx=5, pady=5)
# license_textbox.configure(state="disabled")


if __name__ == "__main__":
    app.mainloop()
