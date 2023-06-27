from PIL import Image


def resize_image(image_path):
    with Image.open(image_path) as img:
        img = img.resize((300, 300))
        img.save(image_path, optimize=True, quality=90)
