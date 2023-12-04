# (a) Calories from Fat and Carbohydrates  (15 points)

# A nutritionist who works for a fitness club helps members by evaluating
# their diets. As part of her evaluation, she asks members for the number 
# of fat grams and carbohydrate grams that they consumed in a day. (4 points)

# Then, she calculates the number of calories that result from the fat, 
# using the following formula: calories from fat=fat grams × 9  (2 points)

# Next, she calculates the number of calories that result from the 
# carbohydrates, using the following formula:
# calories from carbs=carb grams × 4  (2 points)


# The nutritionist asks you to write a program that will make these 
# calculations. Display the results in a nicely formatted way.  (3 points)



def main():
  
  while True:
    try:
      
      fat, carb = input_values()
      
      print("\nResults:")
      print(f"Calories from fat: {cal_from_fat(fat):.2f} calories")
      print(f"Calories from carbs: {cal_from_carb(carb):.2f} calories")
      break

    except ValueError:
      print("* Enter a valid number")
      continue

def input_values():
  fat = float(input("Enter a number of fat in grams: "))
  carb = float(input("Enter a number of carbohydrate in grams: "))
  return fat, carb

def cal_from_fat(fat):
  return fat * 9
    
def cal_from_carb(carb):
  return carb * 4

main()


# Test 1:
#      input: Enter a number of fat grams: 5.11
#             Enter a number of carbohydrate grams: 57.2
#     output: Results:
#             Calories from fat: 45.99 calories
#             Calories from carbs: 228.80 calories

# Test 2:
#      input: Enter a number of fat grams: 157
#             Enter a number of carbohydrate grams: 289
#     output: Results:
#             Calories from fat: 1413.00 calories
#             Calories from carbs: 1156.00 calories