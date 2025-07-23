import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from newsapp.models import Region, Sentiment, Category, NewsArticle

@pytest.mark.django_db
def test_home_view_authenticated(client, django_user_model):
    user = django_user_model.objects.create_user(username="test", email="t@t.com", password="pass")
    client.login(username="test", password="pass")
    response = client.get(reverse("home"))
    assert response.status_code == 200
    assert b"News Analysis Application" in response.content

@pytest.mark.django_db
def test_home_view_unauthenticated(client):
    response = client.get(reverse("home"))
    assert response.status_code == 200
    assert b"News Analysis Application" in response.content

@pytest.mark.django_db
def test_register_view_post_password_mismatch(client):
    data = {"username": "user1", "email": "a@a.com", "password": "pass1", "confirm_password": "pass2"}
    response = client.post(reverse("register"), data)
    assert response.status_code == 302

@pytest.mark.django_db
def test_register_view_post_success(client):
    data = {"username": "user2", "email": "b@b.com", "password": "pass", "confirm_password": "pass"}
    response = client.post(reverse("register"), data)
    assert response.status_code == 302
    assert User.objects.filter(username="user2").exists()

@pytest.mark.django_db
def test_logout_view(client, django_user_model):
    user = django_user_model.objects.create_user(username="test2", email="test2@t.com", password="pass")
    client.login(username="test2", password="pass")
    response = client.get(reverse("logout"))
    assert response.status_code == 302

@pytest.mark.django_db
def test_region_view(client):
    region = Region.objects.create(name="US")
    Sentiment.objects.create(name="POS", region=region)
    user = User.objects.create_user(username="u", email="u@u.com", password="pass")
    client.login(username="u", password="pass")
    response = client.get(reverse("region", args=["us"]))
    assert response.status_code == 200
    assert b"US" in response.content

@pytest.mark.django_db
def test_sentiment_view(client):
    region = Region.objects.create(name="US")
    sentiment = Sentiment.objects.create(name="POS", region=region)
    user = User.objects.create_user(username="u2", email="u2@u.com", password="pass")
    client.login(username="u2", password="pass")
    response = client.get(reverse("sentiment", args=["us", "positive"]))
    assert response.status_code == 200
    assert b"Positive" in response.content

@pytest.mark.django_db
def test_category_view(client):
    region = Region.objects.create(name="US")
    sentiment = Sentiment.objects.create(name="POS", region=region)
    category = Category.objects.create(name="Economy", sentiment=sentiment)
    NewsArticle.objects.create(title="T", url="http://a.com", text="body", category=category)
    user = User.objects.create_user(username="u3", email="u3@u.com", password="pass")
    client.login(username="u3", password="pass")
    response = client.get(reverse("category", args=["us", "positive", "economy"]))
    assert response.status_code == 200
    assert b"Economy" in response.content
