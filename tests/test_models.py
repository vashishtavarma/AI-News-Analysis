import pytest
from newsapp.models import Region, Sentiment, Category, NewsArticle
from django.db import IntegrityError

@pytest.mark.django_db
def test_region_str():
    region = Region(name="US")
    assert str(region) == "US"

@pytest.mark.django_db
def test_sentiment_str():
    region = Region(name="INDIA")
    sentiment = Sentiment(name="POS", region=region)
    sentiment.name = "POS"
    expected = f"Positive - {region.name}"
    assert str(sentiment) == expected

@pytest.mark.django_db
def test_category_str():
    region = Region(name="US")
    sentiment = Sentiment(name="NEG", region=region)
    category = Category(name="Politics", sentiment=sentiment)
    expected = f"Politics ({sentiment})"
    assert str(category) == expected

@pytest.mark.django_db
def test_newsarticle_str():
    region = Region(name="US")
    sentiment = Sentiment(name="NEU", region=region)
    category = Category(name="Tech", sentiment=sentiment)
    article = NewsArticle(title="Test Article", url="http://example.com", text="Some text", category=category)
    assert str(article) == "Test Article"

@pytest.mark.django_db
def test_unique_url_constraint():
    region = Region.objects.create(name="US")
    sentiment = Sentiment.objects.create(name="POS", region=region)
    category = Category.objects.create(name="Economy", sentiment=sentiment)
    NewsArticle.objects.create(title="A", url="http://dup.com", text="t", category=category)
    with pytest.raises(IntegrityError):
        NewsArticle.objects.create(title="B", url="http://dup.com", text="t2", category=category)
