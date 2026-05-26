import customtkinter #bringing the cusomtkinter module to create the app
from tkinter import messagebox
import tkinter as tk
from tkinter import simpledialog
from datetime import date
from datetime import datetime
import json #to save/load data into file
from data_manager import (
    save_data,
    load_data
)
from task_manager import (
    set_task,
    select_task,
    edit_task,
    delete_task
)
from timer_logic import (
    calculate_points,
    change_timer,
    pause_timer,
    reset_timer,
    countdown,
    start_timer_logic,
    update_duration
)
from session_manager import (
    update_task_stats,
    finish_session
)
from plant_system import (
    load_plant_images,
    update_plant_growth
)
from achievement_system import (
    check_achievements
)
from notification_system import (
    show_notification
)
from badge_popup import (
    show_badge_popup
)
from badge_collection import (
    open_badges_page
)

# creating main application window
app = customtkinter.CTk()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# title of app
app.title("FocusVerse")

# window size
app.geometry("500x400")

left_frame = customtkinter.CTkFrame(
    app,
    width=300
)
left_frame.pack(
    side="left",
    fill="y", #stretches vertically to fill the left side of the window
    padx=10,
    pady=10
)
left_frame.pack_propagate(False)

center_frame = customtkinter.CTkFrame(app)
center_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(20,40),
    pady=10
)

#title of app
title_label = customtkinter.CTkLabel(
    center_frame,
    text="FocusVerse",
    font=("Arial", 28, "bold")
)
title_label.pack(pady=20)

#subtitle of app
subtitle_label = customtkinter.CTkLabel(
    center_frame,
    text="Build consistency through focus",
    font=("Arial", 14)
)
subtitle_label.pack()

branding_label = customtkinter.CTkLabel(
    left_frame,
    text="🌱 FocusVerse",
    font=("Arial", 24, "bold")
)
branding_label.pack(pady=(20, 5)) #top & bottom spacing

tagline_label = customtkinter.CTkLabel(
    left_frame,
    text="Grow Through Focus",
    font=("Arial", 12)
)
tagline_label.pack(pady=(0, 20))

task_section_label = customtkinter.CTkLabel(
    left_frame,
    text="TASKS",
    font=("Arial", 14, "bold")
)
task_section_label.pack(pady=(10, 5))

#to take the task input from user
task_entry = customtkinter.CTkEntry(
    left_frame,
    placeholder_text="Add a focus task...",
    width=240,
    height=38
)
task_entry.pack(pady=10)

#add task button
set_task_button = customtkinter.CTkButton(
    left_frame,
    text="Add Task",
    width=240,
    height=38,
    command=lambda: set_task( #lambda means when the user clicks button, do something
        task_entry,
        task_listbox,
        tasks,
        task_data,
        save_data
    )
)
set_task_button.pack(pady=5)

#delete task button
delete_task_button = customtkinter.CTkButton(
    left_frame,
    text="Delete Task",
    width=240,
    height=38,
    command=lambda: delete_task(
        task_listbox,
        tasks,
        task_data,
        selected_task,
        current_task_label,
        selected_task_heading,
        streak_label,
        points_label,
        focus_label,
        save_data
    )
)
delete_task_button.pack(pady=5)

#edit task button
edit_task_button = customtkinter.CTkButton(
    left_frame,
    text="Edit Task",
    width=240,
    height=38,
    command=lambda: edit_task(
        task_listbox,
        tasks,
        task_data,
        selected_task,
        current_task_label,
        selected_task_heading,
        save_data
    )
)
edit_task_button.pack(pady=5)

#we can use listbox instead of textbox (above code) to show tasks in a cleaner way
task_listbox = tk.Listbox(
    left_frame,
    width=35,
    height=8,
    font=("Arial", 13),
    bg="#1f1f1f",
    fg="white",
    justify="center",
    selectbackground="#2b6cb0",
    selectforeground="white",
    activestyle="none",
    bd=0,
    highlightthickness=0,
    selectborderwidth=2
)
task_listbox.pack(
    pady=10,
    padx=15,
    fill="x"
)
# task_listbox.config(
#     justify="center"
# )

