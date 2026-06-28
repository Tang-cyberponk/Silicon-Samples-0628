# Step 3: Call the large model API to retrieve the model’s response

# Call the large language model API
def call_llm(messages):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE,
    )

    # Extract the questionnaire-response text returned by the model
    return response.choices[0].message.content.strip()
  
