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

    "consistency": {
        "title": "🔥 Consistency Starter",
        "message":
        "Maintained a 3-day streak!"
    }
}

def check_achievements(
    app,
    selected_duration,
    task,
    show_notification
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
        not in shown_achievements
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

        shown_achievements.add(
            "focus_beginner"
        )

    # ⏳ Focus time achievement
    if (
        task["focus_minutes"] == 60
        and "deep_focus"
        not in shown_achievements
    ):

        unlocked.append(
            (
                "⏳ Deep Worker",
                "Focused for 1 total hour!"
            )
        )

        shown_achievements.add(
            "deep_focus"
        )

    # 🔥 Streak achievement
    if (
        task["streak"] >= 3
        and "consistency"
        not in shown_achievements
    ):

        unlocked.append(
            (
                "🔥 Consistency Starter",
                "Maintained a 3-day streak!"
            )
        )

        shown_achievements.add(
            "consistency"
        )

    for title, message in unlocked:
        show_notification(
            app,
            "🏆 Achievement Unlocked!",
            f"{title}\n{message}"
        )