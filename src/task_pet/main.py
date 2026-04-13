import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Task Pet")
app.geometry("500x400")

title = ctk.CTkLabel(
    app,
    text="🐾 Task Pet",
    font=("Arial", 28, "bold")
)
title.pack(pady=30)

status = ctk.CTkLabel(
    app,
    text="Your pet is waiting for tasks...",
    font=("Arial", 16)
)
status.pack(pady=10)

feed_button = ctk.CTkButton(
    app,
    text="Feed Pet",
    command=lambda: status.configure(text="Your pet is happy! 🍖")
)
feed_button.pack(pady=20)

app.mainloop()