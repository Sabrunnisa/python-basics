def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
user_input = input("Enter a list of strings separated by commas: ")
strings_list = user_input.split(",")
result = longest_common_prefix([s.strip() for s in strings_list])
print("Longest common prefix:", result)
