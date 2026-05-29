import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from auth_system import (
    save_user_tasks
)

def set_task(
        task_entry,
        task_listbox,
        tasks,
        task_data,
        save_data,
        current_user
):
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
        "achievements": [],
        "last_focus_date": None,
        "night_sessions": 0,
        "morning_sessions": 0,
        "daily_sessions": 0,
        "focus_sessions": 0,
        "session_streak": 0,
        "missed_day": False,
    }
    #print(task_data)

    task_listbox.insert( #shows task in UI
        tk.END, #add tasks at the bottom
        task_name
    )

    task_entry.delete(0, "end") #starts deleting from first character till end
    save_data(
        task_data
    ) #save new task to file

def select_task(
    event,
    task_listbox,
    current_task_label,
    selected_task_heading,
    update_task_stats,
    selected_task_ref
):
    selected_index = task_listbox.curselection() #which item user selected in the listbox

    if selected_index:
        selected_task = task_listbox.get(selected_index)
        selected_task_ref[0] = selected_task

        current_task_label.configure(
            text=f"Current Task: {selected_task}"
        )
        selected_task_heading.configure(
            text=selected_task
        )
        update_task_stats() #when task is selected, center instantly shows stats for that task

def delete_task(
    task_listbox,
    tasks,
    task_data,
    selected_task_ref,
    current_task_label,
    selected_task_heading,
    streak_label,
    points_label,
    focus_label,
    save_data,
    current_user
):
    selected_index = task_listbox.curselection() #which task user selected

    if not selected_index:
        messagebox.showwarning(
            "No Task Selected",
            "Please select a task to delete."
        )
        return

    task_name = task_listbox.get(selected_index)

    answer = messagebox.askyesno(
        "Delete Task",
        f"Delete '{task_name}'?\n\nThis action cannot be undone."
    )

    if answer:
        task_listbox.delete(selected_index)
        tasks.remove(task_name)
        selected_task_ref[0] = None

        current_task_label.configure(
            text="Current Task: None"
        )
        selected_task_heading.configure(
            text="No Task Selected"
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

        if task_name in task_data:
            task_data.pop(task_name) #removes task data from memory

        if current_user[0]:
            save_user_tasks(
                current_user[0],
                task_data
            )
        print(task_data)

#creating edit function
def edit_task(
    task_listbox,
    tasks,
    task_data,
    selected_task_ref,
    current_task_label,
    selected_task_heading,
    save_data,
    current_user
):
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

    selected_task_ref[0] = new_task

    current_task_label.configure(
        text=f"Current Task: {new_task}"
    )
    if current_user[0]:
        save_user_tasks(
            current_user[0],
            task_data
        )