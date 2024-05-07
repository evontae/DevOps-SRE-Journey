# Write a script that reads a log file and counts the number of occurrences of different error levels (INFO, WARNING, ERROR).
import fileinput

# Open file set as read, set varible content as the read file
with open("log.txt", "r") as file:
    content = file.readlines()

# Set counter varibles for errors, info and warning
err = 0
inf = 0
wrn = 0
    
# Iterate over each line in content to check the log type and add the type to its count    
for lines in content:
    if "ERROR" in lines:
        err += 1
    elif "INFO" in lines:
        inf +=1
    elif "WARNING" in lines:
        wrn +=1 
 
# Print out final count, formatted for ease of reading        
print(f'Counting Error, Warning & Info occurances...\nThere are exactly {err} Errors, {inf} info & {wrn} warnings in the log file.')