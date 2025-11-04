import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # Load environment variables
api_key = os.environ.get('GROQ_API_KEY')  # Secure!

def chat_with_ai():
    client = Groq(api_key=api_key)
    messages = []
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            break
            
        messages.append({"role": "user", "content": user_input})
        
        response = client.chat.completions.create(
            messages=messages,
            model="moonshotai/kimi-k2-instruct-0905",
            max_tokens=150
        )
        
        ai_response = response.choices[0].message.content
        print(f"AI: {ai_response}")
        messages.append({"role": "assistant", "content": ai_response})

if __name__ == "__main__":
    chat_with_ai()