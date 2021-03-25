from django.db import models

# Create your models here.
class Article(models.Model):
    arXiv = models.CharField(max_length=15, blank=True)
    title = models.CharField(max_length=200, blank=True)
    year = models.PositiveSmallIntegerField(default=0)
    journal = models.CharField(max_length=25, blank=True)
    volume = models.CharField(max_length=10, blank=True)
    page = models.CharField(max_length=10, blank=True)
    author = models.CharField(max_length=30, blank=True)
    collaboration = models.CharField(max_length=30, blank=True)
    doi = models.CharField(max_length=30, blank=True)
    bibtex = models.TextField(blank=True)
    citation_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'arXiv:{self.arXiv}'