"""
Service for mood detection using the emotion model.
"""
from transformers import pipeline

class MoodService:
    def __init__(self):
        self.emotion_model = pipeline("text-classification", 
                                    model="j-hartmann/emotion-english-distilroberta-base")


    def detect_mood(self, text):
        """
        Detect mood from input text using BERT-based model.
        
        Args:
            text (str): Input text to analyze
            
        Returns:
            str: Detected emotion/mood
        """
        predictions = self.emotion_model(text)
        print(predictions)

        return predictions[0]['label'].lower() 