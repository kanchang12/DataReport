import os
from flask import Flask, render_template, request
from nbconvert import execute_notebook

app = Flask(__name__)


# Route to serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Route to execute the notebook when the button is clicked
@app.route('/run_notebook', methods=['POST'])
def run_notebook():
    # Execute the notebook (add your notebook execution logic here)
    try:
        # Example: Execute notebook using nbconvert
        execute_notebook('https://6d4780637308d21c-dot-europe-west2.notebooks.googleusercontent.com/lab/tree/DataNotebook.ipynb')
        return 'Notebook executed successfully', 200
    except Exception as e:
        return f'Error executing notebook: {str(e)}', 500





if __name__ == "__main__":
    # Use Gunicorn as the production WSGI server
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)

