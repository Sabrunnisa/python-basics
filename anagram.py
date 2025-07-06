# Sample list of strings
words_list = input("w:")
word=words_list.split()

# Initialize count
count = 0

# Iterate through each word in the list
for i in words_list:
    # Check if the word is not empty and first and last characters are the same (case-insensitive)
    if i and i[0].lower() == i[-1].lower():
        count += 1

# Print the result
print(f"Number of words that start and end with the same letter: {count}")



word1 = "Listen"
word2 = "Silent"

print(sorted(word1.lower()))  # ['e', 'i', 'l', 'n', 's', 't']
print(sorted(word2.lower()))  # ['e', 'i', 'l', 'n', 's', 't']

# Since the sorted lists are equal:
are_anagrams = sorted(word1.lower()) == sorted(word2.lower())

print(are_anagrams)  # True




from collections import Counter

word1 = "Listen"
word2 = "Silent"

print(Counter(word1.lower()))  # Counter({'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1})
print(Counter(word2.lower()))  # Counter({'s': 1, 'i': 1, 'l': 1, 'e': 1, 'n': 1, 't': 1})

# Since counters are equal:
are_anagrams = Counter(word1.lower()) == Counter(word2.lower())

print(are_anagrams)  # True
