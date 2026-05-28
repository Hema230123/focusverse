import json
from tkinter import messagebox


USERS_FILE = "users.json"


def load_users():

    try:
        with open(
            USERS_FILE,
            "r"
        ) as file:

            return json.load(
                file
            )

    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        return {}


def save_users(
    users
):

    with open(
        USERS_FILE,
        "w"
    ) as file:

        json.dump(
            users,
            file,
            indent=4
        )


def signup_user(
    username,
    password,
    confirm_password
):

    users = load_users()

    # empty fields
    if (
        username.strip() == ""
        or password.strip() == ""
    ):

        messagebox.showerror(
            "Error",
            "Please fill all fields."
        )

        return False

    # password match
    if (
        password
        != confirm_password
    ):

        messagebox.showerror(
            "Error",
            "Passwords do not match."
        )

        return False

    # username exists
    if username in users:

        messagebox.showerror(
            "Error",
            "Username already exists."
        )

        return False

    users[
        username
    ] = {

        "password":
        password
    }

    save_users(
        users
    )

    messagebox.showinfo(
        "Success",
        "Account created successfully!"
    )

    return True


def login_user(
    username,
    password
):

    users = load_users()

    if (
        username in users
        and users[
            username
        ][
            "password"
        ] == password
    ):

        return True

    messagebox.showerror(
        "Error",
        "Invalid username or password."
    )

    return False