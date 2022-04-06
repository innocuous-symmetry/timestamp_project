from datetime import datetime
from time import time

timestamp1 = "Feb 12 08:02:32 2014"
timestamp2 = "Feb 21 11:52:02 2014"

converted1 = datetime.strptime(timestamp1, "%b %d %H:%M:%S %Y")
converted2 = datetime.strptime(timestamp2, "%b %d %H:%M:%S %Y")

print(converted1)
print(converted2)

difference = converted2 - converted1
days_extracted = difference.days

print(difference)

def days_to_minutes(days):
    hours = days * 24
    minutes = hours * 60
    return minutes

print(days_to_minutes(days_extracted))