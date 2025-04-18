from django.contrib import admin
from .models import Region, Sentiment, Category, NewsArticle

admin.site.register(Region)
admin.site.register(Sentiment)
admin.site.register(Category)
admin.site.register(NewsArticle)
