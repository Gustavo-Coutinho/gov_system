from django.db import models
from .utils import get_filtered_image
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
from django.contrib.auth.models import User

# Create your models here.

class Biometry(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user.username)

    def save(self, *args, **kwargs):
        # open image
        pil_img = Image.open(self.image)

        # convert image to array in order to process it
        image_as_array = np.array(pil_img)
        img = get_filtered_image(image_as_array)


        # convert back to pil image
        array_back_to_image = Image.fromarray(img)

        # save
        buffer = BytesIO()
        array_back_to_image.save(buffer, format='png')
        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png), save=False)

        super().save(*args, **kwargs)