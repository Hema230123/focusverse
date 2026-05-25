from PIL import Image
from customtkinter import CTkImage

def draw_base_plant_area(
    plant_canvas
):
    plant_canvas.delete(
        "all"
    )

    # soft circle background
    plant_canvas.create_oval(
        20, 10,
        220, 210,
        fill="#DCE5B6",
        outline=""
    )

    # soil
    plant_canvas.create_oval(
        55, 135,
        185, 175,
        fill="#7B4B1A",
        outline=""
    )

def load_plant_images():

    plant_images = {
        "seed": CTkImage(
            light_image=Image.open(
                "assets/seed.png"
            ),
            size=(150, 150)
        ),

        "sprout": CTkImage(
            light_image=Image.open(
                "assets/sprout.png"
            ),
            size=(150, 150)
        ),

        "plant": CTkImage(
            light_image=Image.open(
                "assets/plant.png"
            ),
            size=(150, 150)
        ),

        "tree": CTkImage(
            light_image=Image.open(
                "assets/tree.png"
            ),
            size=(150, 150)
        )
    }

    return plant_images


def update_plant_growth(
    plant_label,
    plant_images,
    progress_percentage
):

    if progress_percentage < 25:

        plant_label.configure(
            image=plant_images["seed"]
        )

    elif progress_percentage < 50:

        plant_label.configure(
            image=plant_images["sprout"]
        )

    elif progress_percentage < 75:

        plant_label.configure(
            image=plant_images["plant"]
        )

    else:

        plant_label.configure(
            image=plant_images["tree"]
        )