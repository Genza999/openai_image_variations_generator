import openai
from django.conf import settings


def open_ai_image_variations(image):
    """Create variations of the uploaded image."""
    # Since its an InMemoryFile
    image_byte_object = image.file
    image_byte_stream = image_byte_object.getvalue()

    openai.api_key = settings.API_KEY
    response = openai.Image.create_variation(
        image=image_byte_stream,
        n=settings.VARIATIONS_NUMBER,  # Generate 3 variations of the uploaded image
        size=f"{settings.IMAGE_SIZE}x{settings.IMAGE_SIZE}",
    )
    return response["data"]
