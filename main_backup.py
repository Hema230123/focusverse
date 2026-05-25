import customtkinter #bringing the cusomtkinter module to create the app
from tkinter import messagebox
import tkinter as tk
from tkinter import simpledialog
from datetime import date
import json #to save/load data into file

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
    width=180
)
left_frame.pack(
    side="left",
    fill="y", #stretches vertically to fill the left side of the window
    padx=10,
    pady=10
)


center_frame = customtkinter.CTkFrame(app)
center_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=10,
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
    placeholder_text="Add a focus task..."
)
task_entry.pack(pady=10)

def set_task():
    task_name = task_entry.get() #gets whatever user types in the input box

    if task_name == "": #don't add empty tasks
        return
    
    if task_name in tasks: #prevent duplicate tasks
        messagebox.showwarning( #popup warning
            "Duplicate Task",
            "This task already exists!"
        )
        return

    tasks.append(task_name) #adds task to list of tasks
    task_data[task_name] = {
        "focus_minutes": 0,
        "sessions": 0,
        "points": 0,
        "streak": 0,
        "last_focus_date": None
    }
    #print(task_data)

    task_listbox.insert( #shows task in UI
        tk.END, #add tasks at the bottom
        task_name
    )

    task_entry.delete(0, "end") #starts deleting from first character till end
    save_data() #save new task to file

def select_task(event):
    global selected_task

    selected_index = task_listbox.curselection() #which item user selected in the listbox

    if selected_index:
        selected_task = task_listbox.get( #gets selected task text
            selected_index
        )

        current_task_label.configure(
            text=f"Current Task: {selected_task}"
        )
        selected_task_heading.configure( #updates heading automatically
            text=selected_task
        )
        update_task_stats() #when task is selected, center instantly shows stats for that task  
        update_plant_growth()

def delete_task():
    global selected_task

    selected_index = task_listbox.curselection() #which task user selected

    if not selected_index:
        messagebox.showwarning(
            "No Task Selected",
            "Please select a task to delete."
        )
        return
    task_name = task_listbox.get(
            selected_index
    )

    answer = messagebox.askyesno(
        "Delete Task",
        f"Delete '{task_name}'?\n\nThis action cannot be undone."
    )

    if answer:
        task_listbox.delete( #removes task from listbox UI
            selected_index
        )

        tasks.remove(task_name) #remove from memory list

        selected_task = None

        current_task_label.configure(
            text="Current Task: None"
        )
        selected_task_heading.configure(
            text="No Task Selected"
        )
        plant_label.configure(
            text="🌱 Seed"
        )
        streak_label.configure(
            text="🔥 Streak: 0 days"
        )
        points_label.configure(
            text="⭐ Points: 0"
        )
        focus_label.configure(
            text="⏱ Focus Time: 0 mins"
        )
        task_data.pop(task_name) #removes task data from memory
        save_data()

#creating edit function
def edit_task():
    global selected_task

    selected_index = task_listbox.curselection()

    if not selected_index:
        messagebox.showwarning(
            "No Task Selected",
            "Please select a task to edit."
        )
        return

    old_task = task_listbox.get(
        selected_index
    )

    new_task = simpledialog.askstring( #popup input box
        "Edit Task",
        "Enter new task name:",
        initialvalue=old_task #shows current task name in the input box
    )

    if not new_task:
        return

    if new_task in tasks:
        messagebox.showwarning(
            "Duplicate Task",
            "This task already exists!"
        )
        return

    task_listbox.delete(
        selected_index
    )

    task_listbox.insert(
        selected_index,
        new_task
    )

    tasks.remove(old_task)
    tasks.append(new_task)

    task_data[new_task] = task_data.pop( #moves old task data to new task name
        old_task
    )

    selected_task = new_task

    current_task_label.configure(
        text=f"Current Task: {new_task}"
    )
    save_data() #save changes to file

#add task button
set_task_button = customtkinter.CTkButton(
    left_frame,
    text="Add Task",
    command=set_task
)

set_task_button.pack(pady=5)

#delete task button
delete_task_button = customtkinter.CTkButton(
    left_frame,
    text="Delete Task",
    command=delete_task
)

delete_task_button.pack(pady=5)

#edit task button
edit_task_button = customtkinter.CTkButton(
    left_frame,
    text="Edit Task",
    command=edit_task
)

edit_task_button.pack(pady=5)

#textbox used to display list of tasks
# task_listbox = customtkinter.CTkTextbox(
#     left_frame,
#     width=250,
#     height=120
# )

# task_listbox.pack(pady=10)

