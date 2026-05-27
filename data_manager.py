import json
import tkinter as tk
from datetime import date


# creating load function
def load_data(
    task_listbox,
    tasks,
    task_data
):

    try:
        with open(
            "focusverse_data.json",
            "r"
        ) as file:

            loaded_data = json.load(file)

            task_data.clear()
            task_data.update(
                loaded_data
            )

            tasks.clear()
            tasks.extend(
                task_data.keys()
            )

            for task in task_data:

                if (
                    "achievements"
                    not in task_data[task]
                ):
                    task_data[task][
                        "achievements"
                    ] = []

                if (
                    "night_sessions"
                    not in task_data[task]
                ):
                    task_data[task][
                        "night_sessions"
                    ] = 0

                if (
                    "morning_sessions"
                    not in task_data[task]
                ):
                    task_data[task][
                        "morning_sessions"
                    ] = 0

                if (
                    "daily_sessions"
                    not in task_data[task]
                ):
                    task_data[task][
                        "daily_sessions"
                    ] = 0

                if (
                    "focus_sessions"
                    not in task_data[task]
                ):
                    task_data[task][
                        "focus_sessions"
                    ] = 0

                if (
                    "session_streak"
                    not in task_data[task]
                ):
                    task_data[task][
                        "session_streak"
                    ] = 0

                if (
                    "missed_day"
                    not in task_data[task]
                ):
                    task_data[task][
                        "missed_day"
                    ] = False

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

                today = date.today()
                last_date = (
                    task_data[task][
                        "last_focus_date"
                    ]
                )
                if last_date:
                    days_difference = (
                        today
                        - last_date
                    ).days

                    # missed day
                    if (
                        days_difference > 1
                    ):
                        task_data[task][
                            "session_streak"
                        ] = 0
                        task_data[task][
                            "missed_day"
                        ] = True

                    # new day
                    if (
                        days_difference >= 1
                    ):
                        task_data[task][
                            "daily_sessions"
                        ] = 0

                task_listbox.insert(
                    tk.END,
                    task
                )

    except FileNotFoundError:
        pass


# creating save function
def save_data(
    task_data
):

    with open(
        "focusverse_data.json",
        "w"
    ) as file:

        json.dump(
            task_data,
            file,
            default=str
        )