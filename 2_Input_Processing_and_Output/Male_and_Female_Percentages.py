# (b) Male and Female Percentages (15 points)
# Write a program that asks the user for the number
# of males and the number of females registered in a class.
# (5 points)

# The program should display the percentage of males and
# females in the class. (5 points)

# Hint: Suppose there are 8 males and 12 females in a class. There
# are 20 students in the class. The percentage of males can be
# calculated as 8 ÷ 20 = 0.4, or 40%. The percentage of females can
# be calculated as 12 ÷ 20 = 0.6, or 60%.

males = int(input('Enter the number of males registered: '))
females = int(input('Enter the number of females registered: '))

sum = males + females

print('\n')
print(f'Percentage of males: {males / sum * 100:.0f}%')
print(f'Percentage of females: {females / sum * 100:.0f}%')
