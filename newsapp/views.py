from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Region, Sentiment, Category, NewsArticle
from django.contrib.auth.decorators import login_required

def home(request):
    regions = Region.objects.all()
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been logged in!")
                return redirect('home')
            else:
                messages.error(request, "Invalid email or password!")
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password!")
    
    context = {
        'regions': regions,
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Account created successfully! You can log in now.")
        return redirect('home')

    return render(request, 'register.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')

@login_required
def region_view(request, region_name):
    region = get_object_or_404(Region, name=region_name.upper())
    sentiments = Sentiment.objects.filter(region=region)
    
    context = {
        'region': region,
        'sentiments': sentiments,
    }
    return render(request, 'region.html', context)

login_required
def sentiment_view(request, region_name, sentiment_name):
    region = get_object_or_404(Region, name=region_name.upper())
    
    sentiment_map = {'positive': 'POS', 'negative': 'NEG', 'neutral': 'NEU'}
    sentiment_code = sentiment_map.get(sentiment_name.lower())
    
    sentiment = get_object_or_404(Sentiment, region=region, name=sentiment_code)
    categories = Category.objects.filter(sentiment=sentiment)
    
    context = {
        'region': region,
        'sentiment': sentiment,
        'categories': categories,
    }
    return render(request, 'sentiment.html', context)


@login_required
def category_view(request, region_name, sentiment_name, category_name):
    region = get_object_or_404(Region, name=region_name.upper())
    
    sentiment_map = {'positive': 'POS', 'negative': 'NEG', 'neutral': 'NEU'}
    sentiment_code = sentiment_map.get(sentiment_name.lower())
    
    sentiment = get_object_or_404(Sentiment, region=region, name=sentiment_code)
    category = get_object_or_404(Category, sentiment=sentiment, name__iexact=category_name)
    articles = NewsArticle.objects.filter(category=category).order_by('-published_at')
    
    context = {
        'region': region,
        'sentiment': sentiment,
        'category': category,
        'articles': articles,
    }
    return render(request, 'category.html', context)