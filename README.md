# DjangoMart - E-commerce Platform

## Overview
DjangoMart is a modern e-commerce web application built using Django. It provides a seamless shopping experience with features like product browsing, cart management, authentication, and an admin panel. The project also includes a REST API for integration with third-party services and mobile applications.

## Features
### **User Features**
- Browse all products with category filtering
- View single product details
- Add/remove products from the cart
- View cart contents
- User authentication (Login/Register)

### **Admin Features**
- Add, update, and delete products
- Manage product categories
- View and manage all user orders

### **API Features**
- Retrieve a list of products (GET `/api/products/`)
- Retrieve a single product (GET `/api/products/<id>/`)
- Add a product to the cart (POST `/api/cart/add/`)
- Remove a product from the cart (DELETE `/api/cart/remove/<id>/`)
- View user cart details (GET `/api/cart/`)

## Technologies Used
### **Backend**
- Django (Python)
- Django REST Framework (DRF) for API development
- PostgreSQL as the database

### **Frontend**
- HTML, CSS, Bootstrap for UI
- JavaScript for interactivity

### **Authentication & Security**
- Django's built-in authentication system
- Role-based access control for staff and users

### **Deployment & DevOps**
- Docker for containerized deployment (planned)

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/AhmedMazenNn/DjangoMart.git
   cd DjangoMart
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser (admin login):
   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Testing with Postman
- Import the API endpoints into Postman
- Use `http://127.0.0.1:8000/api/products/` to fetch products
- Use authentication headers for protected routes

## Future Enhancements
- Implement payment gateway integration
- Add product reviews and ratings
- Improve UI with React.js
- Optimize performance using caching

## Contributors
- **Ahmed Mazen** - Full Stack Developer
