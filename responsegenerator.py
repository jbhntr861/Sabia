class ResponseGenerator:
    def __init__(self):
        self.openai = OpenAI()
    
    def generate_response(self, input_text):
        response = self.openai.generate_response(input_text)
        return response
