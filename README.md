# &#9825; BagLuxe — Luxury Bag Shop

A Django luxury handbag e-commerce website with a soft pink and white theme targeting women and girls, selling iconic brands like Chanel, Dior, Hermès, Louis Vuitton, Gucci, Prada, Balenciaga, and Fendi.

Developed with AI assistance (Kiro), fully supervised, reviewed, and directed by me.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Tech Stack](#2-tech-stack)
3. [Project Structure](#3-project-structure)
4. [Installation & Setup](#4-installation--setup)
5. [Running the Project](#5-running-the-project)
6. [Admin Credentials](#6-admin-credentials)
7. [User Roles](#7-user-roles)
8. [Features](#8-features)
9. [Pages & URLs](#9-pages--urls)
10. [Email & Forgot Password](#10-email--forgot-password)
11. [Adding Products](#11-adding-products)
12. [Seeding Sample Data](#12-seeding-sample-data)
13. [Switching to MySQL](#13-switching-to-mysql)

---

## 1. Project Overview

BagLuxe is a full-featured luxury handbag online shop built with Django. It supports three levels of users — visitors, buyers, and sellers — each with different access levels. The design uses soft pink and white colors for an elegant, feminine feel.

---

## 2. Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.12 | Programming language |
| Django 6 | Web framework |
| SQLite | Database (built-in, no setup needed) |
| Bootstrap 5 | Frontend styling |
| Jazzmin | Beautiful Django admin theme |
| Pillow | Image handling |
| Pipenv | Virtual environment & dependency management |

---

## 3. Project Structure

```
BagLuxe/
├── bagluxe/                  # Project settings & URLs
│   ├── settings.py           # All configuration
│   └── urls.py               # Main URL routing
│
├── shop/                     # Main shop app
│   ├── models.py             # Brand, Product, Cart, Order models
│   ├── views.py              # All shop views
│   ├── urls.py               # Shop URLs
│   ├── admin.py              # Admin panel config
│   ├── context_processors.py # Cart count in navbar
│   └── management/
│       └── commands/
│           ├── seed_data.py             # Seeds brands & products
│           └── generate_placeholders.py # Generates product images
│
├── accounts/                 # User authentication app
│   ├── models.py             # Custom User model with roles
│   ├── views.py              # Register, login, logout, profile
│   ├── forms.py              # Auth forms
│   ├── urls.py               # Auth URLs + password reset
│   └── admin.py              # User admin config
│
├── templates/                # All HTML templates
│   ├── base.html             # Base layout (navbar, footer)
│   ├── admin/
│   │   └── base_site.html    # Admin branding override
│   ├── registration/
│   │   ├── password_reset_email.html   # Branded reset email
│   │   └── password_reset_subject.txt  # Email subject
│   ├── shop/
│   │   ├── home.html
│   │   ├── product_list.html
│   │   ├── product_detail.html
│   │   ├── brand_list.html
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   ├── order_list.html
│   │   ├── order_detail.html
│   │   └── seller_dashboard.html
│   └── accounts/
│       ├── login.html
│       ├── register.html
│       ├── profile.html
│       ├── password_reset.html
│       ├── password_reset_done.html
│       ├── password_reset_confirm.html
│       └── password_reset_complete.html
│
├── static/
│   └── css/
│       ├── style.css         # Main pink theme CSS
│       └── admin_custom.css  # Admin panel pink overrides
│
├── media/                    # Uploaded & generated images
│   └── products/             # Product SVG images
│
├── make_images.py            # Script to generate product images
├── Pipfile                   # Pipenv dependencies
└── README.md                 # This file
```

---

## 4. Installation & Setup

### Prerequisites
- Python 3.12+
- Pipenv installed (`pip install pipenv`)

### Steps

**1. Clone or open the project folder**

**2. Install dependencies**
```bash
pipenv install
```

**3. Apply database migrations**
```bash
pipenv run python manage.py migrate
```

**4. Seed sample brands and products**
```bash
pipenv run python manage.py seed_data
```

**5. Generate product placeholder images**
```bash
pipenv run python make_images.py
```

**6. Create admin account** (skip if already done)
```bash
pipenv run python manage.py createsuperuser
```

---

## 5. Running the Project

```bash
pipenv run python manage.py runserver
```

Then open your browser:

| Page | URL |
|------|-----|
| Homepage | http://127.0.0.1:8000/ |
| All Products | http://127.0.0.1:8000/products/ |
| Brands | http://127.0.0.1:8000/brands/ |
| Login | http://127.0.0.1:8000/accounts/login/ |
| Register | http://127.0.0.1:8000/accounts/register/ |
| Cart | http://127.0.0.1:8000/cart/ |
| My Orders | http://127.0.0.1:8000/orders/ |
| Seller Dashboard | http://127.0.0.1:8000/seller/dashboard/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

---

## 6. Admin Credentials

| Field | Value |
|-------|-------|
| Username | `admin` |
| Password | `admin123` |
| Role | Seller + Superadmin |

> **Important:** Change this password after first login at `/admin/`

---

## 7. User Roles

BagLuxe has 3 access levels:

### Visitor (no account)
- Browse all products and prices
- View product details and brands
- Cannot add to cart or checkout
- Sees "Login to Purchase" button on product pages

### Buyer (registered account)
- Everything a visitor can do
- Add products to cart
- Checkout and place orders
- View order history
- Update profile

To become a buyer: register at `/accounts/register/`

### Seller (admin)
- Everything a buyer can do
- Access the Seller Dashboard at `/seller/dashboard/`
- Full Django Admin Panel at `/admin/`
- Add, edit, delete products and brands
- Manage and update order statuses
- View all buyers and orders

To make someone a seller:
1. Go to `/admin/` → Users
2. Find the user → set `role = seller` and check `Staff status`
3. Save

---

## 8. Features

### Shop
- Homepage with featured products and new arrivals
- Filter products by brand, category, price (low/high), newest
- Search products by name or brand
- Product detail page with related products
- Brand listing page

### Cart & Orders
- Add to cart (buyers only)
- Update quantity or remove items
- Checkout with shipping address
- Order confirmation with order ID
- Full order history with status tracking

### Order Statuses
Pending → Processing → Shipped → Delivered → Cancelled
Updated by seller via admin panel.

### Accounts
- Register with name, email, phone, address
- Login / Logout
- Profile page with photo upload
- Forgot password via email (see section 10)

### Admin Panel (Jazzmin theme)
- Beautiful pink-themed admin UI
- Manage products, brands, categories
- Manage orders and update statuses
- Manage users and roles
- Quick links to shop from admin navbar

---

## 9. Pages & URLs

### Public (Visitor + Buyer + Seller)
| Page | URL |
|------|-----|
| Home | `/` |
| All Products | `/products/` |
| Filter by brand | `/products/?brand=chanel` |
| Filter by category | `/products/?category=tote-bag` |
| Search | `/products/?q=flap` |
| Product Detail | `/products/<slug>/` |
| Brands | `/brands/` |

### Auth
| Page | URL |
|------|-----|
| Register | `/accounts/register/` |
| Login | `/accounts/login/` |
| Logout | `/accounts/logout/` |
| Profile | `/accounts/profile/` |
| Forgot Password | `/accounts/password-reset/` |

### Buyer Only
| Page | URL |
|------|-----|
| Cart | `/cart/` |
| Checkout | `/checkout/` |
| My Orders | `/orders/` |
| Order Detail | `/orders/<order_id>/` |

### Seller Only
| Page | URL |
|------|-----|
| Seller Dashboard | `/seller/dashboard/` |
| Admin Panel | `/admin/` |

---

## 10. Email & Forgot Password

### How it works for the user
1. Click **"Forgot your password?"** on the login page
2. Enter email address
3. Receive a branded BagLuxe email with a reset button
4. Click the button → enter new password → done
5. Log in with the new password

### Setting up Gmail (to send real emails)

**Step 1:** Go to [myaccount.google.com](https://myaccount.google.com) → Security → enable **2-Step Verification**

**Step 2:** Search **"App passwords"** → create one → copy the 16-character code

**Step 3:** Open `bagluxe/settings.py` and update:
```python
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'abcdefghijklmnop'  # 16-char App Password, no spaces
DEFAULT_FROM_EMAIL = 'BagLuxe <youremail@gmail.com>'
```

**Step 4:** Save and restart the server. Done.

### Testing without Gmail (development)
Change `EMAIL_BACKEND` in `settings.py` to:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
The reset link will print in your terminal instead of being emailed.

---

## 11. Adding Products

### Via Admin Panel (recommended)
1. Go to `/admin/`
2. Click **Brands** → add your brand first
3. Click **Products** → Add Product
4. Fill in: name, brand, category, description, price, stock, image
5. Check **Is active** and optionally **Is featured**
6. Save

### Via Django Shell
```bash
pipenv run python manage.py shell
```
```python
from shop.models import Brand, Product
brand = Brand.objects.get(slug='chanel')
Product.objects.create(
    brand=brand,
    name='My New Bag',
    slug='my-new-bag',
    description='A beautiful bag.',
    price=3500.00,
    stock=5,
    is_active=True,
)
```

---

## 12. Seeding Sample Data

Rerun anytime to restore the 8 brands and 21 products:
```bash
pipenv run python manage.py seed_data
```

Regenerate product placeholder images:
```bash
pipenv run python make_images.py
```

Brands included: Chanel, Dior, Hermes, Louis Vuitton, Gucci, Prada, Balenciaga, Fendi

---

## 13. Switching to MySQL

Open `bagluxe/settings.py` and replace the database section:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bagluxe_db',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Install the MySQL driver:
```bash
pipenv install mysqlclient
```

Create the database in MySQL:
```sql
CREATE DATABASE bagluxe_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Run migrations:
```bash
pipenv run python manage.py migrate
pipenv run python manage.py seed_data
pipenv run python make_images.py
```

---

*BagLuxe &copy; 2026 — Elegance. Authenticity. You.*
