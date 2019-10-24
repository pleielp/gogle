from django.db import models
from core.models import TimeStampedModel


class Edge(TimeStampedModel):
    dest = models.ForeignKey("Node", related_name="edge", on_delete=models.CASCADE)
    weight = models.IntegerField(blank=True, default=1)

class Node(TimeStampedModel):
    """
    Nodes(Website) Model Definition
    """
    url = models.URLField(primary_key=True)
    edges = models.ManyToManyField("Edge", related_name="src", blank=True)

    def __str__(self):
        return str(self.url)
    
class Keyword(models.Model):
    """
    Keyword Model Definition
    """
    keyword = models.CharField(max_length=100)

    def __str__(self):
        return str(self.keyword)

class Image(models.Model):
    """
    Image Model Definition
    """
    uri = models.URLField(primary_key=True)
    node = models.ForeignKey("Node", related_name="image", on_delete=models.CASCADE)
    keywords = models.ManyToManyField("Keyword", related_name="image", blank=True)

