# (a) Capital Quiz
# Write a program that creates a dictionary containing the U.S.
# states as keys, and their capitals as values. (Use the Internet
# to get a list of the states and their capitals.) (5 points)

# The program should then randomly quiz the user by displaying 
# the name of a state and asking the user to enter that state’s
# capital. The program should loop until the user wishes to quit.
# (5 points)

# The program should keep a count of the number of correct and 
# incorrect responses.  The score should be displayed when the 
# user does not wish to continue playing. (3 points)

# Display a formatted message for output  (2 points)


import random


def main():
  
    state_capitals = {
        'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
        'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
        'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
        'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
        'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
        'Michigan': 'Lansing', 'Minnesota': 'St. Paul', 'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
        'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
        'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
        'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
        'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
        'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
        'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
    }

    correct = 0
    incorrect = 0

    while True:

        state, capital = random.choice(list(state_capitals.items()))

        response = input(f"What is the capital of {state}? (Enter 'quit' to exit) ").strip()

        if response.lower() == 'quit':
            break

        elif response.lower() == capital.lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect. The correct answer is {capital}.")
            incorrect += 1

    print("\n")
    print("   * Thank you for playing! *")
    print("-" * 34)
    print(f"You got {correct} correct and {incorrect} incorrect.")

if __name__ == '__main__':
    main()