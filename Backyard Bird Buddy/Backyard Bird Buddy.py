import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import winsound
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PHOTOS_DIR = os.path.join(BASE_DIR, "Photos")
SOUNDS_DIR = os.path.join(BASE_DIR, "Sounds")


birds = [
    {
        "name": "Northern Cardinal",
        "image": os.path.join(PHOTOS_DIR, "Cardinal.png"),
        "sound": os.path.join(SOUNDS_DIR, "CardinalSong.wav"),
        "description": "The Northern Cardinal is a bright, year‑round resident found across the eastern and central United States, parts of the Southwest, and southern Canada. It lives in brushy forests, thickets, parks, and backyard shrubs where it can stay hidden while foraging. Cardinals eat mainly seeds and berries but also insects, especially during breeding season. Males are vivid red with a black mask, while females are warm brown with red highlights, and both have a tall crest and strong cone‑shaped bill. They’re common at feeders, known for their clear whistled songs, and often stay in the same area all year."
    },
    {
        "name": "American Robin",
        "image": os.path.join(PHOTOS_DIR, "Robin.png"),
        "sound": os.path.join(SOUNDS_DIR, "RobinSong.wav"),
        "description": "The American Robin is a familiar, widespread bird found across nearly all of North America. It thrives in lawns, parks, forests, and backyards, often seen hopping on the ground searching for worms. Robins eat insects, earthworms, and berries, switching to more fruit in winter. Males and females look similar, with warm orange bellies and gray backs. Their cheerful songs and early‑morning activity make them one of the most recognizable birds in the country."
    },
    {
        "name": "American Goldfinch",
        "image": os.path.join(PHOTOS_DIR, "Goldfinch.png"),
        "sound": os.path.join(SOUNDS_DIR, "GoldfinchSong.wav"),
        "description": "The American Goldfinch is a bright, lively finch found across most of the United States and southern Canada. It prefers open fields, meadows, gardens, and weedy areas where it feeds mainly on seeds from thistles, sunflowers, and other plants. Males turn vibrant yellow in summer and olive in winter, while females stay softer in color year‑round. Goldfinches are acrobatic feeders, often visiting backyard feeders and flying with a distinctive bouncy pattern."
    },
    {
        "name": "Eastern Bluebird",
        "image": os.path.join(PHOTOS_DIR, "Bluebird.png"),
        "sound": os.path.join(SOUNDS_DIR, "BluebirdSong.wav"),
        "description": "The Eastern Bluebird is a gentle, colorful bird found in open fields, orchards, pastures, and suburban areas across the eastern United States. Males are bright blue with rusty chests, while females are softer blue‑gray. Bluebirds eat insects, caterpillars, beetles, and berries, often perching on wires or fence posts before swooping down to catch prey. They readily use nest boxes and are year‑round residents in many southern areas, migrating shorter distances in colder regions."
    },
    {
        "name": "Carolina Wren",
        "image": os.path.join(PHOTOS_DIR, "Wren.png"),
        "sound": os.path.join(SOUNDS_DIR, "WrenSong.wav"),
        "description": "The Carolina Wren is a small, energetic bird found year‑round in the southeastern and eastern United States. It prefers dense shrubs, wooded areas, and cluttered backyard spaces where it can stay hidden. Wrens eat insects, spiders, and occasionally seeds or berries. They’re known for their loud, ringing songs and their habit of exploring porches, garages, and nooks around homes. Their bold personality and upright tail make them easy to spot once you know their behavior."
    },
    {
        "name": "Baltimore Oriole",
        "image": os.path.join(PHOTOS_DIR, "Oriole.png"),
        "sound": os.path.join(SOUNDS_DIR, "BaltimoreSong.wav"),
        "description": "The Baltimore Oriole is a striking orange‑and‑black songbird found in the eastern and central United States during spring and summer. It lives in open woods, parks, and backyard trees, weaving hanging pouch‑like nests high in branches. Orioles feed on insects, fruit, and nectar, and they’re known to visit feeders offering oranges or sugar water. Their rich, whistled songs and bright colors make them a favorite sign of warmer weather."
    },
    {
        "name": "Blue Jay",
        "image": os.path.join(PHOTOS_DIR, "BlueJay.png"),
        "sound": os.path.join(SOUNDS_DIR, "BlueJaySong.wav"),
        "description": "The Blue Jay is an intelligent, bold bird found throughout the eastern and central United States in forests, parks, and suburban neighborhoods. It eats acorns, seeds, nuts, insects, and occasionally small animals or eggs. Blue Jays are known for their loud calls, strong family bonds, and ability to mimic hawks. Their bright blue feathers, crested heads, and curious behavior make them one of the most recognizable backyard birds."
    },
    {
        "name": "Pileated Woodpecker",
        "image": os.path.join(PHOTOS_DIR, "Woodpecker.png"),
        "sound": os.path.join(SOUNDS_DIR, "WoodpeckerSong.wav"),
        "description": "A large woodpecker with a flaming red crest, famous for its deep rectangular holes in trees."
    },
    {
        "name": "Carolina Chickadee",
        "image": os.path.join(PHOTOS_DIR, "Chickadee.png"),
        "sound": os.path.join(SOUNDS_DIR, "ChickadeeSong.wav"),
        "description": "The Carolina Chickadee is a tiny, active songbird found year‑round in the southeastern United States, especially in forests, wooded neighborhoods, and parks. It eats seeds, berries, and insects, often hanging upside‑down while foraging in trees. These birds travel in small flocks, frequently visiting feeders and calling with their familiar chick‑a‑dee‑dee notes. They nest in cavities and stay in the same area all year, making them a common backyard companion"
    }
]

