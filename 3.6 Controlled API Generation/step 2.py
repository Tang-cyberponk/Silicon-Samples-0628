
# 2.Combine the System Prompt with the User Prompt specific to the current sample
def build_messages(user_prompt: str):
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]
