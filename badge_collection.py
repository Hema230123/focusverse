import customtkinter


def open_badges_page(
    app,
    task_data
):

    # prevent multiple windows
    if hasattr(
        app,
        "badge_window"
    ):

        if (
            app.badge_window
            is not None
            and app.badge_window
            .winfo_exists()
        ):
            app.badge_window.focus()
            return

    app.badge_window = (
        customtkinter
        .CTkToplevel(app)
    )

    badge_window = (
        app.badge_window
    )

    badge_window.title(
        "My Badges"
    )

    badge_window.geometry(
        "500x500"
    )

    badge_window.attributes(
        "-topmost",
        True
    )

    title_label = (
        customtkinter
        .CTkLabel(
            badge_window,
            text=(
                "🏅 My Badge Collection"
            ),
            font=(
                "Arial",
                24,
                "bold"
            )
        )
    )

    title_label.pack(
        pady=20
    )

    earned_label = (
        customtkinter
        .CTkLabel(
            badge_window,
            text=(
                "Earned Badges"
            ),
            font=(
                "Arial",
                18,
                "bold"
            )
        )
    )

    earned_label.pack(
        pady=(10, 10)
    )

    earned_badges = set()

    for task in (
        task_data.values()
    ):

        for badge in task[
            "achievements"
        ]:

            earned_badges.add(
                badge
            )

    if earned_badges:

        for badge in (
            earned_badges
        ):

            badge_card = (
                customtkinter
                .CTkLabel(
                    badge_window,
                    text=f"🏆 {badge}",
                    font=(
                        "Arial",
                        14
                    )
                )
            )

            badge_card.pack(
                pady=5
            )

    else:

        no_badges_label = (
            customtkinter
            .CTkLabel(
                badge_window,
                text=(
                    "No badges earned yet 😄"
                ),
                font=(
                    "Arial",
                    14
                )
            )
        )

        no_badges_label.pack(
            pady=10
        )

    def on_close():

        app.badge_window = None
        badge_window.destroy()

    badge_window.protocol(
        "WM_DELETE_WINDOW",
        on_close
    )