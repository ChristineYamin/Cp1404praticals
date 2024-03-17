"""
Word Occurrences
Estimate: 20 minutes
Actual:   40 minutes
"""


word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    if word in word_to_count:
        word_to_count[word] +=1
        # print(word,word_to_count[word])
    else:
        word_to_count[word] =1
        # print(word,word_to_count[word])

words = list(word_to_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
