def is_palindrome(s):
    cleaned = ""
    
    for char in s:
        if char.isalnum():
            cleaned += char.lower()
    
    return cleaned == cleaned[::-1]

user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
