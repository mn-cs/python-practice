# (a). Car Class
# Write a class named  Car that has the following data attributes:
#   __year_model (for the car’s year model)
#   __make (for the make of the car)
#    __speed (for the car’s current speed)


# The Car class should have an __init__ method that accepts the car’s
#  year model and make as arguments. These values should be
# assigned to the object’s __year_model and __make data attributes.
# It should also assign 0 to the __speed data attribute.
# The class should also have the following methods:

# Accelerate
#     The method should add 5 to the speed data attribute each time it is called.

# Brake
#     The method should subtract 5 from the speed data attribute each time it is called.

# get_speed
#    The method should return the current speed.


# Next, design a program that creates a Car object. (10 points)

# Then call Accelerate  method five times.  After each call to 
# the Accelerate method, get the current speed of the car and 
# display it. (5 points) 

# Then call  the Brake method five times. After each call to 
# the method, get the current speed of the car and display it.  (5 points)


import car


def main():

  my_car = car.Car(2008, "Kia")

  print()

  for i in range(5):
    my_car.accelerate()
    print(f"Current speed after acceleration {i + 1}: {my_car.get_speed()} mph")

  print("-" * 44)

  for i in range(5):
    my_car.brake()
    print(f"Current speed after brake {i + 1}: {my_car.get_speed()} mph")

if __name__ == "__main__":
  main()
