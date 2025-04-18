import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')

import django
django.setup()

from newsapp.models import Category, NewsArticle
from GoogleNews import GoogleNews
from transformers import pipeline

import pytz

NewsArticle.objects.all().delete()
print("🧹 All existing NewsArticles deleted.")

print("Loading FinBERT sentiment model...")
pipe = pipeline("text-classification", model="ProsusAI/finbert")
print("✅ Sentiment model ready!")

timezone = pytz.timezone('Asia/Kolkata')

for category in Category.objects.all():
    print(f"\n▶️ Populating: {category}...")

    fetched = 0
    seen_links = set()

    region_code = 'IN' if category.sentiment.region.name == 'INDIA' else 'US'
    googlenews = GoogleNews(lang='en', region=region_code, period='1d')
    googlenews.clear()
    googlenews.search(category.name)
    results = googlenews.results()

    for r in results:
        if fetched >= 10:
            break
        

        if not r['desc'] or r['link'] in seen_links:
            continue

        seen_links.add(r['link'])

        try:
            sentiment_result = pipe(r['desc'])[0]['label']
        except Exception as e:
            print("⛔ Sentiment analysis error:", e)
            continue

        sentiment_label = sentiment_result.upper()
        if sentiment_label[0:3] != category.sentiment.name:
            continue  

        try:
            published_at = r['datetime']
            if published_at:
                published_at = timezone.localize(published_at)
        except Exception:
            published_at = None

        try:
            article, created = NewsArticle.objects.get_or_create(
                url=r['link'],
                defaults={
                    'title': r['title'],
                    'text': r['desc'],
                    'top_image': r['img'],
                    'category': category,
                    'published_at': published_at
                }
            )
            if created:
                fetched += 1
                print(f"✅ [{fetched}/10] Added: {article.title}")
        except Exception as e:
            print("⛔ Database error:", e)
            continue

print("\n✅ All categories populated with up to 10 matching articles.")
