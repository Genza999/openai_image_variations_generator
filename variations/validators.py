import os
import magic
from django.core.exceptions import ValidationError


def validate_image_file(file):
    """Validate that the file is a png image."""
    valid_mime_types = ["image/png"]
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    if file_mime_type not in valid_mime_types:
        raise ValidationError("Unsupported file type.")

    valid_file_extensions = [".png"]
    ext = os.path.splitext(file.name)[1]

    if ext.lower() not in valid_file_extensions:
        raise ValidationError("Unacceptable file extension.")
