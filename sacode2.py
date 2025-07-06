from collections import defaultdict

def common_prefix(str1, str2):
    length = min(len(str1), len(str2))
    i = 0
    while i < length and str1[i] == str2[i]:
        i += 1
    return str1[:i]

def longest_prefix_shared_by_at_least_two(strs):
    max_prefix = ""
    n = len(strs)
    for i in range(n):
        for j in range(i + 1, n):
            prefix = common_prefix(strs[i], strs[j])
            if len(prefix) > len(max_prefix):
                max_prefix = prefix
    return max_prefix

def group_by_starting_letter(words):
    groups = defaultdict(list)
    for word in words:
        if word:  # ignore empty strings
            groups[word[0]].append(word)
    return groups

def count_words_with_prefix(words, prefix):
    return sum(1 for word in words if word.startswith(prefix))

# Input list
words =eval(input("enter list of strings:"))

# Group words by their starting letter
groups = group_by_starting_letter(words)

# Dictionary to store prefix and count
prefix_count_dict = {}

# Iterate each group and find longest prefix shared by at least two words
for letter, group in groups.items():
    if len(group) < 2:
        # Not enough words to compare, skip or store empty prefix with count 1
        continue
    longest_prefix = longest_prefix_shared_by_at_least_two(group)
    if longest_prefix:
        count = count_words_with_prefix(group, longest_prefix)
        prefix_count_dict[longest_prefix] = count

# Print the dictionary
print(prefix_count_dict)

# Step 1: Find the maximum value
max_value = max(prefix_count_dict.values())

# Step 2: Get all keys with the maximum value
max_keys = [key for key, value in prefix_count_dict.items() if value == max_value]

print("Keys with the maximum value:", max_keys)
print("Maximum value:", max_value)
