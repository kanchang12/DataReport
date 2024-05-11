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

# Route to process the input from frontend
@app.route('/process', methods=['POST'])
def process_input():
    # Get input text from the form submitted by frontend
    input_text = request.form['input_text']

    # URL of the Jupyter Notebook backend (Vertex AI endpoint)
    notebook_url = 'https://6d4780637308d21c-dot-europe-west2.notebooks.googleusercontent.com/lab/tree/DataNotebook.ipynb'

    # Send the input text to the Jupyter Notebook backend
    response = requests.post(notebook_url, json={'input_text': input_text})

    # Retrieve the processed output from the Jupyter Notebook
    processed_output = response.json().get('processed_output')

    # Return the processed output to the frontend
    return jsonify({'result': processed_output})





if __name__ == "__main__":
    # Use Gunicorn as the production WSGI server
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)

