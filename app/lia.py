from empath import Empath

lexicon = Empath()

LIA_CATEGORIES = [
    "positive_emotion", "negative_emotion", "joy", "anger", "sadness",
    "violence", "confusion", "affection", "work", "money", "home", "love"
]

def analyze_lia(text: str) -> dict:
    results = lexicon.analyze(text, categories=LIA_CATEGORIES, normalize=True)
    return results
