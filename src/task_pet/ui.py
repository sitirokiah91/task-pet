import customtkinter as ctk


def build_task_row(parent, task, index, round_active, on_complete):
    row = ctk.CTkFrame(parent)
    row.pack(fill="x", pady=5, padx=5)

    symbol = "✔" if task["done"] else "☐"

    label = ctk.CTkLabel(
        row,
        text=f"{symbol} {task['name']}",
    )
    label.pack(side="left", padx=10)

    if not round_active or task["done"]:
        state = "disabled"
    else:
        state = "normal"

    button = ctk.CTkButton(
        row,
        text="Complete",
        command=lambda idx=index: on_complete(idx),
        state=state,
        width=100,
    )
    button.pack(side="right", padx=10)


def refresh_task_list(task_frame, tasks, round_active, on_complete):
    for widget in task_frame.winfo_children():
        widget.destroy()

    for index, task in enumerate(tasks):
        build_task_row(task_frame, task, index, round_active, on_complete)
