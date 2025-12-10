# MonarchTime - Luxury Watch Store

A modern Django-based e-commerce platform for luxury watches with a beautiful, responsive UI.

## Features

- 🎨 Modern UI with Bootstrap 5 and Tailwind CSS
- 📱 Fully responsive design (mobile-first)
- 🔄 Auto-reload during development
- 🖼️ Image upload for products
- 💾 SQLite database
- 🎯 Product management (CRUD operations)
- 🎭 Beautiful hero sections and cards

## Tech Stack

- **Backend:** Django 6.0
- **Frontend:** Bootstrap 5.3.2 + Tailwind CSS
- **Database:** SQLite3
- **Image Processing:** Pillow
- **Dev Tools:** django-browser-reload

## Local Development

### Prerequisites

- Python 3.9+
- pip

### Setup

1. Clone the repository
```bash
git clone <your-repo-url>
cd Project
```

2. Create and activate virtual environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Create a superuser (optional)
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000

## Deployment to Vercel

### Via GitHub

1. Push your code to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

2. Go to [Vercel](https://vercel.com)
3. Click "New Project"
4. Import your GitHub repository
5. Vercel will automatically detect the configuration from `vercel.json`
6. Click "Deploy"

### Important Notes for Vercel Deployment

- The `vercel.json` file is already configured
- Static files will be collected automatically during build
- Media files are stored locally (consider using cloud storage like AWS S3 for production)
- The database is SQLite (consider using PostgreSQL for production)

### Environment Variables (Optional)

For production, consider setting these in Vercel:
- `SECRET_KEY`: Your Django secret key
- `DEBUG`: Set to `False` in production

## Project Structure

```
Project/
├── Project/          # Django project settings
├── Store/            # Main app
│   ├── models.py     # Product model
│   ├── views.py      # Views
│   ├── forms.py      # Forms
│   └── urls.py       # URL routing
├── templates/        # HTML templates
│   ├── base.html     # Base template with navbar/footer
│   ├── home.html     # Homepage
│   ├── about.html    # About page
│   ├── products.html # Products listing
│   └── add_product.html # Add product form
├── static/           # Static files (CSS, JS, images)
├── media/            # User uploaded files
└── manage.py         # Django management script
```

## Pages

- **Home** - Hero section with call-to-action
- **About** - Company information and values
- **Products** - Product catalog with responsive cards
- **Add Product** - Form to add new products
- **Admin** - Django admin panel at `/admin`

## License

MIT License

## Author

MonarchTime Team
