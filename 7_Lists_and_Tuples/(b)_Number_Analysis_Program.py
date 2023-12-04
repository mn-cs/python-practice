# (b) Number Analysis Program (15 points)

# This is a minor modification of the problem from (a) above. 
# Instead of asking the user for input values, generate 20 
# random numbers between 1 & 100.

# TIP:
# --------------------------------------------

# import random
#        print (random.randint(1,100))
# Will print a random number between 1 and 100.
# --------------------------------------------------
# (10 points) The program should store the numbers in a list
#   (using the random number generator) then display the 
#   following data:

# The lowest number in the list

# The highest number in the list

# The total of the numbers in the list

# The average of the numbers in the list

# IN ADDITION, display the list so the values calculated 
# can be verified. (5 points)


import random


def generate_random_numbers():
    return [random.randint(1, 100) for _ in range(20)]
def display_results(numbers):

    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    print("---------------------------------------------")
    print(f"The lowest number in the list: {lowest}")
    print(f"The highest number in the list: {highest}")
    print(f"The total of the numbers in the list: {total}")
    print(f"The average of the numbers in the list: {average:.2f}")
    print("----------------------------------------------")
    print(f"The list of the numbers: {numbers}")

def main():
    numbers = generate_random_numbers()
    display_results(numbers)

if __name__ == "__main__":
    main()


#   one of the outputs:
# 
#           ---------------------------------------------
#           The lowest number in the list: 5
#           The highest number in the list: 100
#           The total of the numbers in the list: 1066
#           The average of the numbers in the list: 53.30
#           ----------------------------------------------
#           The list of the numbers: [60, 59, 20, 78, 24, 56, 78, 
#                                     10, 97, 65, 40, 5, 74, 40, 
#                                     68, 41, 100, 68, 17, 66]