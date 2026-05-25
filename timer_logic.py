from random import choice


def calculate_points(
    selected_duration
):
    if selected_duration == 25:
        return 5

    elif selected_duration == 45:
        return 14

    elif selected_duration == 60:
        return 19

    return 0

def change_timer(
    choice,
    app,
    timer_id,
    timer_label,
    selected_timer_label
):
    is_running = False

    if timer_id:
        app.after_cancel(
            timer_id
        )

    TESTING_MODE = True
    if TESTING_MODE:
        time_left = 10

    else:
        if choice == "25 min":
            time_left = 1500

        elif choice == "45 min":
            time_left = 2700

        elif choice == "60 min":
            time_left = 3600

    timer_label.configure(
        text=choice.replace(
            " min",
            ":00"
        )
    )

    selected_timer_label.configure(
        text=f"Selected Timer: {choice}"
    )

    selected_duration = int(
        choice.replace(
            " min",
            ""
        )
    )

    return (
        time_left,
        selected_duration,
        is_running
    )

# def pause_timer():
#     global is_running, timer_id

#     is_running = False
#     status_label.configure(text="Status: paused")
#     start_button.configure(state="normal")
#     pause_button.configure(state="disabled")
#     # timer_option.configure(state="normal") #re-enables dropdown when timer is paused

#     if timer_id:
#         app.after_cancel(timer_id)

def pause_timer(
    timer_id,
    app,
    status_label,
    start_button,
    pause_button
):
    is_running = False

    status_label.configure(
        text="Status: paused"
    )

    start_button.configure(
        state="normal"
    )

    pause_button.configure(
        state="disabled"
    )

    if timer_id:
        app.after_cancel(
            timer_id
        )

    return is_running

def reset_timer(
    timer_id,
    app,
    timer_option,
    timer_label,
    status_label,
    start_button,
    pause_button
):
    is_running = False

    status_label.configure(
        text="Status: Ready"
    )

    start_button.configure(
        state="normal"
    )

    pause_button.configure(
        state="disabled"
    )

    if timer_id:
        app.after_cancel(
            timer_id
        )

    selected_time = timer_option.get()

    TESTING_MODE = True
    if TESTING_MODE:
        time_left = 10

    else:
        if selected_time == "25 min":
            time_left = 1500
        elif selected_time == "45 min":
            time_left = 2700
        elif selected_time == "60 min":
            time_left = 3600

    if selected_time == "25 min":
        timer_label.configure(
            text="25:00"
        )
    elif selected_time == "45 min":
        timer_label.configure(
            text="45:00"
        )
    elif selected_time == "60 min":
        timer_label.configure(
            text="60:00"
        )

    timer_option.configure(
        state="normal"
    )

    return (
        time_left,
        is_running
    )

def countdown(
    app,
    time_left,
    timer_label,
    status_label,
    pause_button,
    start_button,
    timer_option,
    timer_finished_callback,
    session_complete_callback
):
    if time_left > 0:

        minutes = time_left // 60
        seconds = time_left % 60

        timer_label.configure(
            text=f"{minutes}:{seconds:02d}"
        )

        timer_id = app.after(
            1000,
            lambda: timer_finished_callback(
                time_left - 1
            )
        )

        return timer_id

    else:
        status_label.configure(
            text="Status: Complete"
        )

        pause_button.configure(
            state="disabled"
        )

        start_button.configure(
            state="normal"
        )

        timer_option.configure(
            state="normal"
        )

        session_complete_callback()

        return None
    
def start_timer_logic(
    selected_task,
    is_quick_focus,
    is_running,
    timer_option,
    status_label,
    start_button,
    pause_button,
    countdown_callback,
    current_task_label,
    selected_task_heading,
    messagebox
):
    if selected_task[0] is None and not is_quick_focus:

        answer = messagebox.askyesno(
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
            return (
                is_running,
                is_quick_focus
            )

    if is_running:
        return (
            is_running,
            is_quick_focus
        )

    is_running = True

    timer_option.configure(
        state="disabled"
    )

    status_label.configure(
        text="Status: Running"
    )

    start_button.configure(
        state="disabled"
    )

    pause_button.configure(
        state="normal"
    )

    countdown_callback()

    return (
        is_running,
        is_quick_focus
    )

def update_duration(
    choice,
    change_timer,
    app,
    timer_id,
    timer_label,
    selected_timer_label
):
    (
        time_left,
        selected_duration,
        is_running
    ) = change_timer(
        choice,
        app,
        timer_id,
        timer_label,
        selected_timer_label
    )

    return (
        time_left,
        selected_duration,
        is_running
    )