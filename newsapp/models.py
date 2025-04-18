from django.db import models

SENTIMENT_CHOICES = [
    ('POS', 'Positive'),
    ('NEG', 'Negative'),
    ('NEU', 'Neutral'),
]

REGION_CHOICES = [
    ('US', 'US'),
    ('INDIA', 'India'),
]

class Region(models.Model):
    name = models.CharField(max_length=20, choices=REGION_CHOICES, unique=True)

    def __str__(self):
        return self.name

class Sentiment(models.Model):
    name = models.CharField(max_length=3, choices=SENTIMENT_CHOICES)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='sentiments')

    def __str__(self):
        return f"{self.get_name_display()} - {self.region.name}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    sentiment = models.ForeignKey(Sentiment, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return f"{self.name} ({self.sentiment})"

class NewsArticle(models.Model):
    title = models.CharField(max_length=500)
    url = models.URLField(unique=True)
    text = models.TextField()
    top_image = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    published_at = models.DateTimeField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
