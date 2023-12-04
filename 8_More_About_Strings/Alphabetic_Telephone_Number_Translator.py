# 5. Alphabetic Telephone Number Translator (15 points)

# Many companies use telephone numbers like 555-GET-FOOD
# so the number is easier for their customers to remember.

# On a standard telephone, the alphabetic letters are mapped
# to numbers in the following fashion:

# A, B, and C = 2
# D, E, and F = 3
# G, H, and I = 4
# J, K, and L = 5
# M, N, and O = 6
# P, Q, R, and S = 7
# T, U, and V = 8
# W, X, Y, and Z = 9

# Write a program that asks the user to enter a 10-character
# telephone number in the format XXX-XXX-XXXX.

# The application should display the telephone number with any
# alphabetic characters that appeared in the original translated
# to their numeric equivalent. For example, if the user enters
# 555-GET-FOOD, the application should display 555-438-3663.

# Must use at least 2 functions. One function to get input values,
# one to display the results and main to invoke these two. (8 points)

# Display a formatted message for output  (5 points)

# Test your program on multiple inputs and include the output as
# comments in your program.   (2 points)


def get_input_values():
  print("* The Format Should be: XXX-XXX-XXXX *")
  print("* For Example: 555-GET-FOOD          *")
  print("-" * 38)
  return input("Enter a 10-character phone number: ")


def get_numeric_equivalent(char):
  char = char.upper()
  if char in 'ABC':
    return '2'
  elif char in 'DEF':
    return '3'
  elif char in 'GHI':
    return '4'
  elif char in 'JKL':
    return '5'
  elif char in 'MNO':
    return '6'
  elif char in 'PQRS':
    return '7'
  elif char in 'TUV':
    return '8'
  elif char in 'WXYZ':
    return '9'
  else:
    return char


def convert_phone_number(phone_number):
  numeric_phone_number = ""
  for char in phone_number:
    numeric_phone_number += get_numeric_equivalent(char)
  return numeric_phone_number


def display_phone_number(n):
  print(f"The Numeric phone number is: {n}")
  print("-" * 38)


def main():

  user_inp = get_input_values()
  converted = convert_phone_number(user_inp)
  display_phone_number(converted)


if __name__ == "__main__":
  main()

# Test 1:
#       Input: 555-GET-FOOD
#      Output: * The Format Should be: XXX-XXX-XXXX *
#              * For Example: 555-GET-FOOD *
#              --------------------------------------
#              Enter a 10-character phone number: 555-GET-FOOD
#              Numeric phone number: 555-438-3663
#              --------------------------------------

# Test 2:
#       Input: 555-get-food
#      Output: * The Format Should be: XXX-XXX-XXXX *
#              * For Example: 555-GET-FOOD *
#              --------------------------------------
#              Enter a 10-character phone number: 555-get-food
#              Numeric phone number: 555-438-3663
#              --------------------------------------

# Test 3:
#       Input: 555-NEW-YEAR
#      Output: * The Format Should be: XXX-XXX-XXXX *
#              * For Example: 555-GET-FOOD *
#              --------------------------------------
#              Enter a 10-character phone number: 555-NEW-YEAR
#              Numeric phone number: 555-639-9327
#              --------------------------------------
