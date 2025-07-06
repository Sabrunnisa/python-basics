import re

def is_palindrome(text):
    text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return text == text[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
