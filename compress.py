def compress_string(input_string):
  if not input_string:
    return ""

  compressed = []
  count = 1
  current_char = input_string[0]

  for i in range(1, len(input_string)):
    if input_string[i] == current_char:
      count += 1
    else:
      compressed.append(current_char)
      compressed.append(str(count))
      current_char = input_string[i]
      count = 1
  compressed.append(current_char)
  compressed.append(str(count))

  return "".join(compressed)
input_string = input()
output_string = compress_string(input_string)
print(output_string)
