"""
Word Occurrences
Estimated Completion Time: 15-20 minutes
Actual Completion Time: 17 minutes
"""
string = str(input("Enter a sentence to evaluate word occurrences: "))
word_to_count = {}
split_words = string.split(" ")
for word in split_words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

split_words = list(word_to_count.keys())
split_words.sort()

for word in split_words:
    print(f"{word} : {word_to_count[word]}")
