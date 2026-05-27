ACHIEVEMENTS = {

    "focus_starter": {
        "title": "🌱 Focus Starter",
        "message":
        "Completed your first 25-minute focus session!"
    },

    "deep_worker": {
        "title": "🌿 Deep Worker",
        "message":
        "Completed your first 45-minute deep focus!"
    },

    "forest_mind": {
        "title": "🌳 Forest Mind",
        "message":
        "Completed your first 60-minute focus session!"
    },

    "focus_beginner": {
        "title": "⭐ Focus Beginner",
        "message":
        "Earned 50 focus points!"
    },

    "deep_focus": {
        "title": "⏳ Deep Focus",
        "message":
        "Focused for 1 total hour!"
    },

    "night_owl": {
        "title": "🌙 Night Owl",
        "message":
        "You stayed focused while the world slept 🌙"
    },

    "early_bird": {
        "title": "☀️ Early Bird",
        "message":
        "You showed up before the world woke up ☀️"
    },

    "marathoner": {
        "title": "⚡ Marathoner",
        "message":
        "Locked in for the day ⚡"
    },

    "tiny_steps": {
        "title": "🌱 Tiny Steps",
        "message":
        "Every big journey starts small 🌱"
    },

    "locked_in": {
        "title": "🧠 Locked In",
        "message":
        "You're fully in the zone 🧠"
    },

    "comeback": {
        "title": "🔥 Comeback",
        "message":
        "Welcome back stronger 🔥"
    },

    "consistency_starter": {
        "title": "🔥 Consistency Starter",
        "message":
        "Maintained a 3-day streak!"
    },

    "unstoppable": {
        "title": "🚀 Unstoppable",
        "message":
        "Maintained a 7-day streak!"
    }
}


def check_achievements(
    app,
    selected_duration,
    task,
    show_notification,
    show_badge_popup
):

    unlocked = []

    # 🌱 25 min achievement
    if (
        selected_duration == 25
        and "focus_starter"
        not in task["achievements"]
    ):
        achievement = ACHIEVEMENTS[
            "focus_starter"
        ]

        unlocked.append(
            (
                achievement["title"],
                achievement["message"]
            )
        )

        task["achievements"].append(
            "focus_starter"
        )

    # 🌿 45 min achievement
    if (
        selected_duration == 45
        and "deep_worker"
        not in task["achievements"]
    ):
        achievement = ACHIEVEMENTS[
            "deep_worker"
        ]

        unlocked.append(
            (
                achievement["title"],
                achievement["message"]
            )
        )

        task["achievements"].append(
            "deep_worker"
        )

    # 🌳 60 min achievement
    if (
        selected_duration == 60
        and "forest_mind"
        not in task["achievements"]
    ):
        achievement = ACHIEVEMENTS[
            "forest_mind"
        ]

        unlocked.append(
            (
                achievement["title"],
                achievement["message"]
            )
        )

        task["achievements"].append(
            "forest_mind"
        )

    # ⭐ Points achievement
    if (
        task["points"] == 50
        and "focus_beginner"
        not in task["achievements"]
    ):
        achievement = ACHIEVEMENTS[
            "focus_beginner"
        ]

        unlocked.append(
            (
                achievement["title"],
                achievement["message"]
            )
        )

        task["achievements"].append(
            "focus_beginner"
        )

    # ⏳ Focus time achievement
    if (
        task["focus_minutes"] == 60
        and "deep_focus"
        not in task["achievements"]
    ):
        achievement = ACHIEVEMENTS[
            "deep_focus"
        ]

        unlocked.append(
            (
                achievement["title"],
                achievement["message"]
            )
        )

        task["achievements"].append(
            "deep_focus"
        )

    # 🔥 Consistency Starter
    if (
        task["session_streak"] == 3
        and "consistency_starter"
        not in task["achievements"]
    ):

        achievement = ACHIEVEMENTS[
            "consistency_starter"
        ]

        unlocked.append(
            (
                achievement["title"],
                achievement["message"]
            )
        )

        task["achievements"].append(
            "consistency_starter"
        )

    # 🚀 Unstoppable
    if (
        task["session_streak"] == 7
        and "unstoppable"
        not in task["achievements"]
    ):

        achievement = ACHIEVEMENTS[
            "unstoppable"
        ]

        unlocked.append(
            (
                achievement["title"],
                achievement["message"]
            )
        )

        task["achievements"].append(
            "unstoppable"
        )

    # 🌙 Night Owl achievement
    if (
        task["night_sessions"] == 10
        and "night_owl"
        not in task["achievements"]
    ):
        achievement = ACHIEVEMENTS[
            "night_owl"
        ]

        unlocked.append(
            (
                achievement["title"],
                achievement["message"]
            )
        )

        task["achievements"].append(
            "night_owl"
        )

    # ☀️ Early Bird achievement
    if (
        task["morning_sessions"] == 10
        and "early_bird"
        not in task["achievements"]
    ):
        achievement = ACHIEVEMENTS[
            "early_bird"
        ]

        unlocked.append(
            (
                achievement["title"],
                achievement["message"]
            )
        )

        task["achievements"].append(
            "early_bird"
        )

    # ⚡ Marathoner achievement
    if (
        task["daily_sessions"] == 3
        and "marathoner"
        not in task["achievements"]
    ):
        achievement = ACHIEVEMENTS[
            "marathoner"
        ]

        unlocked.append(
            (
                achievement["title"],
                achievement["message"]
            )
        )

        task["achievements"].append(
            "marathoner"
        )

    # 🌱 Tiny Steps achievement
    if (
        task["focus_sessions"] == 5
        and "tiny_steps"
        not in task["achievements"]
    ):
        achievement = ACHIEVEMENTS[
            "tiny_steps"
        ]

        unlocked.append(
            (
                achievement["title"],
                achievement["message"]
            )
        )

        task["achievements"].append(
            "tiny_steps"
        )

    # 🧠 Locked In achievement
    if (
        task["session_streak"] == 3
        and "locked_in"
        not in task["achievements"]
    ):
        achievement = ACHIEVEMENTS[
            "locked_in"
        ]

        unlocked.append(
            (
                achievement["title"],
                achievement["message"]
            )
        )

        task["achievements"].append(
            "locked_in"
        )

    # 🔥 Comeback achievement
    if (
        task["missed_day"]
        and "comeback"
        not in task["achievements"]
    ):
        achievement = ACHIEVEMENTS[
            "comeback"
        ]

        unlocked.append(
            (
                achievement["title"],
                achievement["message"]
            )
        )

        task["achievements"].append(
            "comeback"
        )

        task["missed_day"] = False

    major_badges = [
        "Night Owl",
        "Early Bird",
        "Marathoner"
    ]

    for title, message in unlocked:

        if any(
            badge in title
            for badge in major_badges
        ):

            show_badge_popup(
                app,
                title,
                message
            )

        else:

            show_notification(
                app,
                "🏆 Achievement Unlocked!",
                f"{title}\n{message}"
            )