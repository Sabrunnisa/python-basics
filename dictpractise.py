words = eval(input("enter:"))

grouped_words = {}

for word in words:
  first_letter = word[0]
  if first_letter in grouped_words:
    grouped_words[first_letter].append(word)
  else:
    grouped_words[first_letter] = [word]

# Now, convert the dictionary of lists into the desired list of lists
result = []
for key in sorted(grouped_words.keys()):  # Sorting keys for consistent output order
  result.append(grouped_words[key])
print(result)
