def is_palindrome_after_cleaning(text):
  """
  Checks if a string is a palindrome after removing non-alphanumeric characters
  and converting to lowercase.

  Args:
    text: The input string.

  Returns:
    True if the cleaned string is a palindrome, False otherwise.
  """
  cleaned_chars = []
  for char in text:
    # Check if the character is alphanumeric
    if char.isalnum():
      # Convert to lowercase
      cleaned_chars.append(char.lower())

  # Join the cleaned characters back into a string
  cleaned_text = "".join(cleaned_chars)

  # Check if the cleaned string is a palindrome
  n = len(cleaned_text)
  # We only need to compare the first half with the second half reversed
  for i in range(n // 2):
    # Compare character at index i with character at index n - 1 - i
    if cleaned_text[i] != cleaned_text[n - 1 - i]:
      return False # Not a palindrome if characters don't match

  # If the loop completes without finding mismatches, it's a palindrome
  return True

# The input string
input_string = "le#$34vel43*&"

# Check if the cleaned string is a palindrome
if is_palindrome_after_cleaning(input_string):
  print(f"'{input_string}' the output should be it is palindrome after removing the non alphanumeric values")
else:
  print(f"'{input_string}' the output should be it is NOT a palindrome after removing the non alphanumeric values")
