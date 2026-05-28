import customtkinter


def open_profile(
    app,
    current_user,
    selected_task,
    task_data,
    shown_achievements
):

    profile_window = (
        customtkinter
        .CTkToplevel(
            app
        )
    )

    profile_window.title(
        "My Profile"
    )

    profile_window.geometry(
        "420x500"
    )

    profile_window.resizable(
        False,
        False
    )

    profile_window.grab_set()

    # center popup
    window_width = 420
    window_height = 500

    screen_width = (
        profile_window
        .winfo_screenwidth()
    )

    screen_height = (
        profile_window
        .winfo_screenheight()
    )

    x_position = (
        screen_width // 2
    ) - (
        window_width // 2
    )

    y_position = (
        screen_height // 2
    ) - (
        window_height // 2
    )

    profile_window.geometry(
        f"{window_width}x{window_height}"
        f"+{x_position}"
        f"+{y_position}"
    )

    # title
    title_label = (
        customtkinter
        .CTkLabel(
            profile_window,
            text=(
                f"👤 "
                f"{current_user[0]}"
            ),
            font=(
                "Arial",
                28,
                "bold"
            )
        )
    )
    title_label.pack(
        pady=(25, 10)
    )

    selected_task_name = (
        selected_task[0]
    )

    streak = 0
    points = 0
    focus_time = 0

    if selected_task_name:

        streak = (
            task_data[
                selected_task_name
            ][
                "session_streak"
            ]
        )

        points = (
            task_data[
                selected_task_name
            ][
                "points"
            ]
        )

        focus_time = (
            task_data[
                selected_task_name
            ][
                "focus_time"
            ]
        )

    stats = [

        (
            "🔥 Current Streak",
            f"{streak} days"
        ),

        (
            "⭐ Points",
            str(points)
        ),

        (
            "⏱ Focus Time",
            (
                f"{focus_time} mins"
            )
        ),

        (
            "🌱 Trees Grown",
            "0"
        ),

        (
            "🏅 Badges Earned",
            (
                f"{len(shown_achievements)}"
            )
        )
    ]

    for label, value in stats:

        stat_card = (
            customtkinter
            .CTkFrame(
                profile_window,
                corner_radius=12
            )
        )

        stat_card.pack(
            padx=30,
            pady=8,
            fill="x"
        )

        stat_label = (
            customtkinter
            .CTkLabel(
                stat_card,
                text=(
                    f"{label}: "
                    f"{value}"
                ),
                font=(
                    "Arial",
                    16
                )
            )
        )

        stat_label.pack(
            pady=12
        )

    close_button = (
        customtkinter
        .CTkButton(
            profile_window,
            text="Close",
            command=(
                profile_window
                .destroy
            )
        )
    )

    close_button.pack(
        pady=20
    )