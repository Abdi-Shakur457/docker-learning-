import os
from flask import Flask, render_template
from redis import Redis

app = Flask(__name__)

redis_host = os.getenv("LOCAL_HOST", "redis")
redis_port = int(os.getenv("LOCAL_PORT", 6379))

r = Redis(host=redis_host, port=redis_port)

@app.route("/")
def index():
    count = r.incr("visits")
    return render_template("index.html", visit_count=count)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)