#we can use listbox instead of textbox (above code) to show tasks in a cleaner way
task_listbox = tk.Listbox(
    left_frame,
    height=8,
    font=("Arial", 12),
    bg="#1f1f1f",
    fg="white",
    selectbackground="#2b6cb0",
    selectforeground="white",
    activestyle="none",
    bd=0,
    highlightthickness=0
)
task_listbox.pack(
    pady=10,
    fill="x"
)
task_listbox.bind( #listens for when user clicks on task in listbox
    "<<ListboxSelect>>",
    select_task
)

current_task_label = customtkinter.CTkLabel(
    left_frame,
    text="Current Task: None",
    font=("Arial", 12)
)
current_task_label.pack(pady=5)

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
    pady=(0, 10)
)

#creating plant area
plant_canvas = tk.Canvas(
    plant_section,
    width=260,
    height=260,
    bg="#2b2b2b",
    highlightthickness=0,
    bd=0
)
plant_canvas.pack(pady=(0,5))

def draw_base_plant_area():
    plant_canvas.delete("all")

    # soft circle background
    plant_canvas.create_oval(
        20, 10, 220, 210,
        fill="#DCE5B6",
        outline=""
    )

    # soil
    plant_canvas.create_oval(
        55, 135, 185, 175,
        fill="#7B4B1A",
        outline=""
    )

#add plant label in center
# plant_label = customtkinter.CTkLabel(
#     center_frame,
#     text="🌱 Seed",
#     font=("Arial", 28)
# )
# plant_label.pack(pady=10)

#creating plant canvas
plant_canvas = tk.Canvas(
    center_frame,
    width=240,
    height=220,
    bg="#2b2b2b",
    highlightthickness=0
)
plant_canvas.pack(pady=(0,5))

