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

## Deployment to Railway

### Step-by-Step Deployment

1. **Push your code to GitHub**
```bash
git init
git add .
git commit -m "Initial commit - MonarchTime watch store"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

2. **Deploy on Railway**
   - Go to [Railway.app](https://railway.app)
   - Sign up/Login with GitHub
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will automatically detect Django and deploy!

3. **Configure Environment Variables (Optional)**
   - In Railway dashboard, go to your project
   - Click on "Variables" tab
   - Add: `DEBUG=False` (for production)

4. **Access Your Site**
   - Railway will provide a URL like: `your-app.up.railway.app`
   - Visit it and your site is live! 🎉

### ✅ What Works on Railway

- ✅ Add products from mobile/desktop
- ✅ Upload images (they persist!)
- ✅ SQLite database (or upgrade to PostgreSQL)
- ✅ All CRUD operations work perfectly
- ✅ Static files served automatically
- ✅ Media files stored persistently

### Important Notes

- Railway provides 500 hours/month free tier
- Your SQLite database persists across deployments
- Uploaded images are stored in the `/media` folder
- No need for external storage services (S3, Cloudinary) for basic usage

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
