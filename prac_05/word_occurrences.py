"""
Word Occurrences
Estimated Completion Time: 15-20 minutes
Actual Completion Time:
"""
string = str(input("Enter a sentence to evaluate word occurrences: "))
word_to_count = {}
words = string.split(" ")
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

for word in words:
    print(f"{word} : {word_to_count[word]}")
