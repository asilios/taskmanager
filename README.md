# ✅ TaskManager

A full-featured task management web application built with Django, PostgreSQL, Docker, and GitHub Actions CI/CD.

## Features

- **User Authentication** — Register, login, logout
- **Task Management** — Full CRUD: create, view, edit, delete tasks
- **Categories** — Organise tasks by category (many-to-one)
- **Tags** — Label tasks with multiple tags (many-to-many)
- **Filtering** — Search and filter tasks by status and priority
- **Dashboard** — Overview of task statistics
- **Admin Panel** — Django admin for data management

## Technologies Used

| Layer | Technology |
|-------|-----------|
| Backend | Django 4.2, Python 3.11 |
| Database | PostgreSQL 15 |
| Web Server | Nginx + Gunicorn |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Cloud | Eskiz Cloud Server |
| SSL | Let's Encrypt (Certbot) |

## Local Setup

### Prerequisites
- Docker & Docker Compose installed

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/YOURUSERNAME/taskmanager.git
cd taskmanager

# 2. Copy and configure environment variables
cp .env.example .env
# Edit .env with your values

# 3. Start development environment
docker compose -f docker-compose.dev.yml up --build

# 4. Open http://localhost:8000
```

## Deployment Instructions

```bash
# On your server
git clone https://github.com/YOURUSERNAME/taskmanager.git
cd taskmanager
cp .env.example .env
# Edit .env with production values

# Pull and start
docker compose pull
docker compose up -d

# Create superuser
docker compose exec web python manage.py createsuperuser
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | Set to `False` in production |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts |
| `POSTGRES_DB` | PostgreSQL database name |
| `POSTGRES_USER` | PostgreSQL username |
| `POSTGRES_PASSWORD` | PostgreSQL password |
| `POSTGRES_HOST` | PostgreSQL host (use `db` for Docker) |
| `DOCKERHUB_USERNAME` | Your Docker Hub username |

## GitHub Secrets Required

- `DOCKERHUB_USERNAME` — Docker Hub username
- `DOCKERHUB_TOKEN` — Docker Hub access token
- `SSH_PRIVATE_KEY` — Private SSH key for server access
- `SSH_HOST` — Server IP address
- `SSH_USERNAME` — Server SSH username

## Live Application

- **App URL:** https://yourdomain.uz
- **Admin:** https://yourdomain.uz/admin
- **Test credentials:** username: `testuser` / password: `testpass123`

<!-- Updated deployment configuration -->
