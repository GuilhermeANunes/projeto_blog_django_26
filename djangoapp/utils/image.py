from PIL import Image
from pathlib import Path
from django.conf import settings

def resize_image(image_django, new_width=32, optimize=True, quality=60):
    image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()
    image_pillow = Image.open(image_path)
    original_width, original_heigth = image_pillow.size

    if original_width <= new_width:
        image_pillow.close()
        return image_pillow
    
    new_heigth = round(new_width * original_heigth / original_width)

    new_image = image_pillow.resize((new_width, new_heigth), Image.LANCZOS)
    new_image.save(
        image_path,
        optimize=optimize,
        quality=quality
    )

    return new_image