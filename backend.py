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


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("1")
    print(response)