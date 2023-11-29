# VENDORMANAGEMENT_ASSIGNMENT

# 🚀 Project Setup

Welcome to the quick-start guide for your Django project! Get up and running in no time.

## ⚙️ Prerequisites

- [Python](https://www.python.org/) installed (version 3.x recommended)
- [Django](https://www.djangoproject.com/) installed (install using `pip install django`)

## 🛠️ Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Brijesh-26/VENDORMANAGEMENT_ASSIGNMENT.git
   cd your-django-project

1. **Create a Virtual Environment:**

   ```bash
   python -m venv venv


1. **Activate the Virtual Environment:**

   ```bash
   .\venv\Scripts\activate
   
1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

1. **Apply Migrations:**

   ```bash
   python manage.py migrate

1. **Create Superuser:**

   ```bash
   python manage.py createsuperuser
   
1. **Run the Development Server:**

   ```bash
   python manage.py runserver
   
1. **Access Django Admin:**

   ```bash
   Go to http://localhost:8000/admin
   Log in with the superuser credentials created earlier.
   ```

   

# 🌈 Django API Endpoints

Welcome to the documentation of our vibrant Django API! Below, you'll find details about the available endpoints and their functionalities.

## 🚀 Authentication

### Get Tokens
- **Endpoint:** `/api/token/`
- **Method:** `POST`
- **Description:** Get a authorization token.

### Refresh Tokens
- **Endpoint:** `api/token/refresh/`
- **Method:** `POST`
- **Description:** Refresh The Token In case the access token has been expired.

## 🚀 Vendors

### Create Vendor
- **Endpoint:** `/create_vendors/`
- **Method:** `POST`
- **Description:** Create a new vendor.

### Get All Vendors
- **Endpoint:** `/all_vendors/`
- **Method:** `GET`
- **Description:** Retrieve a list of all vendors.

### Get Vendor by ID
- **Endpoint:** `/vendors/<int:vendor_id>/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific vendor by ID.

### Update Vendor
- **Endpoint:** `/update_vendor/<int:vendor_id>/`
- **Method:** `PUT`
- **Description:** Update information for a specific vendor.

### Delete Vendor
- **Endpoint:** `/delete_vendor/<int:vendor_id>/`
- **Method:** `DELETE`
- **Description:** Delete a vendor by ID.

## 📦 Purchasing Things

### Create Purchase Orders
- **Endpoint:** `/make_purchase_orders/`
- **Method:** `POST`
- **Description:** Create a new purchase order.

### List All Purchase Orders
- **Endpoint:** `/purchase_orders/`
- **Method:** `GET`
- **Description:** Retrieve a list of all purchase orders.

### Get Purchase Order by ID
- **Endpoint:** `/purchase_orders/<int:id>/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific purchase order by ID.

### Update Purchase Order
- **Endpoint:** `/update_purchase_orders/<int:id>/`
- **Method:** `PUT`
- **Description:** Update information for a specific purchase order.

### Delete Purchase Order
- **Endpoint:** `/delete_purchase_orders/<int:id>/`
- **Method:** `DELETE`
- **Description:** Delete a purchase order by ID.

## 🚀 Performance

### Get Vendor Metrics
- **Endpoint:** `/vendors/<int:vendor_id>/performance/`
- **Method:** `GET`
- **Description:** Retrieve performance metrics for a specific vendor.

Feel free to explore and test these endpoints to unleash the full power of our API! Happy coding! 🚀


