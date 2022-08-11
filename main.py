# Your friend Bob is a somewhat weird person. He has two obsessions in his life: his digital clock and divisibility. His digital clock displays the time in the 24-hour format (i.e., the first minute of a day is 00:00, and the last minute of a day is 23:59), and one of Bob’s favorite hobbies is to pick a random number 1x9 and just watch his clock until all 4 digits of the display are divisible by x (assume 0 is divisible by every number).

# Given an arbitrary number x (between 1 and 9) and an arbitrary current time y in the 24-hour format described above, how many minutes will Bob have to wait until the clock displays a time such that all 4 digits of the time are perfectly divisible by x? For example, if x is 3 and y is 03:23, the answer is 7 minutes, because 7 minutes after y would be 03:30, and all 4 digits of this resulting time are divisible by x.

import random
