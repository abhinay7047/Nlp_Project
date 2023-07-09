import paralleldots
# Setting your API key

class API:

    def __init__(self):
        paralleldots.set_api_key('8qIxghqWrB3cl1R5xmZPVQBIHxTFZFLGH66aEdM8uRk')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def ner(self,text):
        response1=paralleldots.ner(text)
        return response1

    def emotion_prediction(self,text):
        response2=paralleldots.emotion(text)
        return response2
