# (a). Sum of Digits in a String
# Write a program that asks the user to enter a series of single-digit
# numbers with nothing separating them.

# The program should display the sum of all the single digit numbers
# in the string.

# For example, if the user enters 2514, the method should return 12,
# which is the sum of 2, 5, 1, and 4.

# Must use functions. One function to get input values,  a function
# to do the calculation and one to display the results and main to
# invoke them.    (10 points)

# Display a formatted message for output  (5 points)

# Test your program on these inputs:

# 5

# 1212

# 123456789

# Be aware of the due dates, after Sunday the assignment will close
# and no more submission. Do not send submissions as email attachments
# or in comments of the assignment.


def get_input_values():
  print("* Nothing should separate the Numbers *")
  print("-" * 39)
  return input("Enter a series of single-digit numbers: ")


def calculation(v):
  return sum(int(i) for i in v)


def display_results(v):
  print(f"The sum of all numbers in the string is: {v}")
  print("-" * 39)


def main():
  user_inp = get_input_values()
  calulated = calculation(user_inp)
  display_results(calulated)


if __name__ == "__main__":
  main()

# Test 1:
#     Input: 5
#    Output: * Nothing should separate the Numbers *
#            ---------------------------------------
#            Enter a series of single-digit numbers: 5
#            The sum of all numbers in the string is: 5
#            ---------------------------------------

# Test 2:
#     Input: 1212
#    Output: * Nothing should separate the Numbers *
#            ---------------------------------------
#            Enter a series of single-digit numbers: 1212
#            The sum of all numbers in the string is: 6
#            ---------------------------------------

# Test 3:
#     Input: 123456789
#    Output: * Nothing should separate the Numbers *
#            ---------------------------------------
#            Enter a series of single-digit numbers: 123456789
#            The sum of all numbers in the string is: 45
#            ---------------------------------------
