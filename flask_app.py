import os
from flask import Flask, request, jsonify, render_template
#from nbconvert import execute_notebook
import requests
#import vertexai
#from vertexai.generative_models import GenerativeModel

import subprocess



app = Flask(__name__)


# Route to serve the index.html page
@app.route('/')
def index():
    print("html")
    return render_template('index.html')

def execute_notebook(notebook_path):
    # Construct the command to execute the notebook with jupytext
    command = f"jupytext --execute {notebook_path}"


@app.route('/process', methods=['POST'])
def process_request():
    # Get text input from the form
    user_input = request.form['user_input']
    print(user_input)

    # Send the input to the Jupyter Notebook (replace with your notebook URL)
    jupyter_url = 'https://6d4780637308d21c-dot-europe-west2.notebooks.googleusercontent.com/lab/tree/DataNotebook.ipynb'
    exec = execute_notebook(jupyter_url)
    response = requests.post(jupyter_url, json={'user_input': user_input})
    print('user_input': user_input}

    # Get the result from the Jupyter Notebook
    if response.status_code == 200:
        result = response.json().get('result', 'No result')
    else:
        result = 'Error communicating with the Jupyter Notebook'

    # Render a new page to display the result
    return render_template('index.html', result=result)





if __name__ == "__main__":
    # Use Gunicorn as the production WSGI server
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port, debug=True)

