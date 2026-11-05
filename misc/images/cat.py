import io
import tkinter as tk

import requests
from PIL import Image, ImageTk

API_URL = "https://api.thecatapi.com/v1/images/search"
MAX_SIZE = (700, 700)

def load_cat():
    button.config(state="disabled", text="Loading...")
    root.update_idletasks()
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        url = response.json()[0]["url"]

        image_data = requests.get(url, timeout=10)
        image_data.raise_for_status()

        img = Image.open(io.BytesIO(image_data.content))
        img.thumbnail(MAX_SIZE)            # shrink to fit the window
        photo = ImageTk.PhotoImage(img)

        label.config(image=photo, text="")
        label.image = photo                # keep a reference, or it disappears
    except Exception as e:
        label.config(image="", text=f"Error: {e}")
    finally:
        button.config(state="normal", text="New cat")

root = tk.Tk()
root.title("Random Cat")

label = tk.Label(root)
label.pack(padx=10, pady=10)

button = tk.Button(root, text="New cat", command=load_cat)
button.pack(pady=(0, 10))

load_cat()          # show a cat when the window opens
root.mainloop()