from django.db import models

# Create your models here.


class Image(models.Model):
    """ Image Model Definition """

    file = models.ImageField(upload_to="images/")


class ImageLink(models.Model):
    """ ImageLinks Model Definition"""

    web_link = models.URLField()
    img_link = models.URLField()
    img_path = models.ForeignKey(
        "Image", null=True, on_delete=models.CASCADE, blank=True
    )

