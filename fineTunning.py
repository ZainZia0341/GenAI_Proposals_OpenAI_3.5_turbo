import json
import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load data from the JSON file
with open(r"E:\Kachori\GenAI_Proposals_OpenAI\data.json", 'r') as file:
    data = json.load(file)

# Prepare the data for fine-tuning
# Prepare the data for fine-tuning in the chat format
train_data = []
for item in data:
    job_description = item['job_description']['description']
    proposal = item['proposal']['introduction'] + " " + item['proposal']['experience'] + " " + " ".join(item['proposal']['solutions_implemented']) + " " + item['proposal']['conclusion']
    train_data.append({
        "messages": [
            {"role": "user", "content": job_description},
            {"role": "assistant", "content": proposal}
        ]
    })

# Save the training data in a new JSONL file
with open(r"E:\Kachori\GenAI_Proposals_OpenAI\prepared_data.jsonl", 'w') as file:
    for entry in train_data:
        json.dump(entry, file)
        file.write('\n')

# Load OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Upload the file to OpenAI
with open(r"E:\Kachori\GenAI_Proposals_OpenAI\prepared_data.jsonl", "rb") as f:
    response = openai.files.create(file=f, purpose='fine-tune')
# Print response to understand its structure

print("File upload response:", response)

# Get file_id from response
file_id = "file-QDf1vx1COhmmvqIJWwTjvEGO"
# if not file_id:
#     raise ValueError("Failed to upload file to OpenAI")

# Create a fine-tuning job
response = openai.fine_tuning.jobs.create(training_file=file_id, model="gpt-3.5-turbo")

# Print response to understand its structure
print("Fine-tuning response:", response)

# fine_tune_id = response.get('id')
# if not fine_tune_id:
#     raise ValueError("Failed to create fine-tuning job")

# print(f"Fine-tuning job created with ID: {fine_tune_id}")