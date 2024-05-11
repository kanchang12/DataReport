import os
from flask import Flask, request, jsonify, render_template
from nbconvert import execute_notebook
import requests

app = Flask(__name__)


# Route to serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Route to process form submission from the frontend
@app.route('/process', methods=['POST'])
def process_request():
    # Get data from the form submitted by the frontend
    input_text = request.form.get('input_text')

    # Make a request to the Jupyter Notebook backend
    notebook_url = 'https://6d4780637308d21c-dot-europe-west2.notebooks.googleusercontent.com/lab/tree/DataNotebook.ipynb'
    data = {'input_text': input_text}  # Data to send to Jupyter Notebook
    response = requests.post(notebook_url, json=data)

    # Return response from Jupyter Notebook to frontend
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'Failed to process request'}), 500






if __name__ == "__main__":
    # Use Gunicorn as the production WSGI server
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)

