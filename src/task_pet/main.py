import customtkinter as ctk


tasks = []
selected_minutes = 5
time_left = 0
countdown_job = None
round_active = False

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Task Pet Plant")
app.geometry("500x650")


def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append({
            "name": task,
            "done": False,
        })
        task_entry.delete(0, "end")
        refresh_task_list()
        update_start_button()


def refresh_task_list():
    for widget in task_frame.winfo_children():
        widget.destroy()

    for index, task in enumerate(tasks):
        row = ctk.CTkFrame(task_frame)
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
            command=lambda idx=index: complete_task(idx),
            state=state,
            width=100,
        )
        button.pack(side="right", padx=10)



def all_tasks_completed():
    return all(task["done"] for task in tasks)



def handle_round_success():
    global countdown_job, round_active

    if countdown_job is not None:
        app.after_cancel(countdown_job)
        countdown_job = None

    round_active = False
    status.configure(text="All tasks completed! Your plant grows 🌱")
    refresh_task_list()



def complete_task(index):
    if round_active and not tasks[index]["done"]:
        tasks[index]["done"] = True
        refresh_task_list()

        if all_tasks_completed():
            handle_round_success()



def set_timer(minutes):
    global selected_minutes
    selected_minutes = minutes
    timer_label.configure(text=f"Selected timer: {selected_minutes} minutes")



def click_button():
    global time_left, round_active

    round_active = True
    refresh_task_list()
    time_left = selected_minutes * 60
    status.configure(text="Round in progress...")
    countdown()



def countdown():
    global time_left, countdown_job, round_active

    minutes = time_left // 60
    seconds = time_left % 60

    timer_label.configure(text=f"Time left: {minutes:02}:{seconds:02}")

    if time_left > 0:
        time_left -= 1
        countdown_job = app.after(1000, countdown)
    else:
        countdown_job = None
        round_active = False
        status.configure(text="Time is up! Plant returns to seed 🌰")
        refresh_task_list()



def update_start_button():
    if tasks:
        start_button.configure(state="normal")
    else:
        start_button.configure(state="disabled")



def restart_round():
    global time_left, countdown_job, round_active

    round_active = False

    if countdown_job is not None:
        app.after_cancel(countdown_job)
        countdown_job = None

    for task in tasks:
        task["done"] = False

    time_left = selected_minutes * 60
    timer_label.configure(text=f"Selected timer: {selected_minutes} minutes")
    status.configure(text="Round reset. Ready to start again.")
    refresh_task_list()



title = ctk.CTkLabel(
    app,
    text="🐾 Task Pet Plant",
    font=("Arial", 28, "bold"),
)
title.pack(pady=30)

status = ctk.CTkLabel(
    app,
    text="Your pet plant is waiting for tasks...",
    font=("Arial", 16),
)
status.pack(pady=10)

task_entry = ctk.CTkEntry(
    app,
    width=300,
    placeholder_text="Enter a task",
)
task_entry.pack(pady=10)

add_task_button = ctk.CTkButton(
    app,
    text="Add Task",
    command=add_task,
)
add_task_button.pack(pady=10)

task_frame = ctk.CTkFrame(app)
task_frame.pack(pady=20, padx=20, fill="x")

timer_label = ctk.CTkLabel(
    app,
    text=f"Selected timer: {selected_minutes} minutes",
    font=("Arial", 14),
)
timer_label.pack(pady=10)

timer_5_button = ctk.CTkButton(
    app,
    text="5 Mins",
    command=lambda: set_timer(5),
)
timer_5_button.pack(pady=5)

timer_10_button = ctk.CTkButton(
    app,
    text="10 Mins",
    command=lambda: set_timer(10),
)
timer_10_button.pack(pady=5)

timer_25_button = ctk.CTkButton(
    app,
    text="25 Mins",
    command=lambda: set_timer(25),
)
timer_25_button.pack(pady=5)

start_button = ctk.CTkButton(
    app,
    text="Start Round",
    command=click_button,
    state="disabled",
)
start_button.pack(pady=15)

restart_button = ctk.CTkButton(
    app,
    text="Restart Round",
    command=restart_round,
)
restart_button.pack(pady=5)

app.mainloop()