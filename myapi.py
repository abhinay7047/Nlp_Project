import paralleldots

class API:
    def __init__(self):
        # Initialize the ParallelDots API with your API key
        paralleldots.set_api_key('8qIxghqWrB3cl1R5xmZPVQBIHxTFZFLGH66aEdM8uRk')

    def sentiment_analysis(self, text):
        """
        Perform sentiment analysis on the given text.

        Args:
            text (str): The text for sentiment analysis.

        Returns:
            dict: A dictionary containing sentiment analysis results.
        """
        response = paralleldots.sentiment(text)
        return response

    def ner(self, text):
        """
        Perform named entity recognition (NER) on the given text.

        Args:
            text (str): The text for NER analysis.

        Returns:
            dict: A dictionary containing NER analysis results.
        """
        response1 = paralleldots.ner(text)
        return response1

    def emotion_prediction(self, text):
        """
        Predict emotions in the given text.

        Args:
            text (str): The text for emotion prediction.

        Returns:
            dict: A dictionary containing emotion prediction results.
        """
        response2 = paralleldots.emotion(text)
        return response2
