# AI-News-Analysis

AI News Analysis application allows users to view news articles categorized by region, sentiment (positive, negative, neutral), and topic. Users can register, log in, and access content based on these categories.

## Key Features
- **User Authentication**: Register, log in, and log out securely.
- **Region & Sentiment Views**: Browse articles by country and sentiment (positive, negative, neutral).
- **News Aggregation**: Articles are scraped from Google News, analyzed for sentiment using FinBERT, and stored in the database.
- **Dynamic Categorization**: News is dynamically categorized by topic and sentiment.

## Tech Stack
- **Django 5.2** (Backend framework)
- **FinBERT** (Sentiment analysis)
- **GoogleNews Python library** (News scraping)
- **Pytest** (Testing)

## Architecture
- **Django Project Structure**: Main app is `newsapp`.
- **Models**: `Region`, `Sentiment`, `Category`, `NewsArticle`.
- **Data Flow**: News articles are fetched, analyzed with FinBERT, categorized, and stored in the database. Users interact via views and templates.
- **Authentication**: Uses Django's built-in user model with custom registration/login views.

## API Reference
- `/` : Home (login/region listing)
- `/register/` : Register new user
- `/logout/` : Logout
- `/<region>/` : Browse news by region
- `/<region>/<sentiment>/` : Browse by region & sentiment
- `/<region>/<sentiment>/<category>/` : Browse by region, sentiment & category

## Usage Examples
- **Register**: Go to `/register/` and fill the form.
- **Login**: Use your email and password on the home page.
- **Browse**: Click on a region, then select sentiment and category to view articles.

## Setup Instructions
1. **Clone the repository**
   ```sh
   git clone https://github.com/vashishtavarma/AI-News-Analysis.git
   cd AI-News-Analysis
   ```
2. **Create and activate a virtual environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply migrations**
   ```sh
   python manage.py migrate
   ```
5. **Create superuser**
   ```sh
   python manage.py createsuperuser
   ```
6. **Add initial categories/regions**
   ```sh
   python addcat.py
   ```
7. **Populate news articles**
   ```sh
   python datatodb.py
   ```
8. **Run the server**
   ```sh
   python manage.py runserver
   ```

## Migration Notes
- Use `python manage.py makemigrations` and `python manage.py migrate` for schema changes.
- Use `addcat.py` to initialize categories for all regions/sentiments.
- Use `datatodb.py` to fetch and analyze news articles for all categories.

## Testing
- Tests are written with `pytest` and are located in the `tests/` directory.
- To run tests:
   ```sh
   pytest --maxfail=3 --disable-warnings -v tests/
   ```

## References
- [Django Documentation](https://docs.djangoproject.com/en/5.2/)
- [FinBERT (ProsusAI)](https://huggingface.co/ProsusAI/finbert)
- [GoogleNews Python Library](https://pypi.org/project/GoogleNews/)

---
For questions or contributions, please open an issue or pull request on GitHub.
