import os
from flask import Flask, request, render_template
#from google.cloud import aiplatform
from vertexai.generative_models import GenerativeModel, Image, Content, Part, Tool, FunctionDeclaration, GenerationConfig

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


vision_model = GenerativeModel("gemini-ultra-vision")
vision_chat = vision_model.start_chat()
#image = Image.load_from_file("image.jpg")
#print(vision_chat.send_message(["I like this image.", image]))
print(vision_chat.send_message("What things do I like?."))

from vertexai.generative_models import GenerativeModel
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

