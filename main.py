# Your friend Bob is a somewhat weird person. He has two obsessions in his life: his digital clock and divisibility. His digital clock displays the time in the 24-hour format (i.e., the first minute of a day is 00:00, and the last minute of a day is 23:59), and one of Bob’s favorite hobbies is to pick a random number 1x9 and just watch his clock until all 4 digits of the display are divisible by x (assume 0 is divisible by every number).

# Given an arbitrary number x (between 1 and 9) and an arbitrary current time y in the 24-hour format described above, how many minutes will Bob have to wait until the clock displays a time such that all 4 digits of the time are perfectly divisible by x? For example, if x is 3 and y is 03:23, the answer is 7 minutes, because 7 minutes after y would be 03:30, and all 4 digits of this resulting time are divisible by x.

import random

x = random.randrange(1, 10)
hour_ten = random.randrange(3)
if hour_ten == 2:
  hour_one = random.randrange(4)
else:
  hour_one = random.randrange(10)
min_ten = random.randrange(6)
min_one = random.randrange(10)
y = [hour_ten, hour_one, min_ten, min_one]
print("x:", x)
print("Time:", y)

def find_problem(x, y):
  for i in y:
    if i % x != 0:
      problem = y.index(i)
      return problem
  return 4

def min_one_diff(x, y):
  return wait_time

def min_ten_diff(x, y):
  min_one_diff(x, y)

def hour_one_diff(x, y):
  min_ten_diff(x, y)

def hour_ten_diff(x, y):
  hour_one_diff(x, y)