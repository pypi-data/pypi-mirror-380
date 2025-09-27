def c():
    return "Practical 3: Sentiment Analysis with NLTK VADER"


def c1():
    return """import nltk
nltk.download("vader_lexicon")"""


def c2():
    return """from nltk.sentiment import SentimentIntensityAnalyzer"""


def c3():
    return """s = SentimentIntensityAnalyzer()"""


def c4():
    return """text = "I hate this product very much\""""


def c5():
    return """score = s.polarity_scores(text)"""


def c6():
    return """print(score)"""


def c7():
    return """def interpret_sentiment(score):
    compound = score["compound"]
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral\""""


def c8():
    return """print(interpret_sentiment(score))"""
