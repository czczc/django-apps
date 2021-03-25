from django.contrib import admin

# Register your models here.

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('arXiv', 'title', 'journal', 'collaboration', 'year', 'citation_count')

admin.site.register(Article, ArticleAdmin)