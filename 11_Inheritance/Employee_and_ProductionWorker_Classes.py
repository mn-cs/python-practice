# (a) Employee and ProductionWorker Classes
# Write an Employee class that keeps data attributes for the following
# pieces of information:
#    Employee name
#    Employee number
# Next, write a ProductionWorker class named that is a subclass of
# Employee class. The class should keep data
# attributes for the following information:
#    Shift number (an integer, such as 1, 2, or 3)
#    Hourly pay rate
# The workday is divided into two shifts: day and night. The shift
# attribute will hold an integer value representing the shift that
# the employee works. The day shift is shift 1 and the night shift
# is shift 2.

# Write the appropriate accessor and mutator methods for each class.

# Once you have written the classes, write a program that creates an
# object of the class and prompts the user to enter data for each of
# the object’s data attributes. (20 points)

# Store the data in the object, then use the object’s accessor methods
# to retrieve it
# and display it on the screen. (10 points)




from productionWorker import ProductionWorker


def main():

  name = input("Enter the employee's name: ")
  number = input("Enter the employee's number: ")
  shift = input("Enter the shif (1 for day, 2 for night): ")
  pay = float(input("Enter the hourly pay: "))

  worker = ProductionWorker(name, number, shift, pay)

  print("\nEmployee Information")
  print("-" * 20)
  print(f"Name: {worker.get_name()}")
  print(f"Number: {worker.get_number()}")
  print(f"Shift: {worker.get_shift()}")
  print(f"Pay: ${worker.get_pay():.2f}")
  print("-" * 20)


if __name__ == "__main__":
  main()
