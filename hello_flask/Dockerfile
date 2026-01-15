FROM python:3.8-slim
RUN apt update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app 
COPY hello_flask/app.py /app/ 
RUN pip install flask mysqlclient 
EXPOSE 5002 
CMD ["python", "app.py"] 
 