#creates stats frame
stats_frame = customtkinter.CTkFrame(
    plant_section,
    width=260,
    corner_radius=20
)
stats_frame.pack(
    pady=(10,15),
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

def change_timer(choice):
    global time_left, timer_id, is_running, selected_duration

    is_running = False #stops timer state

    if timer_id:
        app.after_cancel(timer_id) #kills old countdown

    if choice == "25 min":
        time_left = 1500

    elif choice == "45 min":
        time_left = 2700

    elif choice == "60 min":
        time_left = 3600

    minutes = time_left // 60
    timer_label.configure(text=f"{minutes}:00")

    selected_timer_label.configure(
        text=f"Selected Timer: {choice}"
    )

    selected_duration = int(
        choice.replace(" min", "")
    )

#creating timer card
timer_frame = customtkinter.CTkFrame(
    center_frame,
    width=420,
    height=320,
    corner_radius=25
)
timer_frame.pack(
    pady=(5,10)
)
timer_frame.pack_propagate(False)

timer_option = customtkinter.CTkOptionMenu(
    timer_frame,
    values=["25 min", "45 min", "60 min"],
    command = change_timer
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
timer_label.pack(pady=30)

time_left = 10 # 25 minutes in seconds
is_running = False #checks whether timer is running or not
timer_id = None
tasks = [] #list to store tasks
selected_task = None
is_quick_focus = False
task_data = {} #task memory system
selected_duration = 25

def calculate_points():
    if selected_duration == 25: #1 point per 5mins
        return 5

    elif selected_duration == 45: #1.5 points per 5mins + 0.5 bonus point 
        return 14

    elif selected_duration == 60: #1.5 points per 5mins + 1 bonus point
        return 19

    return 0

# def update_plant_growth():
#     if not selected_task:
#         return

#     points = task_data[
#         selected_task
#     ]["points"]

#     if points <= 20:
#         plant_stage = "🌱 Seed"

#     elif points <= 50:
#         plant_stage = "🌿 Sprout"

#     elif points <= 100:
#         plant_stage = "🪴 Plant"

#     elif points <= 200:
#         plant_stage = "🌳 Tree"

#     else:
#         plant_stage = "🌸 Blooming Tree"

#     plant_label.configure(
#         text=plant_stage
#     )

def update_task_stats():
    if not selected_task:
        return

    task = task_data[selected_task]

    streak_label.configure(
        text=f"🔥 Streak: {task['streak']} days"
    )

    points_label.configure(
        text=f"⭐ Points: {task['points']}"
    )

    focus_label.configure(
        text=f"⏱ Focus Time: {task['focus_minutes']} mins"
    )

#creating load function
def load_data():
    global task_data, tasks

    try:
        with open(
            "focusverse_data.json",
            "r"
        ) as file:

            task_data = json.load(file)

            tasks = list(
                task_data.keys()
            )

            for task in tasks:
                if task_data[task][
                    "last_focus_date"
                ]:
                    task_data[task][
                        "last_focus_date"
                    ] = date.fromisoformat(
                        task_data[task][
                            "last_focus_date"
                        ]
                    )
                task_listbox.insert(
                    tk.END,
                    task
                )

    except FileNotFoundError:
        pass

def save_data():
    with open(
        "focusverse_data.json",
        "w"
    ) as file:

        json.dump(
            task_data,
            file,
            default=str
        )

def start_timer():
    global time_left, is_running, selected_task, is_quick_focus

    if selected_task is None and not is_quick_focus:
        answer = messagebox.askyesno( #popup with yes/no options
            "Quick Focus",
            "No task selected.\n\nStart a Quick Focus session?"
        )

        if answer:
            is_quick_focus = True
            current_task_label.configure(
                text="Current Task: Quick Focus ⚡"
            )
            selected_task_heading.configure(
                text="Quick Focus ⚡"
            )
        else:
            return

    if is_running:
        return

    is_running = True
    timer_option.configure( #locks timer choice during session
        state="disabled"
    )
    status_label.configure(text="Status: Running")
    start_button.configure(state="disabled")
    pause_button.configure(state="normal")
    timer_option.configure(state="disabled") #disables dropdown while timer is running

    countdown()

def countdown():
    global time_left, is_running, timer_id

    if not is_running:
        return

    if time_left > 0:
        minutes = time_left // 60
        seconds = time_left % 60

        timer_label.configure(
            text=f"{minutes}:{seconds:02}"
        )

        time_left -= 1

        timer_id = app.after(1000, countdown) #Save the scheduled timer_id so we can stop it later

    else:
        is_running = False

        if selected_task:
            earned_points = calculate_points()

            today = date.today()

            last_date = task_data[
                selected_task
            ]["last_focus_date"]

            if last_date is None:
                task_data[selected_task][
                    "streak"
                ] = 1

            elif (today - last_date).days == 1:
                task_data[selected_task][
                    "streak"
                ] += 1

            elif (today - last_date).days > 1:
                task_data[selected_task][
                    "streak"
                ] = 1

            task_data[selected_task][
                "last_focus_date"
            ] = today

            task_data[selected_task][
                "focus_minutes"
            ] += selected_duration

            task_data[selected_task][
                "sessions"
            ] += 1

            task_data[selected_task][
                "points"
            ] += earned_points

            update_task_stats()
            update_plant_growth()
            save_data() 

            # print(task_data)
        earned_points = calculate_points()
        streak = 0
        if selected_task:
            streak = task_data[
                selected_task
            ]["streak"]

        messagebox.showinfo(
            "🎉 Session Complete!",
            f"""
        Great Job! Focus Session Completed 🎉

        ⭐ +{earned_points} Points Earned
        🔥 Streak: {streak} days
        🌱 Plant Growing!

        Keep Going 🚀
        """
        )
        timer_option.configure( #when timer reaches 0, enables timer dropdown
            state="normal"
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

def pause_timer():
    global is_running, timer_id

    is_running = False
    status_label.configure(text="Status: paused")
    start_button.configure(state="normal")
    pause_button.configure(state="disabled")
    # timer_option.configure(state="normal") #re-enables dropdown when timer is paused

    if timer_id:
        app.after_cancel(timer_id)

pause_button = customtkinter.CTkButton(
    button_frame,
    text="Pause",
    command=pause_timer,
    state="disabled",
    width=100
)
pause_button.pack(side="left", padx=10)

def reset_timer():
    global time_left, is_running, timer_id

    is_running = False
    status_label.configure(text="Status: Ready")
    start_button.configure(state="normal")
    timer_option.configure(state="normal")
    pause_button.configure(state="disabled")

    if timer_id:
        app.after_cancel(timer_id)

    selected_time = timer_option.get() #gets current selected dropdown value

    if selected_time == "25 min":
        time_left = 1500

    elif selected_time == "45 min":
        time_left = 2700

    elif selected_time == "60 min":
        time_left = 3600

    minutes = time_left // 60
    timer_label.configure(text=f"{minutes}:00")

    timer_option.configure(
        state="normal"
    )

reset_button = customtkinter.CTkButton(
    button_frame,
    text="Reset",
    command=reset_timer,
    width=100
)

reset_button.pack(side="left", padx=10)

draw_base_plant_area(
    # plant_canvas.create_oval(
    #     40, 20, 240, 220,
    # )   
)

#load saved data when app starts
load_data()

# to keep app running
app.mainloop()