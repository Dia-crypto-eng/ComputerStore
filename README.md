## ComputerStore Headless Backend

ComputerStore is a **headless Django REST API** that provides the core backend for a computer store (or generic retail) system.  
It exposes JSON endpoints for managing **products**, **stock (inventory)**, **clients/companies**, and **invoices**, and is designed to be consumed by independent frontends (web, mobile, POS, etc.).

---

## Architecture Overview

- **Framework**: Django 5.x + Django REST Framework
- **Database**: SQLite (can be swapped for PostgreSQL/MySQL)
- **Style**: Headless, JSON-only API (no templates rendered)
- **Project module**: `ComputerStore`
- **Domain apps**:
  - `product` – product catalog and category-based specifications
  - `inventory` – stock quantities per product and location
  - `invoice` – purchase and sales invoices with line items
  - `client` – clients, companies, payments, and financial summaries

The project URL configuration (`ComputerStore/urls.py`) mounts all app routes under logical prefixes:

- `/product/…`
- `/inventory/…`
- `/invoice/…`
- `/client/…`

---

## Database Models (Core Domain)

### Product & Category (`product` app)

**Category**
- `id` (implicit, auto)
- `name`: `CharField` – unique category name
- `properties`: `JSONField` – list of attribute keys for products in this category (e.g. `["RAM", "Storage", "CPU"]`)

**Product**
- `idProduct`: `AutoField` – primary key
- `name`: `CharField`
- `mark`: `CharField` – brand/mark
- `category`: `ForeignKey(Category)` – category this product belongs to
- `specifications`: `JSONField` – key–value pairs for attributes defined by the category

The **specifications logic** is driven by the category:

- Each `Category` defines a list of attribute keys in `properties`.
- When creating or updating a `Product`, the backend:
  - Takes the input `specifications` dict from the request.
  - Normalizes keys (e.g. capitalization).
  - Builds a new `specifications` JSON where all category-defined keys exist (missing ones default to empty strings).

This gives a flexible schema where:

- Categories control the shape of product attributes.
- Different categories can have different sets of specification keys.

### Inventory / Stock (`inventory` app)

**Inventory**
- `id`: `AutoField` – primary key
- `product`: `ForeignKey(Product)` – product being stocked
- `quantity`: `PositiveIntegerField` – current quantity in stock
- `location`: `CharField` (optional) – store/warehouse location
- `minimum_quantity`: `PositiveIntegerField` – threshold for low-stock alerts (business logic can be added on top)

This app models **stock** as a separate entity from invoices, making it possible to:

- Track stock per product and per location.
- Build custom stock movement logic (e.g. when invoices are created) in services or signals.

### Invoices (`invoice` app)

The invoice system is split into an abstract base and concrete types.

**Invoice (abstract)**
- `id`: `AutoField`
- `date`: `DateField`
- `amount`: `FloatField` – total invoice amount

**BuyInvoice**
- Inherits from `Invoice`
- `client`: `ForeignKey(ClientCompanyLink)` – supplier/customer link (client/company pair)

**SellInvoice**
- Inherits from `Invoice`
- `sold`: `CharField` with choices: `"PAID"`, `"UNPAID"`

**InvoiceItem**
- `idInvoiceElement`: `AutoField` – line item ID
- `invoice`: `ForeignKey(BuyInvoice)` – parent buy invoice
- `product`: `ForeignKey(Product)` – product being purchased
- `price_buy`: `FloatField` – unit purchase price
- `quantity`: `IntegerField`

An invoice therefore consists of:

- A **header** (`BuyInvoice` / `SellInvoice`) with date, client, amount.
- **Line items** (`InvoiceItem`) that reference products and define price/quantity.

The total `amount` on a `BuyInvoice` is computed from its `InvoiceItem`s during create:

\[
\text{amount} = \sum (\text{price\_buy} \times \text{quantity})
\]

---

## API Structure

All endpoints return and accept **JSON**. Authentication and permissions can be layered on top as needed.

### Product API (`/product/`)

