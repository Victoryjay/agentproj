import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key == None:
    raise RunTimeError("API Key Not Found")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key = api_key,
)

def main():
    response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        }
    ],
)
    if response.usage is None:
        raise RunTimeError("API request failed or did not return token usage statistics.")
    
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
    
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