current_task_label = customtkinter.CTkLabel(
    left_frame,
    text="Current Task: None",
    font=("Arial", 12)
)
current_task_label.pack(pady=5)

badges_button = customtkinter.CTkButton(
    left_frame,
    text="🏅 My Badges",
    width=250,
    height=40,
    command=lambda:
    open_badges_page(
        app,
        task_data
    )
)
badges_button.pack(
    pady=10
)

selected_task_heading = customtkinter.CTkLabel(
    center_frame,
    text="No Task Selected", #center shows this text when no task is selected
    font=("Arial", 22, "bold")
)
selected_task_heading.pack(
    pady=(10, 5)
)

#adding motivational quote in center
quote_label = customtkinter.CTkLabel(
    center_frame,
    text="🌱 What you plant now, you will harvest later",
    font=("Arial", 14),
    text_color="#A8C9A4"
)
quote_label.pack(pady=(5, 5))

#create plant section frame
plant_section = customtkinter.CTkFrame(
    center_frame,
    fg_color="transparent"
)
plant_section.pack(
    pady=(5,0)
)

plant_images = load_plant_images()

plant_label = customtkinter.CTkLabel(
    center_frame,
    text="",
    image=plant_images["seed"]
)
plant_label.pack(
    pady=10
)

#creates stats frame
stats_frame = customtkinter.CTkFrame(
    plant_section,
    width=260,
    corner_radius=20
)
stats_frame.pack(
    pady=(5,0),
    #adds internal breathing space
    ipadx=20,
    ipady=10
)

#adds streak, points and focus time labels in center
streak_label = customtkinter.CTkLabel(
    stats_frame,
    text="🔥 Streak: 0 days",
    font=("Arial", 14)
)
streak_label.pack(
    pady=(10,5),
    padx=10
)

points_label = customtkinter.CTkLabel(
    stats_frame,
    text="⭐ Points: 0",
    font=("Arial", 14)
)
points_label.pack(
    pady=5,
    padx=15
)

focus_label = customtkinter.CTkLabel(
    stats_frame,
    text="⏱ Focus Time: 0 mins",
    font=("Arial", 14)
)
focus_label.pack(
    pady=(5,10),
    padx=15
)

#creating timer card
timer_frame = customtkinter.CTkFrame(
    center_frame,
    width=460,
    height=340,
    corner_radius=25
)
timer_frame.pack(
    pady=(10,10)
)
timer_frame.pack_propagate(False)

def update_duration_ui(
    choice
):
    global time_left
    global selected_duration
    global is_running

    (
        time_left,
        selected_duration,
        is_running
    ) = update_duration(
        choice,
        change_timer,
        app,
        timer_id,
        timer_label,
        selected_timer_label
    )

timer_option = customtkinter.CTkOptionMenu(
    timer_frame,
    values=["25 min", "45 min", "60 min"],
    command = update_duration_ui
)
timer_option.pack(pady=10)

selected_timer_label = customtkinter.CTkLabel(
    timer_frame,
    text="Selected Timer: 25 min",
    font=("Arial", 12)
)
#to show whether the timer running,paused or reset
selected_timer_label.pack(pady=5)

status_label = customtkinter.CTkLabel(
    timer_frame,
    text="Status: Ready",
    font=("Arial", 12, "bold")
)
status_label.pack(pady=5)

timer_label = customtkinter.CTkLabel(
    timer_frame,
    text="25:00",
    font=("Arial", 50, "bold")
)
timer_label.pack(pady=(5,5))

time_left = 10 # 25 minutes in seconds
TESTING_MODE = True
is_running = False #checks whether timer is running or not
timer_id = None
tasks = [] #list to store tasks
selected_task = [None]
is_quick_focus = False
task_data = {} #task memory system
selected_duration = 25
shown_achievements = set()

