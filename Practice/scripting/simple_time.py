# Write a Python script that outputs the current date and time.

# Import dateime module will use this to capture the exact moment in time
import datetime

# Assign the current moment in time to variable ctime using the dateime.dateime.now method
ctime = datetime.datetime.now()

# Format the current time method
formated_time = ctime.strftime('%I:%M %b %d %Y ')

# Print out current time
print(f'The current time is: {formated_time}')