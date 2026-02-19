# ComputerStore

> **Work in Progress** — This project is under active development. APIs and structure may change.

[![Django](https://img.shields.io/badge/Django-5.0.1-092E20?logo=django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.x-8B0000)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)](https://www.sqlite.org/)

ComputerStore is a headless Django REST API backend for a computer (or generic retail) store. It exposes JSON endpoints for products, inventory, clients/companies, and invoices, intended for consumption by web, mobile, or POS frontends.

---

## Architecture Overview

| Layer        | Technology                          |
|-------------|--------------------------------------|
| Framework   | Django 5.x + Django REST Framework   |
| Database    | SQLite (default)                     |
| Style       | Headless, JSON-only API              |
| Project     | `ComputerStore`                      |

**Domain apps**

| App        | Purpose                                           |
|------------|---------------------------------------------------|
| `product`  | Product catalog, categories, category-driven specs |
| `inventory`| Stock quantities per product and location         |
| `invoice`  | Buy/sell invoices and line items                  |
| `client`   | Clients, companies, payments, financial summaries |

**URL prefixes:** `/product/`, `/inventory/`, `/invoice/`, `/client/`

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| **Product** | | |
| POST | `/product/` | Create a product with specifications |
| GET | `/product/category` | List all categories |
| GET | `/product/<category_name>` | List products by category name |
| **Inventory** | | |
| GET | `/inventory/` | List all inventory entries |
| **Invoice** | | |
| GET | `/invoice/` | List all buy invoices |
| POST | `/invoice/` | Create buy invoice with line items |
| GET | `/invoice/<id>` | Get line items for a buy invoice |
| GET | `/invoice/sell` | List all sell invoices |
| **Client** | | |
| GET | `/client/` | List client–company links |
| GET | `/client/Finance` | Per-company financial summaries (purchases, payments, balance) |

---

## Key Design Decisions

- **Abstract `Invoice` base** — `BuyInvoice` and `SellInvoice` inherit shared fields (`date`, `amount`); `BuyInvoice` links to `ClientCompanyLink`, `SellInvoice` has `sold` (PAID/UNPAID).
- **Category-driven specifications** — `Category.properties` (JSON list) defines attribute keys; `Product.specifications` (JSON dict) stores values. Categories control the schema without DB migrations.
- **`ClientCompanyLink` as central entity** — Links `Client` and `Company`; `BuyInvoice` and `Payment` reference it for supplier/customer context.
- **Stock as separate model** — `Inventory` holds quantity, location, and `minimum_quantity`; decoupled from invoices for custom stock logic.
- **Nested invoice creation** — `BuyInvoiceCreateSerializer` accepts `items` (product_id, price_buy, quantity) and computes total amount on save.
- **`DynamicFieldsModelSerializer`** — Shared base in `ComputerStore.SumplifySerializer` for controlling serialized fields.

---

## Getting Started

1. **Create and activate a virtual environment** (recommended).

2. **Install dependencies:**
   ```bash
   pip install django djangorestframework
   ```

3. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create superuser** (optional, for `/admin/`):
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the dev server:**
   ```bash
   python manage.py runserver
   ```

   API base: `http://127.0.0.1:8000/`

---

## Roadmap

Unimplemented or planned features based on current codebase:

| Feature | Status | Notes |
|---------|--------|-------|
| **Dashboard app** | Not wired | App exists, empty models; not in `INSTALLED_APPS` |
| **Report app** | Not wired | App exists, empty models; not in `INSTALLED_APPS` |
| **Expenses app** | Not wired | App exists, empty models; not in `INSTALLED_APPS` |
| **Product update/delete** | Missing | Only create and list by category |
| **Inventory write API** | Missing | GET only; no create/update/delete |
| **Client/Company CRUD** | Missing | GET only; no create/update/delete |
| **Invoice update/delete** | Missing | Create and read only |
| **Payment API** | Missing | `Payment` and `PaymentInvoiceLink` models exist; no endpoints |
| **Authentication** | Missing | No auth or permissions on API |
| **REST Framework in settings** | Partial | DRF used in views but not in `INSTALLED_APPS` |

---

## License

Not specified in codebase.
