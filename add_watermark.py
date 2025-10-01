from PIL import Image, ImageDraw, ImageFont
from random import randint, uniform, gauss, choice, shuffle
import os


FONTS = os.listdir("/usr/share/fonts/truetype/freefont/")


def make_watermark_pattern(image, text="sample", font_path=None, background=(255, 255, 255, 0)):
    if uniform(0, 1) > 0.5:
        text = text.upper()
    if len(FONTS) > 0:
        font_path = os.path.join("/usr/share/fonts/truetype/freefont/", choice(FONTS))
    image = image.convert("RGBA")
    font_size = int(gauss(25, 5))
    if uniform(0, 1) > 0.9:
        font_size += randint(1, 100)
    angle = randint(-60, 60)
    text_color = (randint(0, 255), randint(0, 255), randint(0, 255), randint(170, 255))

    # Choose font
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default(font_size)

    # Draw text in the center
    bbox = font.getbbox(text)
    w = bbox[2] - bbox[0]  # right - left
    h = bbox[3] - bbox[1]  # bottom - top

    tile_size = (w + randint(0, 50), h + randint(0, 50))
    empty_space_w, empty_space_h = tile_size[0] - w, tile_size[1] - h
    # Create tile image
    tile = Image.new("RGBA", tile_size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(tile)

    x = (tile_size[0] - w) // 2
    y = (tile_size[1] - h) // 2
    draw.text((x, y), text, fill=text_color, font=font)

    # Rotate tile
    tile = tile.rotate(angle, expand=True)

    # Create base image
    base = Image.new("RGBA", image.size, background)
    count = 0

    # Paste tile repeatedly to fill base
    min_w, max_w = empty_space_w, image.size[0] - randint(5, 20) - empty_space_w
    min_h, max_h = empty_space_h, image.size[1] - randint(5, 20) - empty_space_h
    for i in range(min_w, max_w, tile.size[0]):
        for j in range(min_h, max_h, tile.size[1]):
            if uniform(0, 1) < 0.9:
                base.paste(tile, (i, j), tile)
                count += 1
    # composite overlay onto original
    out = Image.alpha_composite(image, base)
    out = out.convert("RGB")
    return out, count
