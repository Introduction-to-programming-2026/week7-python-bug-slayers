# Project 4 — Word Counter
# Author: your name here

sentence = input("Enter a sentence: ")
words = sentence.lower().split()

# TODO: total word count using len()

# TODO: character count (no spaces)
# Hint: sentence.replace(" ", "") removes all spaces, then use len()

# TODO: word frequency dictionary
# frequency = {}
# for word in words:
#     ...

# TODO: print total words, total characters, then word frequency



# Project 4 — Word Counter
# Author: your name here

sentence = input("Enter a sentence: ")
words = sentence.lower().split()

# total word count
total_words = len(words)

# character count (no spaces)
char_count = len(sentence.replace(" ", ""))

# word frequency dictionary
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# print results
print("Total words:", total_words)
print("Total characters (no spaces):", char_count)
print("Word frequency:", frequency)