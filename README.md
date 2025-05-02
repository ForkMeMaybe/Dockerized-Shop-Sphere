# 🛒 Shop Sphere — Full Stack E-Commerce App (Dockerized)

Access the live application at: [https://shop-sphere-frontend.onrender.com/]

Welcome to **Shop Sphere**, a full-stack, production-ready e-commerce application built with Django, DRF, Celery, Redis, Postgres, and a modern frontend stack (like React or Vue). This project is fully containerized with Docker and ready to run in just a few commands.

---

## 📦 Features

- 🔧 **Backend** – Django + DRF with Celery workers for background tasks  
- 🌐 **Frontend** – Lightweight production-ready SPA  
- 🎯 **Task Queue** – Celery, Celery Beat, and Flower for real-time monitoring  
- 💾 **Database** – PostgreSQL with persistent volume  
- ⚡ **Cache/Broker** – Redis  
- 🧪 **Test Watcher** – Auto-run tests using `ptw`  
- ☁️ **Whitenoise** – Serves static files in production  

---

## 🚀 Getting Started

You can run the application in **two ways**:

---

### ▶️ Option 1: Pull Prebuilt Docker Images (Quick Start)

1. Clone the repository:

    ```bash
    git clone https://github.com/ForkMeMaybe/Dockerized-Shop-Sphere.git
    cd Dockerized-Shop-Sphere
    ```

2. Start all services using prebuilt Docker Hub images:

    ```bash
    docker-compose -f docker-compose-pull.yml up
    ```

> 📝 This option is the fastest and doesn't require you to build images locally.

---

### 🔨 Option 2: Build from Source (Full Local Control)

1. Clone the repository:

    ```bash
    git clone https://github.com/ForkMeMaybe/Dockerized-Shop-Sphere.git
    cd Dockerized-Shop-Sphere
    ```

2. Open `dev.py` and fill in the following placeholders with your environment variables:

    ```python
    DEFAULT_FROM_EMAIL = "<your-email@example.com>"
    EMAIL_HOST = "<your-smtp-host>"
    EMAIL_HOST_USER = "<your-email>"
    EMAIL_HOST_PASSWORD = "<your-email-password>"
    RAZOR_KEY_ID = "<your-razorpay-key-id>"
    RAZOR_KEY_SECRET = "<your-razorpay-key-secret>"
    SECRET_KEY = "<copy this from common.py>"
    ```

    Additionally, **optional**: Configure your **database settings** if needed.

4. **Important for production**: In `backend/core/views.py`, remove `@csrf_exempt` before deploying to production.

5. If you cloned the project on **Windows**, you'll need to change the line endings in all scripts (like `backend/docker-entrypoint.sh` and `backend/wait-for-it.sh`) from CRLF to LF. You can do this using the following command in Git or use VS-Code and look on bottom right:

    ```bash
    git config --global core.autocrlf input
    ```

6. Return to the root of the project and build everything:

    ```bash
    docker-compose up --build
    ```

---

## 🔧 Services Overview

| Service      | Description                        | Port     |
|--------------|------------------------------------|----------|
| frontend     | React/Vite/Next (Production Build) | `5173`   |
| backend      | Django REST API                    | `8000`   |
| postgres     | PostgreSQL Database                | `5432`   |
| redis        | In-memory broker                   | `6379/2` |
| celery       | Background task worker             | `6379/1` |
| celery-beat  | Scheduled tasks                    | —        |
| flower       | Celery monitoring dashboard        | `5555`   |
| tests        | Auto test runner using `ptw`       | —        |

---

## 🗃 Volumes

Docker creates named volumes for persistent storage:

- `pgdata` – for PostgreSQL data
- `redisdata` – for Redis persistence

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---
