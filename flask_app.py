import os
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'






if __name__ == "__main__":
    # Use Gunicorn as the production WSGI server
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)

