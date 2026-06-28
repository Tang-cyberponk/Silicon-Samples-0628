
# 4. Process one individual sample
def process_one_row(sample_index, row):
    # Step 5: Generate the individualized User Prompt for the current sample
    user_prompt = generate_user_prompt(row)

    # Step 6: Combine the prompts into the messages required for the API request
    messages = build_messages(user_prompt)

    # Call the API to obtain the questionnaire responses for the current sample
    raw_answer = call_llm(messages)

    # Save the original background variables, individualized prompt,
    # and model-generated questionnaire responses
    row_result = row.to_dict()
    row_result["sample_index"] = sample_index
    row_result["Prompt"] = user_prompt
    row_result["RawAnswer"] = raw_answer

    return row_result

