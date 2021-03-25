from django.db import models
from urllib.request import urlopen 
import json 

# Create your models here.
class Article(models.Model):
    arXiv = models.CharField(max_length=15, blank=True, unique=True)
    title = models.CharField(max_length=200, blank=True)
    year = models.PositiveSmallIntegerField(default=0)
    journal = models.CharField(max_length=25, blank=True)
    volume = models.CharField(max_length=10, blank=True)
    page = models.CharField(max_length=10, blank=True)
    author = models.CharField(max_length=30, blank=True)
    collaboration = models.CharField(max_length=30, blank=True)
    doi = models.CharField(max_length=60, blank=True)
    bibtex = models.TextField(blank=True)
    citation_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-year', '-arXiv']

    def __str__(self):
        return f'arXiv:{self.arXiv}'
    

    def save(self, *args, **kwargs):
        # print(self.arXiv, self.title)
        data = self.fetchData()['metadata']
        self.title = data['titles'][0]['title']
        self.citation_count = data['citation_count']
        self.doi = data.get('dois', [{}])[0].get('value', '')
        self.author = data['authors'][0]['full_name']
        col_list = []
        for c in data.get('collaborations', []):
            col_list.append(c['value'])
        self.collaboration = ', '.join(col_list)

        try:
            publication = data['publication_info'][0]
            self.year = publication['year']
            self.journal = publication['journal_title']
            self.volume = publication['journal_volume']
            try:
                self.page = publication['artid']
            except KeyError:
                self.page = publication['page_start']
        except KeyError:
            self.year = data['preprint_date'].split('-')[0]
            

        super(Article, self).save(*args, **kwargs)
    
    def fetchData(self):
        url = f'https://inspirehep.net/api/arxiv/{self.arXiv}'
        with urlopen(url) as f:
            data = json.loads(f.read().decode())
        return data
