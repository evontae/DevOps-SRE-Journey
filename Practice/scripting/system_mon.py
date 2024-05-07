# Develop a Python script that checks the current disk usage and sends an alert (prints a message) if it exceeds 80% capacity.

import os

# Get the current directory, which will be used for checking disk usage
cwd = os.getcwd()

# Get disk space information for the current filesystem
disk_stat = os.statvfs(cwd)

# Get the total file size
total_size_files = disk_stat.f_bsize * disk_stat.f_blocks

# Calculate block size as a percentage of total size
block_size_percentage = (disk_stat.f_frsize / total_size_files) * 100

# Check if block size is 80% or more of total size
if block_size_percentage >= 80:
    # Send a desktop notification
    message = "Disk usage exceeds 80%!"
    os.system("notify-send 'Disk Usage Alert' '{}'".format(message))
else:
    print(f"The block size is not significant compared to the total size.")