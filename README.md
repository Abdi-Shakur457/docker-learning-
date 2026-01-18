# 🚀 Docker Commands Learned (CounterPro Project)

Below are the Docker commands I learned while building the CounterPro multi-container application.

---

## ✅ Docker Basics
```bash
docker --version
docker info
docker help
🧱 Working with Images
Pull an image from Docker Hub
bash
Copy code
docker pull redis:alpine
List local images
bash
Copy code
docker images
Remove an image
bash
Copy code
docker rmi <image_name_or_id>
🧰 Building Docker Images
Build image from Dockerfile
bash
Copy code
docker build -t counterpro-web .
🚀 Running Containers
Run a container
bash
Copy code
docker run -d --name my-redis redis:alpine
Run container with port mapping
bash
Copy code
docker run -d -p 5000:5000 counterpro-web
View running containers
bash
Copy code
docker ps
View all containers (including stopped)
bash
Copy code
docker ps -a
Stop a container
bash
Copy code
docker stop <container_id_or_name>
Remove a container
bash
Copy code
docker rm <container_id_or_name>
🧹 Cleaning Up
Remove all stopped containers
bash
Copy code
docker container prune
Remove unused images
bash
Copy code
docker image prune
Remove unused volumes
bash
Copy code
docker volume prune
🧩 Docker Compose Commands
Start services
bash
Copy code
docker-compose up
Start services in detached mode
bash
Copy code
docker-compose up -d
Build and start
bash
Copy code
docker-compose up --build
Stop services
bash
Copy code
docker-compose down
Scale a service (multi-instance)
bash
Copy code
docker-compose up --scale web=3
View Compose logs
bash
Copy code
docker-compose logs
