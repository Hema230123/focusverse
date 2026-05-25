from datetime import date

def update_task_stats(
    selected_task,
    task_data,
    streak_label,
    points_label,
    focus_label
):
    if selected_task[0] is None:
        return

    task = task_data[
        selected_task[0]
    ]

    streak_label.configure(
        text=f"🔥 Streak: {task['streak']} days"
    )

    points_label.configure(
        text=f"⭐ Points: {task['points']}"
    )

    focus_label.configure(
        text=f"⏱ Focus Time: {task['focus_minutes']} mins"
    )



def finish_session(
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
):
    messagebox.showinfo(
        "Focus Complete 🎉",
        "Great job! Focus session completed."
    )

    if (
        selected_task[0]
        and not is_quick_focus
    ):
        earned_points = calculate_points(
            selected_duration
        )

        task_data[
            selected_task[0]
        ]["focus_minutes"] += (
            selected_duration
        )

        task_data[
            selected_task[0]
        ]["sessions"] += 1

        task_data[
            selected_task[0]
        ]["points"] += (
            earned_points
        )

        today = date.today()

        last_date = task_data[
            selected_task[0]
        ]["last_focus_date"]

        if last_date is None:
            task_data[
                selected_task[0]
            ]["streak"] = 1

        elif (
            today - last_date
        ).days == 1:

            task_data[
                selected_task[0]
            ]["streak"] += 1

        elif (
            today - last_date
        ).days > 1:

            task_data[
                selected_task[0]
            ]["streak"] = 1

        task_data[
            selected_task[0]
        ]["last_focus_date"] = today

        update_task_stats(
            selected_task,
            task_data,
            streak_label,
            points_label,
            focus_label
        )

        save_data(
            task_data
        )

    is_quick_focus = False

    return is_quick_focus