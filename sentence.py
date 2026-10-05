import random

sentences = [
    "Python is easy to learn and fun to use.",
    "Practice makes a person perfect.",
    "Typing speed improves with regular practice.",
    "Learning programming helps us solve problems.",
    "Technology makes our life easier."
]

def get_sentence():
    return random.choice(sentences)
