import customtkinter
from PIL import Image


def show_badge_popup(
    app,
    badge_title,
    badge_message
):

    popup = customtkinter.CTkFrame(
        app,
        width=420,
        height=120,
        corner_radius=20,
        fg_color="#1E293B",
        border_width=2,
        border_color="#22C55E"
    )

    popup.pack_propagate(
        False
    )

    # badge image path
    badge_key = (
        badge_title
        .lower()
        .replace(" ", "_")
    )

    badge_path = (
        f"assets/badges/"
        f"{badge_key}.png"
    )

    badge_image = (
        customtkinter
        .CTkImage(
            light_image=Image.open(
                badge_path
            ),
            dark_image=Image.open(
                badge_path
            ),
            size=(60, 60)
        )
    )

    # start above screen
    start_y = -130
    final_y = 35

    popup.place(
        relx=0.5,
        y=start_y,
        anchor="n"
    )

    # main content frame
    content_frame = (
        customtkinter
        .CTkFrame(
            popup,
            fg_color="transparent"
        )
    )

    content_frame.pack(
        expand=True,
        fill="both",
        padx=15,
        pady=12
    )

    # badge image
    image_label = (
        customtkinter
        .CTkLabel(
            content_frame,
            image=badge_image,
            text=""
        )
    )

    image_label.pack(
        side="left",
        padx=(5, 12)
    )

    # text section
    text_frame = (
        customtkinter
        .CTkFrame(
            content_frame,
            fg_color="transparent"
        )
    )

    text_frame.pack(
        side="left",
        fill="both",
        expand=True
    )

    title_label = (
        customtkinter
        .CTkLabel(
            text_frame,
            text=(
                f"🏆 "
                f"{badge_title} "
                f"Unlocked!"
            ),
            font=(
                "Arial",
                17,
                "bold"
            ),
            anchor="w"
        )
    )

    title_label.pack(
        anchor="w"
    )

    message_label = (
        customtkinter
        .CTkLabel(
            text_frame,
            text=badge_message,
            font=(
                "Arial",
                13
            ),
            justify="left",
            anchor="w"
        )
    )

    message_label.pack(
        anchor="w",
        pady=(2, 0)
    )

    # slide down animation
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

    # slide up animation
    def slide_up(
        current_y
    ):

        if current_y > -140:

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