from django.shortcuts import render

from .forms import UploadImageForm
from variations.utils import open_ai_image_variations


def upload_image_page(request):
    """View function for the home page to upload image."""
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            response = open_ai_image_variations(request.FILES["image"])
            return render(
                request,
                "upload_image_page.html",
                context={"images": response},
            )
    else:
        form = UploadImageForm()
    return render(request, "upload_image_page.html", {"form": form})
