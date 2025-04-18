import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')  # Adjust if necessary

import django
django.setup()

from newsapp.models import Region, Sentiment, Category

categories = ["Politics", "Business", "Technology", "Sports", "Health"]

regions = ['INDIA', 'US']
for region_name in regions:
    region, created = Region.objects.get_or_create(name=region_name)

    sentiment_values = ['POS', 'NEG', 'NEU']
    
    for sentiment_name in sentiment_values:
        sentiment, created = Sentiment.objects.get_or_create(name=sentiment_name, region=region)

        for category_name in categories:
            Category.objects.get_or_create(name=category_name, sentiment=sentiment)

print("Categories added successfully for all regions and sentiments!")
