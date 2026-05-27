import customtkinter
from PIL import (
    Image,
    ImageEnhance
)

BADGE_INFO = {

    "focus_starter":
    "Complete your first 25-min session",

    "deep_worker":
    "Complete your first 45-min session",

    "forest_mind":
    "Complete your first 60-min session",

    "tiny_steps":
    "Complete 5 focus sessions",

    "locked_in":
    "Complete 3 sessions in one day",

    "consistency_starter":
    "Maintain a 3-day streak",

    "unstoppable":
    "Maintain a 7-day streak",

    "night_owl":
    "Complete 10 late-night sessions",

    "early_momentum":
    "Complete 10 early-morning sessions",

    "marathoner":
    "Complete 3 sessions in one day",

    "forest_builder":
    "Complete 100 focus sessions",

    "earth_guardian":
    "Sponsor your first real tree"
}


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

    window_width = 620
    window_height = 720
    screen_width = (
        badge_window
        .winfo_screenwidth()
    )
    screen_height = (
        badge_window
        .winfo_screenheight()
    )
    x = int(
        (
            screen_width
            - window_width
        ) / 2
    )
    y = int(
        (
            screen_height
            - window_height
        ) / 2
    )
    badge_window.geometry(
        f"{window_width}x"
        f"{window_height}"
        f"+{x}+{y}"
    )

    badge_window.resizable(
        False,
        False
    )

    badge_window.attributes(
        "-topmost",
        True
    )

    # collect earned badges
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

    # progress calculations
    total_badges = len(
        BADGE_INFO
    )

    earned_count = len(
        earned_badges
    )

    progress_percent = int(
        (
            earned_count
            / total_badges
        ) * 100
    )

    # title
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

    progress_label = (
        customtkinter
        .CTkLabel(
            badge_window,
            text=(
                f"📈 Progress: "
                f"{earned_count}/"
                f"{total_badges} "
                f"({progress_percent}%)"
            ),
            font=(
                "Arial",
                16,
                "bold"
            ),
            text_color="#22C55E"
        )
    )
    progress_label.pack(
        pady=(0, 10)
    )

    scroll_frame = (
        customtkinter
        .CTkScrollableFrame(
            badge_window,
            width=470,
            height=520,
            fg_color="transparent"
        )
    )
    scroll_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    all_badges = list(
        BADGE_INFO.keys()
    )

    locked_badges = [

        badge

        for badge in all_badges

        if badge
        not in earned_badges
    ]

    # earned badges
    if earned_badges:
        earned_title = (
            customtkinter
            .CTkLabel(
                scroll_frame,
                text=(
                    f"🏅 Earned Badges "
                    f"({earned_count}/"
                    f"{total_badges})"
                ),
                font=(
                    "Arial",
                    20,
                    "bold"
                )
            )
        )
        earned_title.pack(
            pady=(10, 15)
        )
        earned_grid = (
            customtkinter
            .CTkFrame(
                scroll_frame,
                fg_color="transparent"
            )
        )
        earned_grid.pack()
        col = 0
        row = 0

        for badge in earned_badges:
            image_path = (
                f"assets/badges/"
                f"{badge}.png"
            )
            badge_image = (
                customtkinter
                .CTkImage(
                    light_image=Image.open(
                        image_path
                    ),
                    dark_image=Image.open(
                        image_path
                    ),
                    size=(
                        100,
                        100
                    )
                )
            )

            badge_card = (
                customtkinter
                .CTkFrame(
                    earned_grid,
                    width=150,
                    height=170,
                    corner_radius=18,
                    border_width=1,
                    border_color="#22C55E",
                    fg_color="#222222"
                )
            )
            badge_card.grid(
                row=row,
                column=col,
                padx=12,
                pady=12
            )
            badge_card.pack_propagate(
                False
            )
            image_label = (
                customtkinter
                .CTkLabel(
                    badge_card,
                    image=badge_image,
                    text=""
                )
            )
            image_label.pack(
                pady=(10, 5)
            )
            name_label = (
                customtkinter
                .CTkLabel(
                    badge_card,
                    text=(
                        badge
                        .replace(
                            "_",
                            " "
                        )
                        .title()
                    ),
                    font=(
                        "Arial",
                        14,
                        "bold"
                    )
                )
            )
            name_label.pack()
            status_label = (
                customtkinter
                .CTkLabel(
                    badge_card,
                    text="Unlocked 😎",
                    font=(
                        "Arial",
                        12
                    )
                )
            )
            status_label.pack(
                pady=(0, 8)
            )

            col += 1
            if col > 2:
                col = 0
                row += 1

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

    locked_title = (
        customtkinter
        .CTkLabel(
            scroll_frame,
            text="🔒 Locked Badges",
            font=(
                "Arial",
                20,
                "bold"
            )
        )
    )
    locked_title.pack(
        pady=(25, 15)
    )
    locked_grid = (
        customtkinter
        .CTkFrame(
            scroll_frame,
            fg_color="transparent"
        )
    )
    locked_grid.pack()
    col = 0
    row = 0
    for badge in locked_badges:
        image_path = (
            f"assets/badges/"
            f"{badge}.png"
        )
        badge_image = (
            customtkinter
            .CTkImage(
                light_image=Image.open(
                    image_path
                ),
                dark_image=Image.open(
                    image_path
                ),
                size=(100, 100)
            )
        )
        badge_card = (
            customtkinter
            .CTkFrame(
                locked_grid,
                width=150,
                height=185,
                corner_radius=18,
                fg_color="#1F1F1F"
            )
        )
        badge_card.grid(
            row=row,
            column=col,
            padx=12,
            pady=12
        )
        badge_card.pack_propagate(
            False
        )
        image_label = (
            customtkinter
            .CTkLabel(
                badge_card,
                image=badge_image,
                text=""
            )
        )
        image_label.pack(
            pady=(10, 5)
        )
        name_label = (
            customtkinter
            .CTkLabel(
                badge_card,
                text=(
                    badge
                    .replace(
                        "_",
                        " "
                    )
                    .title()
                ),
                font=(
                    "Arial",
                    14,
                    "bold"
                ),
                text_color="gray70"
            )
        )
        name_label.pack()
        description_label = (
            customtkinter
            .CTkLabel(
                badge_card,
                text=(
                    BADGE_INFO[
                        badge
                    ]
                ),
                font=(
                    "Arial",
                    11
                ),
                text_color="gray55",
                wraplength=120
            )
        )
        description_label.pack(
            pady=(4, 2)
        )
        status_label = (
            customtkinter
            .CTkLabel(
                badge_card,
                text="🔒 Locked",
                font=(
                    "Arial",
                    12
                ),
                text_color="gray60"
            )
        )
        status_label.pack(
            pady=(0, 8)
        )

        col += 1
        if col > 2:
            col = 0
            row += 1

    def on_close():

        app.badge_window = None
        badge_window.destroy()

    badge_window.protocol(
        "WM_DELETE_WINDOW",
        on_close
    )