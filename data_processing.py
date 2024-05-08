import pandas as pd
import openai
import os
import sys
import logging

# Configure logging to write to a file
logging.basicConfig(filename='app.log', level=logging.DEBUG)

# Log a message that will be written to the file
logging.debug("Starting data_processing script")

# Set your OpenAI API key (assuming the secret name in Koyeb is "OpenAPI_KEY")
API_KEY = os.environ.get("OpenAPI_KEY1")
logging.debug(f"Retrieved API Key: {API_KEY}")

# Check if the API_KEY is None or not retrieved correctly
if API_KEY is None:
    logging.error("Error: OpenAPI_KEY1 environment variable is not set.")
    sys.exit(1)

# Set the OpenAI API key
openai.api_key = API_KEY

def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        logging.error(f"Error: Unable to read CSV file - {e}")
        return None

def preprocess_data(df):
    # Example preprocessing steps (replace NaN values with empty string)
    df.fillna('', inplace=True)
    return df

def generate_table_data(df):
    # Convert DataFrame to list of dictionaries (each row is a dictionary)
    table_data = df.to_dict(orient='records')
    return table_data

def call_openai_playground(prompt_text):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-16K",
            prompt=prompt_text,
            max_tokens=50,
            mode="chat",  # Specify mode as 'chat' for conversational responses
            project="proj_VFmwoRIS4vUBNX20sw0MPHhD",  # Use your specific project ID
            chat_project="chatprojects"  # Specify the chat project ID
        )
        return response.choices[0].text.strip()
    except Exception as e:
        logging.error(f"Error: Failed to call OpenAI Playground - {e}")
        return None

def main(csv_file_path, prompt_text):
    # Read CSV file
    df = read_csv_file(csv_file_path)
    if df is None:
        return

    # Preprocess data
    df_processed = preprocess_data(df)

    # Generate table data
    table_data = generate_table_data(df_processed)

    # Call OpenAI Playground with a prompt
    response_text = call_openai_playground(prompt_text)
    if response_text:
        logging.info("Response from OpenAI Playground:")
        logging.info(response_text)

    return table_data

if __name__ == "__main__":
    # Example usage: Provide CSV file path and prompt text as command-line arguments
    if len(sys.argv) < 3:
        logging.error("Usage: python data_processing.py <csv_file_path> <prompt_text>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    prompt_text = sys.argv[2]
    table_data = main(csv_file_path, prompt_text)
    if table_data:
        logging.info("Table data generated successfully.")
        logging.info(table_data)
