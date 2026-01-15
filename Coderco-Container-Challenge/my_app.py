# my web flask application that runs on redis
import os 
from flask import Flask
from redis import Redis
app = Flask(__name__)

redis_host = os.getenv('LOCAL_HOST' , 'redis')
redis_port = int(os.getenv('LOCAL_PORT' , 6379)) 

r = Redis(host=redis_host , port=redis_port)

@app.route("/")

def index():

    return " Welcome to my Coder co Container Web Application Docker Challange "

@app.route('/count')

def count():

    count = r.incr('visits')

    return f"You have visited this Page {count} times"


if __name__ == "__main__":

    app.run(host="0.0.0.0" , port=5003)
