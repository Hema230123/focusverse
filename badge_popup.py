import customtkinter


def show_badge_popup(
    app,
    badge_title,
    badge_message
):

    popup = customtkinter.CTkFrame(
        app,
        width=360,
        height=82,
        corner_radius=18,
        fg_color="#1E293B",
        border_width=2,
        border_color="#22C55E"
    )

    # Start above screen
    start_y = -90
    final_y = 35

    popup.place(
        relx=0.5,
        y=start_y,
        anchor="n"
    )

    title_label = customtkinter.CTkLabel(
        popup,
        text=f"🏆 {badge_title} Unlocked!",
        font=("Arial", 17, "bold")
    )
    title_label.pack(
        pady=(10, 0)
    )

    message_label = customtkinter.CTkLabel(
        popup,
        text=badge_message,
        font=("Arial", 13)
    )
    message_label.pack(
        pady=(2, 8)
    )

    # Slide down animation
    def slide_down(
        current_y
    ):

        if current_y < final_y:

            current_y += 5

            popup.place(
                relx=0.5,
                y=current_y,
                anchor="n"
            )

            app.after(
                10,
                lambda:
                slide_down(
                    current_y
                )
            )

        else:

            app.after(
                3000,
                lambda:
                slide_up(
                    final_y
                )
            )

    # Slide up animation
    def slide_up(
        current_y
    ):

        if current_y > -100:

            current_y -= 5

            popup.place(
                relx=0.5,
                y=current_y,
                anchor="n"
            )

            app.after(
                10,
                lambda:
                slide_up(
                    current_y
                )
            )

        else:

            popup.destroy()

    slide_down(
        start_y
    )