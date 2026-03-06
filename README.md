# StockWise – Inventory Management System

StockWise is a **role-based inventory management web application** designed to help warehouses and businesses manage products, orders, shipments, and employee operations efficiently.

The system provides **different access levels for managers and employees**, allowing managers to monitor operations through analytics while employees handle day-to-day inventory activities.

---

## Live Demo

**Deployment**  
https://ahmedmazen-stock-wise.hf.space

**Demo Credentials**

Manager Account  
- Username: `manager1`  
- Password: `Admin123456`

---

## Project Overview

StockWise was developed as a **team project** to simulate a real-world warehouse management system.

The application focuses on:

- Inventory tracking
- Order and shipment management
- Role-based access control
- Operational analytics for managers

Managers supervise the system while employees execute operational tasks.

---

## Features

### Manager Features

Managers have full operational visibility and control.

- Register and manage employees
- View system analytics and operational insights
- Monitor total number of orders and shipments
- Access warehouse activity dashboard
- Track inventory performance

### Employee Features

Employees manage daily warehouse operations.

- Add new products to inventory
- Create and manage orders
- Update product stock levels
- Submit operational data to the system

---

## Analytics Dashboard

Managers can view operational analytics including:

- Total orders processed
- Total shipments handled
- Product inventory insights
- Visual charts representing warehouse performance

Analytics are dynamically generated from the database.

---

## Technology Stack

### Backend
- Django
- Python

### Database
- PostgreSQL (Neon)

### Frontend
- HTML
- CSS
- JavaScript
- Bootstrap

### Deployment
- Hugging Face Spaces
- Docker (containerized deployment)

---

## System Architecture

The application follows a typical **Django MVC architecture**:

```
User Interface (HTML/CSS/JS)
        │
        ▼
Django Views & Templates
        │
        ▼
Business Logic
        │
        ▼
PostgreSQL Database
```

Role-based permissions are enforced through a custom **User model**.

---

## Installation (Local Setup)

### Clone the repository

```bash
git clone https://github.com/mohamed1sobhi/Inventory_Management_System.git
```

### Navigate into the project

```bash
cd Inventory_Management_System
```

### Create virtual environment

```bash
python -m venv .venv
```

### Activate environment

Linux / Mac

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run migrations

```bash
python manage.py migrate
```

### Start development server

```bash
python manage.py runserver
```

---

## Project Structure

```
Inventory_Management_System
│
├── accounts
│   ├── authentication
│   └── employee management
│
├── inventory
│   ├── product management
│   └── analytics
│
├── orders
│   └── order handling
│
├── shipment
│   └── shipment processing
│
├── templates
│
└── static
```

---

## Role-Based Access

| Role | Permissions |
|-----|-------------|
| Manager | Manage employees, access analytics, view orders and shipments |
| Employee | Add products, create orders |

---

## Team Project

This project was developed collaboratively as a **team project**, focusing on:

- Backend development
- Database design
- Role-based authorization
- Inventory system logic

---

## Future Improvements

- Advanced inventory forecasting
- Real-time notifications for low stock
- REST API for mobile integration
- Reporting and export features
- Advanced analytics dashboard

---

## License

This project was developed for **educational and demonstration purposes**.

---

## Author

Ahmed Mazen  

GitHub  
https://github.com/AhmedMazenNn
