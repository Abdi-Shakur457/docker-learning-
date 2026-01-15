FROM python:3.12-slim 

WORKDIR /app 

COPY requirements.txt . 

RUN pip3 install --no-cache-dir -r requirements.txt 

EXPOSE 5003 

COPY . . 


CMD ["python3" , "my_app.py"] 

