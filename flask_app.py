import os
from flask import Flask, request, jsonify, render_template
#from nbconvert import execute_notebook
import requests
import vertexai
from vertexai.generative_models import GenerativeModel

app = Flask(__name__)


# Route to serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_request():
    # Get data from frontend
    data = request.get_json()

    # Make a request to the hosted Python script endpoint
    script_endpoint_url = 'YOUR_HOSTED_PYTHON_SCRIPT_ENDPOINT'
    response = requests.post(script_endpoint_url, json=data)

    # Return response from the hosted Python script to frontend
    return jsonify(response.json())





if __name__ == "__main__":
    # Use Gunicorn as the production WSGI server
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)

