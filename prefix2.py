def find_common_prefixes(strings):
  if not strings:
    return {}

  grouped_strings = {}
  for s in strings:
    if s:
      first_char = s[0]
      if first_char not in grouped_strings:
        grouped_strings[first_char] = []
      grouped_strings[first_char].append(s)

  result_prefixes = {}
  for first_char, string_list in grouped_strings.items():
    string_list.sort()
    first_str = string_list[0]
    last_str = string_list[-1]
    prefix = ""

    for i in range(min(len(first_str), len(last_str))):
      if first_str[i] == last_str[i]:
        prefix += first_str[i]
      else:
        break

    if prefix:
      result_prefixes[first_char] = prefix

  sorted_prefixes = [result_prefixes[key] for key in sorted(result_prefixes.keys())]
  return ",".join(sorted_prefixes)
string_list = ['present','perfect','predetermine','preface']
output = find_common_prefixes(string_list)
print(output)

string_list2 = ["apple", "apricot", "banana", "blueberry", "cat"]
output2 = find_common_prefixes(string_list2)
print(output2)

string_list3 = ["", "hello", "hi"]
output3 = find_common_prefixes(string_list3)
print(output3)

string_list4 = []
output4 = find_common_prefixes(string_list4)
print(output4)
