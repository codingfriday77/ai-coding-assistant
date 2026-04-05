import os
from dotenv import load_dotenv
from openai import OpenAI

# Clear any cached API key from environment
if "OPENAI_API_KEY" in os.environ:
    del os.environ["OPENAI_API_KEY"]

# Explicitly load from .env file
load_dotenv(dotenv_path="e:\\ai-coding-assistant-main\\.env", override=True)

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")

print(f"API Key loaded: {api_key}")
print(f"API Key length: {len(api_key) if api_key else 'None'}")

# Try to create a client and make a test call
try:
    client = OpenAI(api_key=api_key)
    print("✓ OpenAI client created successfully")
    
    # Test with a simple API call
    print("\nTesting API call...")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hello"}
        ],
        max_tokens=10
    )
    print("✓ API call successful!")
    print(f"Response: {response.choices[0].message.content}")
    
except Exception as e:
    print(f"✗ Error: {type(e).__name__}: {e}")
