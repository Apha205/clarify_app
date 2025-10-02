import openai

def summarize_text(text: str, api_key: str) -> str:
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Summarize the following text:\n\n{text}"}],
        max_tokens=150
    )
    return response.choices[0].message.content.strip()