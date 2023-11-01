import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.7
        ).choices[0].text
        return response


