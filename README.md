# 🚀 Docker Commands Learned (CounterPro Project)

Below are the Docker commands I learned while building the CounterPro multi-container application.

---

## ✅ Docker Basics
```bash
docker --version
docker info
docker help

## 🧱 Working with Images
Pull an image from Docker Hub : 
docker pull redis:alpine

List local images : 
docker images

Remove an image : 
docker rmi <image_name_or_id>

### 🧰 Building Docker Images

Build image from Dockerfile : 
docker build -t counterpro-web .


## 🚀 Running Containers
Run a container
docker run -d --name my-redis redis:alpine

Run container with port mapping
docker run -d -p 5000:5000 counterpro-web

View running containers
docker ps

View all containers (including stopped)
docker ps -a

Stop a container
docker stop <container_id_or_name>

Remove a container
docker rm <container_id_or_name>
