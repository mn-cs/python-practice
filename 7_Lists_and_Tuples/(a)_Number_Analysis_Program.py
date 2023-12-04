# The two exercises are related. Build your program in a modular way,
# then you need to only change the function that builds the list.

# (a) Number Analysis Program (15 points)

# Must use at least 2 functions. One function to get input values, 
# one to display the results and main to invoke these two.  For 
# input values use:  1,2,3...,18,19,20  (10 points)

# Display a formatted message for output  (5 points)


def get_input_values():
  return list(range(1, 21))

def display_results(numbers):

  total = sum(numbers)
  average = total / len(numbers)
  lowest = min(numbers)
  highest = max(numbers)
  
  print("---------------------------------------------")
  print(f"The lowest number in the list: {lowest}")
  print(f"The highest number in the list: {highest}")
  print(f"The total of the numbers in the list: {total}")
  print(f"The average of the numbers in the list: {average:.2f}")
  print("----------------------------------------------")
  print(f"The list of the numbers: {numbers}")
  
def main():
  
  numbers = get_input_values()
  display_results(numbers)

if __name__ == "__main__":
  main()




#    output:
#           ---------------------------------------------
#           The lowest number in the list: 1
#           The highest number in the list: 20
#           The total of the numbers in the list: 210
#           The average of the numbers in the list: 10.50
#           ---------------------------------------------
#           The list of the numbers: [1, 2, 3, 4, 5, 6, 7, 
#                                     8, 9, 10, 11, 12, 13, 14,
#                                    15, 16, 17, 18, 19, 20]