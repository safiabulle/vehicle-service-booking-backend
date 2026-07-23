# Vehicle Service Booking System - Backend

A RESTful backend API for the Vehicle Service Booking System built with **Django** and **Django REST Framework**. The system allows customers to register, manage vehicles, book service appointments, make payments, and enables administrators to manage services, bookings, and payments.

---

# Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running with Docker](#running-with-docker)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Future Improvements](#future-improvements)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

# Introduction

The Vehicle Service Booking System Backend provides secure REST APIs that power the frontend application. Customers can create accounts, register vehicles, book service appointments, and make payments, while administrators can manage the entire service booking workflow.

The project uses JWT authentication to secure protected endpoints and SQLite as the database.

---

# Features

### Authentication
- User Registration
- User Login
- JWT Authentication
- Protected Routes

### Vehicle Management
- Add Vehicle
- View Vehicles
- Update Vehicle
- Delete Vehicle

### Service Management
- Create Services
- View Services
- Update Services
- Delete Services

### Appointment Management
- Book Appointment
- View Appointments
- Update Appointment Status
- Cancel Appointment

### Payment Management
- Record Payments
- View Payments
- Update Payment Status

### Admin Dashboard
- View Total Customers
- View Total Bookings
- View Pending Bookings
- Manage Services
- Manage Payments

---

# Technologies Used

- Python 3.12
- Django 6
- Django REST Framework
- Simple JWT Authentication
- SQLite
- Docker
- Docker Compose

---

# Project Structure

```
backend/
│
├── accounts/
├── appointments/
├── config/
├── payments/
├── services/
├── vehicles/
│
├── manage.py
├── db.sqlite3
├── Dockerfile
└── requirements.txt
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/safiabulle/vehicle-service-booking-backend.git
```

## 2. Navigate into the project

```bash
cd vehicle-service-booking-backend
```

## 3. Create a virtual environment

```bash
python3 -m venv venv
```

## 4. Activate the virtual environment

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 6. Apply migrations

```bash
cd backend

python manage.py migrate
```

## 7. Run the server

```bash
python manage.py runserver
```

Backend runs at

```
http://127.0.0.1:8000/
```

---

# Running with Docker

Build the Docker containers

```bash
docker compose build
```

Run the containers

```bash
docker compose up
```

Stop the containers

```bash
docker compose down
```

The SQLite database is persisted using a Docker volume.

---

# API Endpoints

## Authentication

| Method | Endpoint |
|---------|----------|
| POST | /api/auth/register/ |
| POST | /api/auth/login/ |
| GET | /api/auth/me/ |

---

## Vehicles

| Method | Endpoint |
|---------|----------|
| GET | /api/vehicles/ |
| POST | /api/vehicles/ |
| PUT | /api/vehicles/{id}/ |
| DELETE | /api/vehicles/{id}/ |

---

## Services

| Method | Endpoint |
|---------|----------|
| GET | /api/services/ |
| POST | /api/services/ |
| PUT | /api/services/{id}/ |
| DELETE | /api/services/{id}/ |

---

## Appointments

| Method | Endpoint |
|---------|----------|
| GET | /api/appointments/ |
| POST | /api/appointments/ |
| PUT | /api/appointments/{id}/ |
| DELETE | /api/appointments/{id}/ |

---

## Payments

| Method | Endpoint |
|---------|----------|
| GET | /api/payments/ |
| POST | /api/payments/ |
| PUT | /api/payments/{id}/ |
| DELETE | /api/payments/{id}/ |

---

# Usage

1. Register a new account.
2. Login to receive a JWT token.
3. Add a vehicle.
4. Browse available services.
5. Book a service appointment.
6. Make payment.
7. Track appointment status.

Administrators can:

- Manage services
- Manage appointments
- Manage payments
- View customer bookings

---

# Future Improvements

- Email Notifications
- SMS Appointment Reminders
- Mpesa Payment Integration
- Service History Reports
- Vehicle Maintenance Records
- Admin Analytics Dashboard
- Search and Filter Features
- Docker Production Deployment
- PostgreSQL Support

---


# Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.

2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to GitHub.

```bash
git push origin feature-name
```

5. Create a Pull Request.

---

# License

This project is licensed under the MIT License.

---

## Author

**Safia Bulle**

GitHub:
https://github.com/safiabulle

---