- `POST /product/`
  - **Purpose**: Create a new product (and, optionally, auto-create/find a category).
  - **Body (example)**:

    ```json
    {
      "name": "Laptop",
      "mark": "Dell",
      "category": 1,
      "specifications": {
        "RAM": "16GB",
        "Storage": "512GB SSD"
      }
    }
    ```

  - **Behavior**:
    - Uses `ProductPostSerializer` to:
      - Normalize names/properties.
      - Ensure `specifications` matches the category `properties`.

- `GET /product/category`
  - **Purpose**: List all categories (including their `properties`).

- `GET /product/<category_name>`
  - **Purpose**: List all products belonging to the given category name.

### Inventory API (`/inventory/`)

- `GET /inventory/`
  - **Purpose**: List all inventory entries with product, quantity, location, and minimum quantity.

This headless backend is ready to be extended with stock movement logic that reacts to invoices (e.g. decrementing stock when a `SellInvoice` is created, or incrementing when a `BuyInvoice` is created).

### Invoice API (`/invoice/`)

- `GET /invoice/`
  - **Purpose**: List all buy invoices.
  - **Response fields** (per invoice):
    - `id`
    - `date`
    - `amount`
    - `provider` – derived provider name (company) from the linked client/company.

- `POST /invoice/`
  - **Purpose**: Create a new `BuyInvoice` and its `InvoiceItem`s in one request.
  - **Body (example)**:

    ```json
    {
      "date": "2025-02-18",
      "client": 1,
      "items": [
        { "product_id": 5, "price_buy": 150.0, "quantity": 2 },
        { "product_id": 8, "price_buy": 89.5, "quantity": 1 }
      ]
    }
    ```

  - **Behavior**:
    - Creates a `BuyInvoice`.
    - Creates `InvoiceItem` records for each item.
    - Computes and saves the total `amount`.
    - Returns the created invoice serialized with `InvoiceSerializer`.

- `GET /invoice/<id>`
  - **Purpose**: Get all line items (`InvoiceItem`) for a specific `BuyInvoice`.

- `GET /invoice/sell`
  - **Purpose**: List all `SellInvoice`s with their basic fields and `sold` status.

### Client & Finance API (`/client/`)

Although not the main focus of this README, the **client** app provides useful financial endpoints that integrate with invoices:

- `GET /client/`
  - Lists client–company links with contact and identity details.

- `GET /client/Finance`
  - Returns **per-company** aggregates:
    - `total_purchases` – sum of invoice amounts
    - `total_payments` – sum of payments
    - `outstanding_balance` – purchases minus payments

---

## JSON-Based Specifications Logic

One of the core design choices of this backend is the use of **JSON fields** to model product specifications:

- `Category.properties` defines the *schema* (attribute keys) for products in that category.
- `Product.specifications` stores per-product **values** keyed by those attributes.

This provides:

- High flexibility for different product types without database schema changes.
- Cleaner, category-driven specification management (e.g. laptops vs. monitors).
- An easy fit for headless frontends that can introspect category `properties` and build dynamic forms/UI.

The serializers (`ProductPostSerializer`) encapsulate the logic for:

- Normalizing property names.
- Mapping input specification JSON to the canonical set of category properties.
- Ensuring the database always stores a consistent structure.

---

## Headless Backend Core

This repository is intended to act as a **Headless Backend core**:

- All business capabilities are exposed via **JSON REST APIs**.
- No HTML pages or templates are rendered.
- Frontends (SPA, mobile apps, POS terminals, admin dashboards) can:
  - Integrate with the product, inventory, and invoice APIs.
  - Use the category/specifications mechanism to drive dynamic UI.
  - Build custom flows on top of invoices and payments.

You can extend this core by adding:

- Authentication/authorization (JWT, session-based, API keys).
- Webhooks or message queues for external integrations.
- Stock movement logic and audit trails.
- Additional reporting and dashboard endpoints.

---

## Running the Project (Development)

1. **Install dependencies** (create a virtualenv first if desired):
   ```bash
   pip install django djangorestframework
   ```

2. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Create a superuser** (optional, for Django admin):
   ```bash
   python manage.py createsuperuser
   ```

4. **Start the dev server**:
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/` with the described endpoints.

