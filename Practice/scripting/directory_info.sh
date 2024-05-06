#!/bin/bash

# Script Creation (directory_info.sh):
# Write a script that:
# Checks if a specified directory exists.
# Lists its contents including hidden files.
# Outputs the details to a file with a time-stamped filename.
# Changes permissions to ensure the script is executable.

# initialize variable for directory
directory="/Users/evo/path/DevOps-SRE-Journey/Practice/scripting"

# Use if statement to check to see if the directory exsists, if not then create it
if [ ! -d "$directory" ]; then
    mkdir "$directory"
fi 

# List all the elements in the variabel directory then redirect to current_directory.txt file
ls -a > "$directory/$(date +%Y%m%d_%H%M%S)_directory.txt"

# Changing permissions to ensure the file can run
chmod u+x $0