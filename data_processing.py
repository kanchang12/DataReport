1  import pandas as pd
2  import openai
3  import os

# Set your OpenAI API key (assuming the secret name in Koyeb is "OpenAPI_KEY")
4  API_KEY = os.environ.get("OpenAPI_KEY")

5  openai.api_key = API_KEY

6  def read_csv_file(file_path):
7      try:
8          df = pd.read_csv(file_path)
9          return df
10      except Exception as e:
11          print(f"Error: Unable to read CSV file - {e}")
12          return None

13  def preprocess_data(df):
14      # Example preprocessing steps (replace NaN values with empty string)
15      df.fillna('', inplace=True)
16      return df

17  def generate_table_data(df):
18      # Convert DataFrame to list of dictionaries (each row is a dictionary)
19      table_data = df.to_dict(orient='records')
20      return table_data

21  def call_openai_playground(prompt_text):
22      try:
23          response = openai.Completion.create(
24              engine="text-davinci-002",
25              prompt=prompt_text,
26              max_tokens=50
27          )
28          return response.choices[0].text.strip()
29      except Exception as e:
30          print(f"Error: Failed to call OpenAI Playground - {e}")
31          return None

32  def main(csv_file_path, prompt_text):
33      # Read CSV file
34      df = read_csv_file(csv_file_path)
35      if df is None:
36          return

37      # Preprocess data
38      df_processed = preprocess_data(df)

39      # Generate table data
40      table_data = generate_table_data(df_processed)

41      # Call OpenAI Playground with a prompt
42      response_text = call_openai_playground(prompt_text)
43      if response_text:
44          print("Response from OpenAI Playground:")
45          print(response_text)

46      return table_data

47  if __name__ == "__main__":
48      # Example usage: Provide CSV file path and prompt text as command-line arguments
49      import sys
50      if len(sys.argv) < 3:
51          print("Usage: python data_processing.py <csv_file_path> <prompt_text>")
52          sys.exit(1)

53      csv_file_path = sys.argv[1]
54      prompt_text = sys.argv[2]
55      table_data = main(csv_file_path, prompt_text)
56      if table_data:
57          print(table_data)
