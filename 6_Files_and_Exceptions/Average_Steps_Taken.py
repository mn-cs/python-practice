# #12 Average Steps Taken (15 points)
# A Personal Fitness Tracker is a wearable device that tracks your 
# physical activity, calories burned, heart rate, sleeping patterns,
# and so on. One common physical activity that most of these devices
# track is the number of steps you take each day.

# A file named steps.txt Download steps.txtcan be downloaded. 
# The steps.txt file contains the number of steps a person has taken
# each day for a year. There are 365 lines in the file, and each line
# contains the number of steps taken during a day. (The first line is
# the number of steps taken on January 1st, the second line is the 
# number of steps taken on January 2nd, and so forth.) Write a program
# that reads the file, then displays the average number of steps taken
# for each month. (The data is from a year that was not a leap year, 
# so February has 28 days.)

# Create a file (name it 'lastname_avg.txt', use your lastname)  with:

# (1) Heading explaining the contents of the file. (3 points)
# (2) Have two columns - Month and AVERAGE steps taken. (3 points)
# (3) Then the values for each month. (9 points)

# NOTE: Upload the steps.txt to your repl.it and it will 
#       be available for reading.



days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

with open("steps.txt", "r") as infile, open("pashinyan_avg.txt", "w") as outfile:
    outfile.write("The average number of steps taken for each month\n")
    outfile.write("------------------------------------\n")
    outfile.write("Month          AVERAGE steps taken\n")
    outfile.write("------------------------------------\n")

    for idx, day in enumerate(days):
        acc = 0
        for _ in range(day):
            acc += int(infile.readline())
        avg = acc / day
        acc = 0
        outfile.write(f"{months[idx]:<17}{str(avg)}\n")




#      output: The average number of steps taken for each month
#              ------------------------------------
#              Month          AVERAGE steps taken
#              ------------------------------------
#              January          5246.096774193548
#              February         4851.857142857143
#              March            5777.612903225807
#              April            5802.133333333333
#              May              4711.548387096775
#              June             4792.333333333333
#              July             5638.225806451613
#              August           5759.645161290323
#              September        6114.566666666667
#              October          5411.032258064516
#              November         4268.8
#              December         5138.064516129032




Jan_check = [
1102,
9236,
10643,
2376,
6815,
10394,
3055,
3750,
4181,
5452,
10745,
9896,
255,
9596,
1254,
2669,
1267,
1267,
1327,
10207,
5731,
8435,
640,
5624,
1062,
3946,
3796,
9381,
5945,
10612,
1970]

print(sum(Jan_check) / 31)


Dec_check = [
5967,
3156,
5919,
2855,
5985,
1780,
6267,
6303,
9855,
3843,
1816,
2876,
5973,
2888,
709,
6509,
4320,
10342,
2616,
4887,
10470,
6084,
4573,
2457,
10205,
4627,
7927,
1703,
5034,
7042,
4292,]

print(sum(Dec_check) / 31)