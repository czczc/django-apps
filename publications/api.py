from .models import Article
from rest_framework import serializers, viewsets

# Serializers define the API representation.
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id', 
            'arXiv', 
            'title', 
            'year', 
            'journal', 
            'volume',
            'page',
            'author',
            'collaboration',
            'doi',
            'citation_count',
            'url'
        ]


# ViewSets define the view behavior.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer