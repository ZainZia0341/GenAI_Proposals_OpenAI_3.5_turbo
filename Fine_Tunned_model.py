import openai

# Load OpenAI API key
openai.api_key = "your_openai_api_key"

def generate_proposal(job_description, fine_tuned_model):
    response = openai.Completion.create(
        model=fine_tuned_model,  # Replace with your fine-tuned model ID
        prompt=job_description,
        max_tokens=1500,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

# Example usage
job_description = ""
fine_tuned_model = "your_fine_tuned_model_id"  # Replace with the fine-tuned model ID you received after fine-tuning
proposal = generate_proposal(job_description, fine_tuned_model)
print(proposal)
