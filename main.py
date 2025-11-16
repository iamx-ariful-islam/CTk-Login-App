import customtkinter


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


root = customtkinter.CTk()
root.geometry("500x350")
root.title("CustomTkinter Login Page")


def login():
    print("Test")


frame    = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label    = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
entry1   = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry2   = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
button   = customtkinter.CTkButton(master=frame, text="Login", command=login)
checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")

label.pack(pady=12, padx=10)
entry1.pack(pady=12, padx=10)
entry2.pack(pady=12, padx=10)
button.pack(pady=12, padx=10)
checkbox.pack(pady=12, padx=10)


root.mainloop()