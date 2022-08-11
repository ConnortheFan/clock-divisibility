# Your friend Bob is a somewhat weird person. He has two obsessions in his life: his digital clock and divisibility. His digital clock displays the time in the 24-hour format (i.e., the first minute of a day is 00:00, and the last minute of a day is 23:59), and one of Bob’s favorite hobbies is to pick a random number 1x9 and just watch his clock until all 4 digits of the display are divisible by x (assume 0 is divisible by every number).

# Given an arbitrary number x (between 1 and 9) and an arbitrary current time y in the 24-hour format described above, how many minutes will Bob have to wait until the clock displays a time such that all 4 digits of the time are perfectly divisible by x? For example, if x is 3 and y is 03:23, the answer is 7 minutes, because 7 minutes after y would be 03:30, and all 4 digits of this resulting time are divisible by x.

import random


def find_problem(x, time):
  '''
  Finds and returns the index in time where the problem is. If there is no problem, return 4.
  '''
  for i in time:
    if i % x != 0:
      problem = time.index(i)
      return problem
  return 4
  
wait_time = 0

def format_time(time):
  formatted_time = "Time: "
  formatted_time += str(time[0])
  formatted_time += str(time[1])
  formatted_time += ":"
  formatted_time += str(time[2])
  formatted_time += str(time[3])
  return formatted_time

def convert_clock(time):
  '''
  Converts time into proper time format
  '''
  if time[3] == 10:
    time[3] = 0
    time[2] += 1
  if time[2] == 6:
    time[2] = 0
    time[1] += 1
  if time[0] != 2:
    if time[1] == 10:
      time[1] = 0
      time[0] += 1
  if time[0] == 2:
    if time[1] == 4:
      time[0] = 0
      time[1] = 0
  return time

def find_wait_time(x, time):
  global wait_time
  while find_problem(x, time) != 4:
    wait_time += 1
    time[3] += 1
    time = convert_clock(time)
  print("Wait time:", wait_time, "minutes")
  print("New time:", format_time(time))
  return wait_time

# Create x as a random digit 1 to 9
x = random.randrange(1, 10)

# Create time as a random list of valid digits
hour_ten = random.randrange(3)
if hour_ten == 2:
  hour_one = random.randrange(4)
else:
  hour_one = random.randrange(10)
min_ten = random.randrange(6)
min_one = random.randrange(10)
time = [hour_ten, hour_one, min_ten, min_one]

print("x:", x)
print(format_time(time))
find_wait_time(x, time)

