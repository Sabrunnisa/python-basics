# Number of rows
n = int(input("enter number of rows:"))

# Upper part of the hollow diamond
for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")
    
    # Print stars and hollow space
    if i == 1:
        print("*")  # Print the first row with just one star
    else:
        print("*", end="")  # Print the first star
        for j in range(2 * i - 3):
            print(" ", end="")  # Print hollow space
        print("*")  # Print the last star

# Lower part of the hollow diamond
for i in range(n - 1, 0, -1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")
    
    # Print stars and hollow space
    if i == 1:
        print("*")  # Print the last row with just one star
    else:
        print("*", end="")  # Print the first star
        for j in range(2 * i - 3):
            print(" ", end="")  # Print hollow space
        print("*")  # Print the last star

    
