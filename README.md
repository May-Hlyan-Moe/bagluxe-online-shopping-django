# BagLuxe - Luxury Bag Shop

A Django-based luxury handbag e-commerce website with soft pink theme.

## Admin Credentials

| Role | Username | Password | Access |
|------|----------|----------|--------|
| Seller / Superadmin | `admin` | `admin123` | Full admin panel + seller dashboard |

> Change the password after first login via `/admin/`

## Run the Project

```bash
pipenv run python manage.py runserver
```

Then open: http://127.0.0.1:8000

- Shop: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/
- Seller dashboard: http://127.0.0.1:8000/seller/dashboard/

## User Roles

| Role | How to get it | Access |
|------|--------------|--------|
| Visitor | No account needed | Browse all products & prices |
| Buyer | Register at `/accounts/register/` | Cart, checkout, order history |
| Seller | Set by admin in `/admin/` (role = seller, is_staff = true) | Seller dashboard + admin panel |

## Seed Sample Data

```bash
pipenv run python manage.py seed_data
```

## Create Another Seller

```bash
pipenv run python manage.py createsuperuser
```

Then in `/admin/` set their role to `seller` and check `is_staff`.
