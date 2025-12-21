# MonarchTime - Luxury Watch Store Project Documentation

## 1. Project Overview
**Project Name:** MonarchTime
**Description:** A Django-based web application designed for a luxury watch store. The system serves as a digital catalog and management platform, allowing users to browse a collection of timepieces and administrators/staff to manage the inventory by adding new products.

## 2. Technical Stack
The project is built using modern web technologies to ensure robustness and a premium user interface.

### Backend
- **Language:** Python
- **Framework:** Django (Web Framework)
- **Database:** SQLite (Lightweight, file-based database)

### Frontend
- **Templating:** Django Template Language (DTL)
- **Styling:**
  - **Tailwind CSS:** For utility-first, responsive design.
  - **Bootstrap 5:** For pre-built components and layout.
  - **Google Fonts:** Uses 'Playfair Display' for headings (luxury feel) and 'Inter' for body text.

### Key Libraries
- **Whitenoise:** For efficient static file serving.
- **Django Browser Reload:** For improved development experience (hot reloading).
- **Pillow:** For handling image uploads and processing.

## 3. Features
1.  **Home Page:** A landing page introducing the brand.
2.  **Product Catalog:** A dynamically generated list of all available watches, sorted by newest arrivals.
    - Displays product image, title, and price.
    - "View Details" action.
3.  **Product Management (Add Product):**
    - Secure form to upload new inventory.
    - Fields: Title, Description, Image Upload, Price.
    - Validation and success messages upon completion.
4.  **About Page:** Information about the brand's history and values.
5.  **Admin Dashboard:** Built-in Django admin interface for advanced database management (filtering, searching, and editing records).
6.  **Responsive Design:** Fully optimized for mobile, tablet, and desktop devices.

## 4. Database Schema
The core data structure is defined in the `Store` application.

### Model: `Product`
| Field Name | Type | Description |
|------------|------|-------------|
| `title` | CharField | Name of the watch (max 200 chars). |
| `description`| TextField | Detailed information about the product. |
| `image` | ImageField | Upload path for product photography (`products/`). |
| `price` | DecimalField | Price of the watch (supports 2 decimal places). |
| `created_at` | DateTimeField | Automatically records when the product was added. |

## 5. Project Structure
```
Project/
├── db.sqlite3          # Database file
├── manage.py           # Command-line utility
├── Project/            # Project configuration
│   ├── settings.py     # Main settings (Apps, DB, Static files)
│   ├── urls.py         # Main URL routing
│   └── wsgi.py         # Web Server Gateway Interface
├── Store/              # Main application logic
│   ├── admin.py        # Admin site configuration
│   ├── models.py       # Database models
│   ├── views.py        # Request handlers
│   └── forms.py        # Form definitions
└── templates/          # HTML Templates
    ├── base.html       # Master layout (Navbar, Footer)
    ├── home.html       # Home page
    ├── products.html   # Catalog page
    └── add_product.html# Product entry form
```

## 6. Installation & Setup Guide
Follow these steps to run the project on a local machine.

### Prerequisites
- Python 3.x installed.

### Steps
1.  **Navigate to the project directory:**
    ```bash
    cd E:\python\Project
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv .venv
    ```

3.  **Activate the Virtual Environment:**
    - Windows: `.venv\Scripts\activate`

4.  **Install Dependencies:**
    (Ensure you have `django`, `pillow`, `whitenoise`, `django-browser-reload` installed)
    ```bash
    pip install django pillow whitenoise django-browser-reload
    ```

5.  **Run Migrations (Setup Database):**
    ```bash
    python manage.py migrate
    ```

6.  **Create Admin User (Optional):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```

8.  **Access the Application:**
    - Website: `http://127.0.0.1:8000/`
    - Admin Panel: `http://127.0.0.1:8000/admin/`

## 7. Future Enhancements
- **User Authentication:** Allow customers to sign up and log in.
- **Shopping Cart:** Enable purchasing functionality.
- **Payment Gateway:** Integration with Stripe or PayPal.
- **Product Details View:** A dedicated page for individual product specs.
