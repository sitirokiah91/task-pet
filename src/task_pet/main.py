import customtkinter as ctk

tasks = []

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Task Pet")
app.geometry("500x400")


def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        task_entry.delete(0, "end")
        refresh_task_list()

def refresh_task_list():
    if tasks:
        task_list_label.configure(
            text="\n".join([f"☐ {task}" for task in tasks])
        )
    else:
        task_list_label.configure(text="No tasks yet.")

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

task_entry = ctk.CTkEntry(
    app,
    width=300,
    placeholder_text="Enter a task"
)
task_entry.pack(pady=10)

add_button = ctk.CTkButton(
    app,
    text="Add Task",
    command=add_task
)
add_button.pack(pady=10)

task_list_label = ctk.CTkLabel(
    app,
    text="No tasks yet.",
    font=("Arial", 14),
    justify="left"
)
task_list_label.pack(pady=20)

app.mainloop()