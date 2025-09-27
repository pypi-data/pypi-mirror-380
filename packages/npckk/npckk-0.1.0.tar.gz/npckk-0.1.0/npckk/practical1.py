def a():
    return "Practical 1: Text Analytics using Manual Dictionary – Identification of words in text and counting the number of times it occurs"


def a1():
    return """text = "This is my test text. We're keeping this text short to keep things manageable."
text = text.lower()"""


def a2():
    return """def count_words(text):
    skips = [".", ",", ":", ";", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts"""


def a3():
    return """num = count_words(text)"""


def a4():
    return """print(num)"""
