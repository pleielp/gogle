from django.contrib import admin
from . import models as crawling_models

# Register your models here.


@admin.register(crawling_models.ImageLink)
class ImageLinkAdmin(admin.ModelAdmin):

    display_list = ["web_link", "img_link"]


@admin.register(crawling_models.Image)
class ImageAdmin(admin.ModelAdmin):

    pass
