import os
import json
import requests

def groq_chat(request):
    """HTTP Cloud Function to handle chat requests."""
    
    # Set CORS headers for web browser support
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization'
    }
    
    # Handle preflight OPTIONS request
    if request.method == 'OPTIONS':
        return ('', 204, headers)
    
    try:
        # Get API key from environment
        api_key = os.environ.get('GROQ_API_KEY')
        if not api_key:
            return (json.dumps({'error': 'API key not configured'}), 500, headers)
        
        # Get user message from request
        if request.method == 'POST':
            request_json = request.get_json(silent=True)
        else:
            request_json = {}
        
        if request_json and 'message' in request_json:
            user_message = request_json['message']
            model = request_json.get('model', 'llama-3.1-8b-instant')
            max_tokens = request_json.get('max_tokens', 150)
        else:
            return (json.dumps({
                'response': 'Please provide a message in the request body.',
                'example': {'message': 'Hello!', 'model': 'llama-3.1-8b-instant'}
            }), 400, headers)
        
        # Call Groq API directly with requests
        groq_response = requests.post(
            'https://api.groq.com/openai/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            },
            json={
                'messages': [{'role': 'user', 'content': user_message}],
                'model': model,
                'max_tokens': max_tokens,
                'temperature': 0.7
            },
            timeout=30
        )
        
        if groq_response.status_code == 200:
            data = groq_response.json()
            ai_response = data['choices'][0]['message']['content']
            
            return (json.dumps({
                'response': ai_response,
                'model': model,
                'tokens_used': data['usage']['total_tokens']
            }), 200, headers)
        else:
            return (json.dumps({
                'error': f'Groq API error: {groq_response.status_code} - {groq_response.text}'
            }), 500, headers)
        
    except Exception as e:
        return (json.dumps({'error': str(e)}), 500, headers)