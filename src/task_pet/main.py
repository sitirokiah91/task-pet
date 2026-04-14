import customtkinter as ctk

tasks = []
selected_minutes = 5
time_left = 0

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Task Pet Plant")
app.geometry("500x650")


def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        task_entry.delete(0, "end")
        refresh_task_list()
        update_start_button()


def refresh_task_list():
    if tasks:
        task_list_label.configure(
            text="\n".join([f"☐ {task}" for task in tasks])
        )
    else:
        task_list_label.configure(text="No tasks yet.")


def set_timer(minutes):
    global selected_minutes
    selected_minutes = minutes
    timer_label.configure(text=f"Selected timer: {selected_minutes} minutes")

def click_button():
    global time_left
    time_left = selected_minutes * 60
    status.configure(text="Round in progress...")
    countdown()

def countdown():
    global time_left

    minutes = time_left // 60
    seconds = time_left % 60

    timer_label.configure(
        text=f"Time left: {minutes:02}:{seconds:02}"
    )

    if time_left > 0:
        time_left -= 1
        app.after(1000, countdown)
    else:
        status.configure(
            text="Time is up! Plant returns to seed 🌰"
        )

def update_start_button():
    if tasks:
        start_button.configure(state="normal")
    else:
        start_button.configure(state="disabled")

title = ctk.CTkLabel(
    app,
    text="🐾 Task Pet Plant",
    font=("Arial", 28, "bold")
)
title.pack(pady=30)

status = ctk.CTkLabel(
    app,
    text="Your pet plant is waiting for tasks...",
    font=("Arial", 16)
)
status.pack(pady=10)

task_entry = ctk.CTkEntry(
    app,
    width=300,
    placeholder_text="Enter a task"
)
task_entry.pack(pady=10)

add_task_button = ctk.CTkButton(
    app,
    text="Add Task",
    command=add_task
)
add_task_button.pack(pady=10)

task_list_label = ctk.CTkLabel(
    app,
    text="No tasks yet.",
    font=("Arial", 14),
    justify="left"
)
task_list_label.pack(pady=20)

timer_label = ctk.CTkLabel(
    app,
    text=f"Selected timer: {selected_minutes} minutes",
    font=("Arial", 14)
)
timer_label.pack(pady=10)

timer_5_button = ctk.CTkButton(
    app,
    text="5 Mins",
    command=lambda: set_timer(5)
)
timer_5_button.pack(pady=5)

timer_10_button = ctk.CTkButton(
    app,
    text="10 Mins",
    command=lambda: set_timer(10)
)
timer_10_button.pack(pady=5)

timer_25_button = ctk.CTkButton(
    app,
    text="25 Mins",
    command=lambda: set_timer(25)
)
timer_25_button.pack(pady=5)

start_button = ctk.CTkButton(
    app,
    text="Start Round",
    command=click_button,
    state="disabled"
)
start_button.pack(pady=15)

app.mainloop()