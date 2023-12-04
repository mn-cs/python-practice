# Exercise 4. Roman Numerals. (10 points)

# Write a program that prompts the user to enter a 
# number within the range of 1 through 10. The program 
# should display the Roman numeral version of that number.
# (3 points)

# If the number is outside the range of 1 through 10, the 
# program should display an error message. (3 points)

# Prints an appropriate response. (4 points)


arr = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

while True:
  try:
    inp = int(input("Enter the number within the range of 1 through 10: "))
    
    if inp < 1:
      print("* The number can not be lower then 1")
      continue
    if inp > 10:
      print("* The number can not be higher then 10")
      continue
      
  except ValueError:
    print("* Enter a velid Integer")
    continue
    
  break
    
print(f"The Roman numeral version: {arr[inp - 1]}")


# Test 1:
#      Input:  Enter the number within the range of 1 through 10: 1
#      output: The Roman numeral version: I

# Test 2:
#      Input:  Enter the number within the range of 1 through 10: 5
#      output: The Roman numeral version: V

# Test 2:
#      Input:  Enter the number within the range of 1 through 10: 10
#      output: The Roman numeral version: X

    