task_listbox.bind(
    "<<ListboxSelect>>",
    lambda event: (
        select_task(
            event,
            task_listbox,
            current_task_label,
            selected_task_heading,
            lambda: update_task_stats(
                selected_task,
                task_data,
                streak_label,
                points_label,
                focus_label
            ),
            selected_task
        ),
        reset_timer_ui()
    )
)

def start_timer():
    global is_running
    global is_quick_focus

    (
        is_running,
        is_quick_focus
    ) = start_timer_logic(
        selected_task,
        is_quick_focus,
        is_running,
        timer_option,
        status_label,
        start_button,
        pause_button,
        lambda: countdown_ui(
            time_left
        ),
        current_task_label,
        selected_task_heading,
        messagebox
    )

def finish_session_ui():
    global is_quick_focus

    is_quick_focus = finish_session(
        selected_task,
        is_quick_focus,
        task_data,
        selected_duration,
        calculate_points,
        update_task_stats,
        streak_label,
        points_label,
        focus_label,
        save_data,
        messagebox
    )

    if selected_task[0]:
        task_data[
            selected_task[0]
        ][
            "daily_sessions"
        ] += 1

        task_data[
            selected_task[0]
        ][
            "focus_sessions"
        ] += 1

        task_data[
            selected_task[0]
        ][
            "session_streak"
        ] += 1

        current_hour = (
            datetime.now().hour
        )

        if current_hour >= 23:

            task_data[
                selected_task[0]
            ][
                "night_sessions"
            ] += 1

            show_notification(
                app,
                "🌙 Still Going Strong",
                (
                    "Late nights are tough.\n"
                    "Proud of you for showing up tonight 🌱"
                )
            )
        if current_hour <= 7:
            task_data[
            selected_task[0]
        ][
            "morning_sessions"
        ] += 1
        show_notification(
            app,
            "☀️ Early Momentum",
            (
                "Starting early is powerful.\n"
                "Proud of you for showing up ☀️"
            )
        )

        check_achievements(
            app,
            selected_duration,
            task_data[
                selected_task[0]
            ],
            show_notification,
            show_badge_popup
        )

def countdown_ui(
    updated_time
):
    global time_left
    global timer_id

    time_left = updated_time
    if TESTING_MODE:
        total_time = 10
    else:
        total_time = (
            selected_duration * 60
        )
    elapsed_time = (
        total_time - time_left
    )
    progress_percentage = (
        elapsed_time / total_time
    ) * 100
    update_plant_growth(
        plant_label,
        plant_images,
        progress_percentage
    )
    timer_id = countdown(
        app,
        time_left,
        timer_label,
        status_label,
        pause_button,
        start_button,
        timer_option,
        countdown_ui,
        finish_session_ui
    )

button_frame = customtkinter.CTkFrame(timer_frame)
button_frame.pack(pady=10)

# startbutton
start_button = customtkinter.CTkButton(
    button_frame,
    text="Start",
    command=start_timer,
    width=100
)
start_button.pack(side="left", padx=10)

def pause_timer_ui():
    global is_running

    is_running = pause_timer(
        timer_id,
        app,
        status_label,
        start_button,
        pause_button
    )

pause_button = customtkinter.CTkButton(
    button_frame,
    text="Pause",
    command=pause_timer_ui,
    state="disabled",
    width=100
)
pause_button.pack(side="left", padx=10)

def reset_timer_ui():
    global time_left
    global is_running

    (
        time_left,
        is_running
    ) = reset_timer(
        timer_id,
        app,
        timer_option,
        timer_label,
        status_label,
        start_button,
        pause_button
    )
    plant_label.configure(
        image=plant_images["seed"]
    )

reset_button = customtkinter.CTkButton(
    button_frame,
    text="Reset",
    command=reset_timer_ui,
    width=100
)
reset_button.pack(side="left", padx=10)

load_data(
    task_listbox,
    tasks,
    task_data
)

# to keep app running
app.mainloop()