def load_image(path, size=(150, 150)):
    try:
        img = Image.open(path)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)
    except:
        return None

def play_sound(sound_path):
    try:
        winsound.PlaySound(sound_path, winsound.SND_FILENAME)
    except:
        messagebox.showerror("Error", "Sound file not found.")

def open_profile(bird):
    profile = tk.Toplevel()
    profile.title(bird["name"])

    img = load_image(bird["image"], size=(250, 250))

    img_label = tk.Label(profile, image=img)
    img_label.image = img
    img_label.pack(pady=10)

    name_label = tk.Label(profile, text=bird["name"], font=("Arial", 18, "bold"))
    name_label.pack()

    desc_label = tk.Label(profile, text=bird["description"], wraplength=350, justify="left")
    desc_label.pack(pady=10)

    sound_btn = tk.Button(profile, text="Play Bird Song",
                          command=lambda: play_sound(bird["sound"]))
    sound_btn.pack(pady=5)

    close_btn = tk.Button(profile, text="Close", command=profile.destroy)
    close_btn.pack(pady=5)

def validate_input(text):
    return text.strip() != "" and text.replace(" ", "").isalpha()

def search_bird():
    user_input = entry.get()

    if not validate_input(user_input):
        messagebox.showerror("Error", "Enter a valid bird name.")
        return

    for bird in birds:
        if bird["name"].lower() == user_input.lower():
            open_profile(bird)
            return

    messagebox.showinfo("Bird not found.")

root = tk.Tk()
root.title("Backyard Bird Buddy")

title_label = tk.Label(root, text="Backyard Bird Buddy", font=("Arial", 22))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

for index, bird in enumerate(birds):
    row = (index // 3) + 1
    col = index % 3

    frame = tk.Frame(root, padx=10, pady=10)
    frame.grid(row=row, column=col)

    img = load_image(bird["image"])

    btn = tk.Button(frame, image=img,
                    command=lambda b=bird: open_profile(b))
    btn.image = img
    btn.pack()

    label = tk.Label(frame, text=bird["name"])
    label.pack()

entry = tk.Entry(root)
entry.grid(row=5, column=0, pady=10)

search_btn = tk.Button(root, text="Search Bird", command=search_bird)
search_btn.grid(row=5, column=1)

exit_btn = tk.Button(root, text="Exit", command=root.destroy)
exit_btn.grid(row=5, column=2)

root.mainloop()
