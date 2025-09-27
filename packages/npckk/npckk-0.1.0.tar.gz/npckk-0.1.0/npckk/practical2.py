def b():
    return "Practical 2: Text Analytics using Counter – Faster word frequency analysis in text"


def b1():
    return """text = "This is my test text. We're keeping this text short to keep things manageable."""


def b2():
    return """from collections import Counter"""


def b3():
    return """def count_words_fast(text):
    text = text.lower()
    skips = [".", ",", ":", ";", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts"""


def b4():
    return """num = count_words_fast(text)"""


def b5():
    return """print(num)"""
