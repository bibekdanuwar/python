"""
Simple stylized portrait of a girl, drawn programmatically with Pillow.
No external images needed — everything is built from basic shapes.
"""

from PIL import Image, ImageDraw
import math

# Canvas setup
W, H = 800, 1000
img = Image.new("RGB", (W, H), (250, 235, 225))  # soft background
draw = ImageDraw.Draw(img)

# --- Background gradient ---
top_color = (255, 223, 211)
bottom_color = (250, 200, 190)
for y in range(H):
    t = y / H
    r = int(top_color[0] * (1 - t) + bottom_color[0] * t)
    g = int(top_color[1] * (1 - t) + bottom_color[1] * t)
    b = int(top_color[2] * (1 - t) + bottom_color[2] * t)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

cx, cy = W // 2, 430  # face center

# --- Hair (back layer, behind face) ---
hair_color = (90, 60, 50)
draw.ellipse([cx - 230, cy - 260, cx + 230, cy + 320], fill=hair_color)

# --- Neck ---
skin = (250, 214, 190)
draw.rectangle([cx - 45, cy + 150, cx + 45, cy + 260], fill=skin)

# --- Shoulders / shirt ---
shirt_color = (120, 150, 190)
draw.polygon(
    [
        (cx - 180, H),
        (cx - 120, cy + 230),
        (cx + 120, cy + 230),
        (cx + 180, H),
    ],
    fill=shirt_color,
)

# --- Face (oval) ---
face_w, face_h = 210, 260
draw.ellipse(
    [cx - face_w // 2, cy - face_h // 2, cx + face_w // 2, cy + face_h // 2],
    fill=skin,
)

# --- Ears ---
ear_color = skin
draw.ellipse([cx - face_w // 2 - 18, cy - 20, cx - face_w // 2 + 18, cy + 40], fill=ear_color)
draw.ellipse([cx + face_w // 2 - 18, cy - 20, cx + face_w // 2 + 18, cy + 40], fill=ear_color)

# --- Hair (front layer, over forehead) ---
draw.pieslice(
    [cx - face_w // 2 - 20, cy - face_h // 2 - 90, cx + face_w // 2 + 20, cy + 60],
    180, 360, fill=hair_color,
)
# side strands
draw.polygon([(cx - 115, cy - 60), (cx - 150, cy + 260), (cx - 90, cy + 200), (cx - 90, cy - 40)], fill=hair_color)
draw.polygon([(cx + 115, cy - 60), (cx + 150, cy + 260), (cx + 90, cy + 200), (cx + 90, cy - 40)], fill=hair_color)

# --- Eyebrows ---
brow_color = (70, 45, 40)
draw.line([(cx - 70, cy - 35), (cx - 25, cy - 42)], fill=brow_color, width=6)
draw.line([(cx + 25, cy - 42), (cx + 70, cy - 35)], fill=brow_color, width=6)

# --- Eyes ---
eye_white = (255, 255, 255)
iris_color = (100, 70, 150)
for ex in (cx - 50, cx + 50):
    ey = cy - 5
    draw.ellipse([ex - 30, ey - 18, ex + 30, ey + 18], fill=eye_white, outline=(60, 40, 40), width=2)
    draw.ellipse([ex - 14, ey - 14, ex + 14, ey + 14], fill=iris_color)
    draw.ellipse([ex - 6, ey - 6, ex + 6, ey + 6], fill=(20, 15, 20))
    draw.ellipse([ex - 3, ey - 9, ex + 2, ey - 4], fill=(255, 255, 255))  # eye sparkle

# --- Eyelashes (subtle) ---
draw.line([(cx - 80, cy - 15), (cx - 90, cy - 22)], fill=(40, 25, 25), width=3)
draw.line([(cx + 80, cy - 15), (cx + 90, cy - 22)], fill=(40, 25, 25), width=3)

# --- Nose ---
draw.line([(cx, cy + 10), (cx - 6, cy + 45)], fill=(210, 170, 150), width=3)
draw.arc([cx - 14, cy + 40, cx + 6, cy + 55], 20, 160, fill=(210, 170, 150), width=2)

# --- Mouth ---
mouth_color = (200, 100, 110)
draw.arc([cx - 35, cy + 70, cx + 35, cy + 105], 15, 165, fill=mouth_color, width=5)

# --- Blush ---
blush_color = (250, 170, 160)
blush_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
blush_draw = ImageDraw.Draw(blush_layer)
blush_draw.ellipse([cx - 110, cy + 25, cx - 55, cy + 60], fill=blush_color + (90,))
blush_draw.ellipse([cx + 55, cy + 25, cx + 110, cy + 60], fill=blush_color + (90,))
img.paste(Image.alpha_composite(img.convert("RGBA"), blush_layer).convert("RGB"))

# --- Simple hair accessory (bow) ---
bow_color = (220, 90, 110)
bx, by = cx + 150, cy - 190
draw.polygon([(bx - 40, by - 20), (bx, by), (bx - 40, by + 20)], fill=bow_color)
draw.polygon([(bx + 40, by - 20), (bx, by), (bx + 40, by + 20)], fill=bow_color)
draw.ellipse([bx - 10, by - 10, bx + 10, by + 10], fill=(180, 60, 80))

img.save("girl_portrait.png")
print("Saved portrait to /mnt/user-data/outputs/girl_portrait.png")