from django.contrib import admin
from . import models as crawling_models
from django.utils.html import mark_safe

# Register your models here.


@admin.register(crawling_models.ImageLink)
class ImageLinkAdmin(admin.ModelAdmin):

    list_display = ("web_link", "img_link")

    def __str__(self):
        return self.name


@admin.register(crawling_models.Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="100px" src={obj.file.url}/>')
