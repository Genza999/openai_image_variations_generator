from django import forms

from variations.validators import validate_image_file


class UploadImageForm(forms.Form):
    image = forms.FileField(label="", validators=[validate_image_file])
