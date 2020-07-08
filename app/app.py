from flask import Flask, render_template
import random

app = Flask(__name__)

# list of images
images = [
    "/static/electron.jpg",
    "/static/falcon9.jpg",
    "/static/falconheavy.jpg",
    "/static/h2b.jpg",
    "/static/vsb30.jpg"
]

@app.route('/')
def index():
    #url = random.choice(images)
    #return render_template('index.html', url=url)
    return "Hello World";

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80);
