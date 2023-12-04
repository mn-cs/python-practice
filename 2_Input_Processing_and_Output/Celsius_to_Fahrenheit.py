# (a)  Celsius to Fahrenheit Temperature Converter. (15 points)

# Write a program that converts Celsius temperatures to Fahrenheit
# temperatures.

# The formula is as follows: F=9/5*C+32

# The program should ask the user to enter a temperature in Celsius,

# then display the temperature converted to Fahrenheit.

# There is a value that has the same numerical value in both scales.
#  Use your program to verify it.  (10 points)
# Test your programs for 0, 100 and 78 degrees Celsius. Include the
#  output as comments in your program. (2 points)

# Can you solve the equation algebraically and verify it with your program.
#  Need to upload the steps of you proof and the value which is same. (3 points)


# convertor
def convert(n):
  return 9 / 5 * n + 32

# ask the user to enter a temperature in Celsius
input = float(input("Enter a temperature in Celsius: "))

print(f'\n {convert(input):.0f} Fahrenheit\n')

for i in range(-100, 101):
  if i == convert(i):
    print(f'{i:.0f} degrees Celsius is equal to {i:.0f} degrees Fahrenheit.')

# 0 Celsius equal to 32 Fahrenheit
# 100 Celsius equal to 212 Fahrenheit
# 78 Celsius equal to 172 Fahrenheit

# Algebraic proof
print("""
\n Algebraic proof: \n
F = (9/5) * C + 32  
C = (9/5) * C + 32
C * 5 = ((9/5) * 5) * C + 32 * 5 
5C = 9C + 160
5C - 9C = 160 
-4C = 160
-4C / -4 = 160 / -4 
C = -40
""")
