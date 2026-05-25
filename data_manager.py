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