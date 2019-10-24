from django.contrib import admin
from . import models as crawling_models
from django.utils.html import mark_safe

@admin.register(crawling_models.Edge)
class EdgeAdmin(admin.ModelAdmin):
    list_display = ("weight", "get_dest_name")
    def get_dest_name(self, obj):
        return str(obj.dest.url)

@admin.register(crawling_models.Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ("url", "edge_count")
    def edge_count(self, obj):
        return obj.edges.count()
    

@admin.register(crawling_models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("uri", "keyword_list", "get_image")
    def keyword_list(self,obj):
        return ", ".join(map(str, obj.keywords.all()))

    def get_image(self, obj):
        return mark_safe(f'<img width="100px" src=\'{obj.uri}\'>')

@admin.register(crawling_models.Keyword)
class KeywordAdmin(admin.ModelAdmin):

    list_display = ("keyword", "image_list")

    def image_list(self, obj):
        return obj.image.all()

# @admin.register(crawling_models.Image)
# class ImageAdmin(admin.ModelAdmin):

#     list_display = ("__str__", "get_thumbnail")

#     def get_thumbnail(self, obj):
#         return mark_safe(f'<img width="100px" src={obj.file.url}/>')
