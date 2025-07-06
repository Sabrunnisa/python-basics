def is_even_list_comprehension_string(numbers):
  """
  Creates a list of strings ("true" or "false") indicating whether each number
  in the input list is even using a list comprehension.

  Args:
    numbers: A list of numbers (integers or floats).

  Returns:
    A list of strings ("true" or "false").
  """
  return ["true" if number % 2 == 0 else "false" for number in numbers]

# Sample Input List:
numbers = eval(input("enter list of numbers:"))

# Get Sample Output:
output = is_even_list_comprehension_string(numbers)

# Print Sample Output:
print("Input:", numbers)
print("Output:", output)

["true" if number % 2 == 0 else "false" for number in numbers]
