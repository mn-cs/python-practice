# 8. Sum of Numbers (15 points)

# Write a program with a loop that asks the user to enter a series of 
# positive numbers.

# The user should enter a negative number to signal the end of the series. 

# After all the positive numbers have been entered, the program should 
# display their sum.

# Must use while loop (6 points)

# Check your program with at least three values: 5, 10, -5 (3 points)

# Display/Print the results. (3 points)

# Include as a comment in your program the response from your program 
# when you run it with each of the above values.  Are the values as 
# expected? (3 points)



acc = 0

while True:
  try:
    inp = int(input("Enter a positive number (or a negative number to end): "))
    if inp > 0:
      acc += inp
      continue
    elif inp < 0:
      break
  except ValueError:
    print("* Enter a valid integer")

print("The Sum is: ", acc)


#  Test 1:
#         Input: Enter a positive number (or a negative number to end): 5
#                Enter a positive number (or a negative number to end): 10
#                Enter a positive number (or a negative number to end): -5
#        Output: The Sum is:  15

#  Test 2:
#         Input: Enter a positive number (or a negative number to end): 4
#                Enter a positive number (or a negative number to end): 8
#                Enter a positive number (or a negative number to end): 11
#                Enter a positive number (or a negative number to end): 55
#                Enter a positive number (or a negative number to end): -1
#        Output: The Sum is:  78

#  Test 3:
#         Input: Enter a positive number (or a negative number to end): 2
#                Enter a positive number (or a negative number to end): 2
#                Enter a positive number (or a negative number to end): 6
#                Enter a positive number (or a negative number to end): -5
#        Output: The Sum is:  10