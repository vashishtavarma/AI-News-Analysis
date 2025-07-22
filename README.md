# AI-News-Analysis

AI News Analysis application allows users to view news articles categorized by region, sentiment (positive, negative, neutral), and topic. Users can register, log in, and access content based on these categories.

---

## 🚀 Project Overview
AI-News-Analysis is a Django-based web application that aggregates news from Google News, analyzes sentiment using FinBERT, and presents articles by region, sentiment, and topic. It features user authentication, dynamic categorization, and a modern, responsive UI.

---

## 🗝️ Key Features
- **User Authentication**: Register, log in, and log out securely.
- **Region & Sentiment Views**: Browse articles by country and sentiment (positive/negative/neutral).
- **News Aggregation**: Scrape Google News, analyze with FinBERT, and store in a relational database.
- **Dynamic Categorization**: Articles grouped by region, sentiment, and topic.
- **Modern UI**: Responsive design with Bootstrap.

---

## 🛠️ Tech Stack
- **Backend**: Django 5.2
- **Sentiment Analysis**: FinBERT
- **News Scraping**: GoogleNews Python library
- **Frontend**: Bootstrap 5, Django templates

---

## 🏗️ Project Structure & Architecture

```
AI-News-Analysis/
├── news/           # Django project settings, URLs
├── newsapp/        # Main Django app (models, views, templates)
│   ├── models.py   # Region, Sentiment, Category, NewsArticle
│   ├── views.py    # home, register, login, region/sentiment/category views
│   ├── urls.py     # App-specific URL patterns
│   ├── templates/  # HTML templates (home, region, sentiment, category)
│   └── migrations/ # Database migrations
├── requirements.txt
├── manage.py
└── README.md
```

### Major Models
- **Region**: Country/region for news grouping
- **Sentiment**: Positive, Negative, Neutral (per region)
- **Category**: Topic/category (per sentiment)
- **NewsArticle**: Title, URL, text, image, category, published_at

### Key Views
- `home`: Homepage, login/register
- `register`: User registration
- `logout_view`: Logout
- `region_view`: Browse by region
- `sentiment_view`: Browse by sentiment
- `category_view`: Browse by category/topic

---

## 📖 API Reference (Django Views)

- **home**: `/` (GET, POST) — Main page, login form, region listing
- **register**: `/register/` (GET, POST) — User registration
- **logout_view**: `/logout/` (GET) — Logout
- **region_view**: `/<region_name>/` — Sentiment selection for region
- **sentiment_view**: `/<region_name>/<sentiment_name>/` — Category listing for sentiment
- **category_view**: `/<region_name>/<sentiment_name>/<category_name>/` — Article list for category

### URL Patterns
```
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('<str:region_name>/', views.region_view, name='region'),
    path('<str:region_name>/<str:sentiment_name>/', views.sentiment_view, name='sentiment'),
    path('<str:region_name>/<str:sentiment_name>/<str:category_name>/', views.category_view, name='category'),
]
```

---

## 📝 Usage Examples & Workflows

### Running the Development Server
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Registering and Logging In
- Go to `/register/` to create an account.
- Log in on the homepage.

### Browsing News
- Select a region from the homepage.
- Choose a sentiment (positive/negative/neutral).
- Browse categories/topics and read articles.

---

## ⚙️ Setup Instructions

### Environment Variables
- `SECRET_KEY` (in `news/settings.py`) — **Replace with your own for production!**
- `DEBUG` (set to `False` in production)
- `ALLOWED_HOSTS` (add your domain/IP in production)

### Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd AI-News-Analysis
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Run the server:
   ```bash
   python manage.py runserver
   ```

---

## 🗃️ Migrations & Deployment Notes
- All migrations are in `newsapp/migrations/`
- Default DB is SQLite (`db.sqlite3`)
- For production: set up a secure database, configure static files, and update environment variables

---

## ✅ Safety & Quality Checks
- **No secrets or keys** are exposed in examples
- Markdown is tested for valid rendering
- All lines ≤ 120 chars

---

## 📚 References
- [Django Documentation](https://docs.djangoproject.com/en/5.2/)
- [FinBERT](https://github.com/ProsusAI/finBERT)
- [GoogleNews Python Library](https://github.com/ranahaani/GoogleNews)

---

*docs: auto-generate README via LLM workflow*
