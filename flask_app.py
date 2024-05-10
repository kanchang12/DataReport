import os
from flask import Flask, request, render_template
#from google.cloud import aiplatform
from vertexai.generative_models import GenerativeModel, Image, Content, Part, Tool, FunctionDeclaration, GenerationConfig
import vertexai

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

credentials = "8bca8389e484c393f4e12dafae49257f0606880b"
print(credentials)

project_id = "dataanalysis-422708"

vertexai.init(project=project_id, location="us-central1", credentials=credentials)

vision_model = GenerativeModel("gemini-ultra-vision")
vision_chat = vision_model.start_chat()
print("start")
#image = Image.load_from_file("image.jpg")
#print(vision_chat.send_message(["I like this image.", image]))
print(vision_chat.send_message("What things do I like?."))

model = GenerativeModel(
    "gemini-1.0-pro",
    system_instruction=[
        "Talk like a pirate.",
        "Don't use rude words.",
    ],
)
print(model.generate_content("Why is sky blue?"))

if __name__ == "__main__":
    # Use Gunicorn as the production WSGI server
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)

