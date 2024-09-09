import customtkinter as ctk

ctk.set_appearance_mode("light")
app = ctk.CTk()
app.geometry("800x600")
app.resizable(False, False)
app.title("대출반납 관리 시스템")


side_menu = ctk.CTkFrame(
    app,
)
side_menu.pack(side="left", fill="y")

home_btn = ctk.CTkButton(
    side_menu,
    text="Home",
    width=100,
    height=50,
)
home_btn.grid(row=0, column=0, padx=10, pady=5)

about_btn = ctk.CTkButton(
    side_menu,
    text="About",
    width=100,
    height=50,
)
about_btn.grid(row=1, column=0, padx=10, pady=5)

if __name__ == "__main__":
    app.mainloop()
