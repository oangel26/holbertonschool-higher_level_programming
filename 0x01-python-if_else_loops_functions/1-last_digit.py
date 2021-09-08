#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
if int(num[-1]) == 0:
    print("Last digit of {} is {} and is 0".format(number, int(num[-1])))
elif int(num) < 0:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, int(num[-1]) * -1))
elif int(num[-1]) < 6:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, int(num[-1])))
elif int(num[-1]) > 5:
    print("Last digit of {} is {} and and is greater than 5"
          .format(number, int(num[-1])))
else:
    pass
