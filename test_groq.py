import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv() 

api_key = os.environ.get('GROQ_API_KEY')  

def test_groq():
    try:
        client = Groq(api_key=api_key)
        
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": "Write a short haiku about cloud computing."}],
            model="moonshotai/kimi-k2-instruct-0905",
            max_tokens=100
        )
        
        print("✅ Success! Response:")
        print(response.choices[0].message.content)
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_groq()