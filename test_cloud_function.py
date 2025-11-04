# Simple test for our cloud function logic
from main import groq_chat

class MockRequest:
    def __init__(self, method='POST', json_data=None):
        self.method = method
        self.json_data = json_data
    
    def get_json(self, silent=False):
        return self.json_data

# Test the function
if __name__ == "__main__":
    test_request = MockRequest(json_data={'message': 'Hello from test!'})
    response, status, headers = groq_chat(test_request)
    print(f"Status: {status}")
    print(f"Response: {response}")