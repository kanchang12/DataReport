import pandas as pd
import openai
from google.cloud import secretmanager

# Function to retrieve the OpenAI API key from Secret Manager
def get_api_key():
  """
  Retrieves the OpenAI API key from Google Cloud Secret Manager.
  """
  project_id = "230931703669"  # Replace only if your project ID is different
  secret_name = "DataAnalysis"  # Replace only if your secret name is different

  client = secretmanager.SecretManagerServiceClient()
  name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
  try:
      response = client.access_secret_version(name=name)
      return response.payload.data.decode("UTF-8")
  except Exception as e:
      print(f"Error: Failed to retrieve API key from Secret Manager - {e}")
      return None  # Handle missing or inaccessible key

# Set OpenAI API key (using the retrieved key)
API_KEY = get_api_key()
openai.api_key = API_KEY


def read_csv_file(file_path):
  """
  Read a CSV file and return a pandas DataFrame.
  """
  try:
    df = pd.read_csv(file_path)
    return df
  except Exception as e:
    print(f"Error: Unable to read CSV file - {e}")
    return None

def preprocess_data(df):
  """
  Preprocess the DataFrame (e.g., handle missing values, data cleaning, etc.).
  """
  # Example preprocessing steps (replace NaN values with empty string)
  df.fillna('', inplace=True)
  return df

def generate_table_data(df):
  """
  Generate table format data suitable for input to OpenAI Playground.
  """
  # Convert DataFrame to list of dictionaries (each row is a dictionary)
  table_data = df.to_dict(orient='records')
  return table_data

def call_openai_playground(prompt_text):
  """
  Call OpenAI Playground API with a prompt text.
  """
  try:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_text,
        max_tokens=50
    )
    return response.choices[0].text.strip()
  except Exception as e:
    print(f"Error: Failed to call OpenAI Playground - {e}")
    return None

def main(csv_file_path, prompt_text):
  """
  Main function to process CSV data and interact with OpenAI Playground.
  """
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
    print("Response from OpenAI Playground:")
    print(response_text)

  return table_data

if __name__ == "__main__":
  # Example usage: Provide CSV file path and prompt text as command-line arguments
  import sys
  if len(sys.argv) < 3:
    print("Usage: python data_processing.py <csv_file_path> <prompt_text>")
    sys.exit(1)
  
  csv_file_path = sys.argv[1]
  prompt_text = sys.argv[2]
  table_data = main(csv_file_path, prompt_text)
  if table_data:
    print(table_data)
