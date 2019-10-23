from django.db import models
from core.models import TimeStampedModel


class Image(models.Model):
    """ Image Model Definition """

    file = models.ImageField(upload_to="images/")

    def __str__(self):
        return str(self.file)


class ImageLink(TimeStampedModel):
    """ ImageLinks Model Definition"""

    web_link = models.URLField()
    img_link = models.URLField()
    img_path = models.ForeignKey(
        "Image", null=True, on_delete=models.CASCADE, blank=True
    )

