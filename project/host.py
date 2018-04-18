from flask import Flask
import settings

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello, World!"

def main():
    app.run(port=settings.FLASK_PORT, debug=settings.FLASK_DEBUG)