# ------------------------------------------------------------
# Word Frequency Counter
# Description:
#   Counts occurrences of each word in a given text.
# Author: Abhishek Rana
# ------------------------------------------------------------

from collections import Counter

def word_count(text):
    words = text.lower().split()
    return Counter(words)

if __name__ == "__main__":
    text = input("Enter your text: ")
    counts = word_count(text)
    for word, freq in counts.items():
        print(f"{word}: {freq}")
