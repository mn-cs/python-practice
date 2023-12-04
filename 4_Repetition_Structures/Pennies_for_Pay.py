# 7. Pennies for Pay. (15 points)

# Write a program that calculates the amount of money a person would 
# earn over a period of time if his or her salary is one penny the 
# first day, two pennies the second day, and continues to double each 
# day. The program should ask the user for the number of days. Display
# a table showing what the salary was for each day, then show the total
# pay at the end of the period. The output should be displayed in a 
# dollar amount, not the number of pennies.

# Must use for loop statement. (3 points)

# Need to check the input value is correct, otherwise an error message 
# is displayed. (3 points)

# Display a nicely formatted table. Display the salary in dollar and 
# cents, it should be formatted correctly. (9 points)


day = int()

while True: 
  try:
    inp = int(input("Enter a number of days: "))
    if inp < 1:
      print("* Enter a pozitive number")
      continue
    
  except ValueError:
    print("* Enter a valid integer for a day")
    continue

  break

print("\n Day |   Salery")
print("-" * 30)

salery = 0.0
total = 0.00

for day in range(1, inp + 1):
  
  if day > 2:
    salery *= 2
    print(f"{day : >3}  |   ${salery : <20,.2f}")
  else:
    salery += 0.01
    print(f"{day : >3}  |   ${salery : <6}")
  total += salery
  
print("-" * 30)
print(f"Total Days:  {inp}")
print(f"Total Salery: ${total:,.2f}")
    
  

#  Test 1:
#       Input:   Enter a number of days: 5
#
#       Output:    Day |   Salery
#                 ------------------------------
#                   1  |   $0.01  
#                   2  |   $0.02  
#                   3  |   $0.04                
#                   4  |   $0.08                
#                   5  |   $0.16                
#                 ------------------------------
#                 Total Days:  5
#                 Total Salery: $0.31

#  Test 2:
#       Input:   Enter a number of days: 11
#
#       Output:    Day |   Salery
#                 ------------------------------
#                    1  |   $0.01  
#                    2  |   $0.02  
#                    3  |   $0.04                
#                    4  |   $0.08                
#                    5  |   $0.16                
#                    6  |   $0.32                
#                    7  |   $0.64                
#                    8  |   $1.28                
#                    9  |   $2.56                
#                   10  |   $5.12                
#                   11  |   $10.24               
#                ------------------------------
#                Total Days:  11
#                Total Salery: $20.47
