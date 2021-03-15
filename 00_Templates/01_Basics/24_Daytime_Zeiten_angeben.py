# https://docs.python.org/2/library/datetime.html

import datetime

# Get Current Date and Time
datetime_object = datetime.datetime.now()
print(datetime_object)

datetime_time = datetime.time()
print(datetime_time,"_")

# Get Current Date
date_object = datetime.date.today()
print(date_object)


# Format date using strftime() - https://www.programiz.com/python-programming/datetime
now = datetime.datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)

currenttime = now.strftime("%Y%m%d_%H%M%S")
# mm/dd/YY H:M:S format
print("Formatierte Zeit:", currenttime)


#What's inside datetime?
#We can use dir() function to get a list containing all attributes of a module.

print(dir(datetime))

