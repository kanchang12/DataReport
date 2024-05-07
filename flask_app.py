import os
from flask import Flask, request, render_template
import openai
import data_processing

app = Flask(__name__)

# Set your OpenAI API key
API_KEY = "<your_openai_api_key>"
openai.api_key = API_KEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    csv_file = request.files['csvFile']
    user_input = request.form['userInput']

    # Read CSV file and preprocess data
    df = data_processing.read_csv_file(csv_file)
    if df is None:
        return "Error: Unable to process CSV file."

    df_processed = data_processing.preprocess_data(df)

    # Generate table data for OpenAI model
    table_data = data_processing.generate_table_data(df_processed)

    # Prepare prompt for GPT-3.5 model
    prompt_text = f"Data analysis for '{user_input}':\n"
    for row in table_data:
        prompt_text += f"{row}\n"

    # Call GPT-3.5 model (datanalysis) with the prompt
    try:
        response = openai.Completion.create(
            engine="datalogist-35",  # Use your GPT-3.5 model engine name
            prompt=prompt_text,
            max_tokens=300  # Adjust max tokens as needed
        )
        analysis_result = response['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error: Failed to call OpenAI model - {e}"

    return render_template('analysis.html', analysis_result=analysis_result)

if __name__ == "__main__":
    # Use Gunicorn as the production WSGI server
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)
