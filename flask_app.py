import os
from flask import Flask, request, render_template
import google.generativeai as genai

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('Please summarise this document: ...')

print(response.text)




if __name__ == "__main__":
    # Use Gunicorn as the production WSGI server
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)

