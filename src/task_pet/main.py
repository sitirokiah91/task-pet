import customtkinter as ctk

import pet
import ui


tasks = []
selected_minutes = 5
time_left = 0
countdown_job = None
round_active = False
restart_available = False
wins = 0
plant_stage = "seed"
plant_emoji = "🌰"
plant_rarity = None

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Task Pet Plant")
app.geometry("500x650")


def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(pet.create_task(task))
        task_entry.delete(0, "end")
        render_task_list()
        update_action_buttons()


def render_task_list():
    ui.refresh_task_list(task_frame, tasks, round_active, complete_task)


def update_plant_growth():
    global wins, plant_stage, plant_emoji, plant_rarity

    wins += 1

    if wins == pet.SPROUT_AT:
        plant_stage = "sprout"
        plant_emoji = "🌱"
        plant_rarity = None
    elif wins == pet.GROWN_AT:
        plant_stage = "grown"
        plant_emoji = "🌿"
        plant_rarity = None
    elif wins == pet.FINAL_AT:
        plant_stage = "final"
        plant_emoji, plant_rarity = pet.get_final_plant()

    plant_label.configure(text=plant_emoji)


def handle_round_success():
    global countdown_job, round_active, restart_available

    if countdown_job is not None:
        app.after_cancel(countdown_job)
        countdown_job = None

    round_active = False
    restart_available = True
    update_plant_growth()
    status.configure(text=f"All tasks completed! Your plant grows into {plant_emoji}")
    render_task_list()
    update_action_buttons()


def complete_task(index):
    if round_active and pet.complete_task(tasks, index):
        render_task_list()

        if pet.all_tasks_completed(tasks):
            handle_round_success()


def set_timer(minutes):
    global selected_minutes
    selected_minutes = minutes
    timer_label.configure(text=f"Selected timer: {selected_minutes} minutes")


def click_button():
    global time_left, round_active, restart_available

    round_active = True
    restart_available = True
    render_task_list()
    update_action_buttons()
    time_left = selected_minutes * 60
    status.configure(text="Round in progress...")
    countdown()


def countdown():
    global time_left, countdown_job, round_active, restart_available

    minutes = time_left // 60
    seconds = time_left % 60

    timer_label.configure(text=f"Time left: {minutes:02}:{seconds:02}")

    if time_left > 0:
        time_left -= 1
        countdown_job = app.after(1000, countdown)
    else:
        countdown_job = None
        round_active = False
        restart_available = True
        status.configure(text="Time is up! Plant returns to seed 🌰")
        render_task_list()
        update_action_buttons()


def update_action_buttons():
    if tasks and not round_active:
        start_button.configure(state="normal")
    else:
        start_button.configure(state="disabled")

    if restart_available:
        restart_button.configure(state="normal")
    else:
        restart_button.configure(state="disabled")


def restart_round():
    global time_left, countdown_job, round_active, restart_available

    round_active = False
    restart_available = False

    if countdown_job is not None:
        app.after_cancel(countdown_job)
        countdown_job = None

    pet.reset_tasks(tasks)

    time_left = selected_minutes * 60
    timer_label.configure(text=f"Selected timer: {selected_minutes} minutes")
    status.configure(text=f"Round reset. {plant_emoji} is ready to keep growing.")
    render_task_list()
    update_action_buttons()


title = ctk.CTkLabel(
    app,
    text="🐾 Task Pet Plant",
    font=("Arial", 28, "bold"),
)
title.pack(pady=30)

plant_label = ctk.CTkLabel(
    app,
    text=plant_emoji,
    font=("Arial", 64),
)
plant_label.pack(pady=10)

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
    state="disabled",
)
restart_button.pack(pady=5)

update_action_buttons()

app.mainloop()
