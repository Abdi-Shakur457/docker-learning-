# CounterPro — CoderCo Containers Challenge

Welcome to **CounterPro**, a multi-container web application built using **Flask** and **Redis**.  
This project demonstrates how to build, dockerize, and run a multi-container application using **Docker Compose**.

---

## 🚀 Project Overview

CounterPro is a simple web app that:

- Displays a **welcome page**
- Increments and displays a **visit counter** stored in Redis
- Includes an **About Me** page
- Provides a link to the **GitHub repository**

---

## 🧩 Features

### ✔ Flask Web App
- **`/`** : Welcome page  
- **`/count`** : Increment and display visit count stored in Redis  
- **`/about`** : About me page  
- **GitHub link** : See source code and learn how it works  

### ✔ Redis Database
- Used as a key-value store  
- Stores visit count  
- Supports persistence via Docker volumes  

### ✔ Dockerized Architecture
- Flask app container  
- Redis container  
- Managed by Docker Compose  

---

## 📦 Docker Architecture

### Container Services

| Service | Description |
|--------|-------------|
| **web** | Flask application |
| **redis** | Redis database |

---

## 🛠️ Requirements

- Docker
- Docker Compose

---

## 🔧 Running the Application

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/CounterPro.git
cd CounterPro

2. Build & start containers
docker-compose up --build

3. Visit the app

Welcome Page: http://localhost:5000/

Counter Page: http://localhost:5000/count

About Me Page: http://localhost:5000/about

🧠 Bonus Features Included
✅ Persistent Redis Storage

Redis uses a Docker volume to persist data:

volumes:
  redis-data:

✅ Environment Variables

Redis connection details are read from environment variables:

redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = os.getenv("REDIS_PORT", 6379)

✅ Scaling Flask Service

Scale multiple Flask instances:

docker-compose up --scale web=3

📁 Project Structure
CounterPro/
│
├── app/
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── count.html
│   │   └── about.html
│   └── static/
│       └── styles.css
│
├── Dockerfile
├── docker-compose.yml
└── README.md

🧾 Docker Compose Example
version: "3.9"

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - REDIS_HOST=redis
      - REDIS_PORT=6379
    depends_on:
      - redis

  redis:
    image: "redis:alpine"
    volumes:
      - redis-data:/data

volumes:
  redis-data:

