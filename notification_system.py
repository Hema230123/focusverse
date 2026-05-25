import customtkinter


active_notifications = []


def show_notification(
    app,
    title,
    message
):

    y_position = (
        0.05
        + (len(active_notifications) * 0.12)
    )

    notification = customtkinter.CTkFrame(
        app,
        width=380,
        height=120,
        corner_radius=20,
        fg_color="#2C2C2C",
        border_width=2,
        border_color="#4CAF50"
    )

    notification.place(
        relx=0.98,
        rely=y_position,
        anchor="ne"
    )

    active_notifications.append(
        notification
    )

    title_label = customtkinter.CTkLabel(
        notification,
        text=title,
        font=(
            "Arial",
            22,
            "bold"
        ),
        text_color="white"
    )

    title_label.pack(
        pady=(12, 5)
    )

    message_label = customtkinter.CTkLabel(
        notification,
        text=message,
        font=(
            "Arial",
            15
        ),
        text_color="#D3D3D3",
        wraplength=330,
        justify="center"
    )

    message_label.pack(
        padx=10,
        pady=(0, 10)
    )

    def remove_notification():

        notification.destroy()

        if (
            notification
            in active_notifications
        ):
            active_notifications.remove(
                notification
            )

    app.after(
        3500,
        remove_notification
    )