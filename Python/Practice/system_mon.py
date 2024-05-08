# Develop a Python script that checks the current disk usage and sends an alert (prints a message) if it exceeds 80% capacity.

import os

# Get the current directory, which will be used for checking disk usage
cwd = os.getcwd()

# Get disk space information for the current filesystem
disk_stat = os.statvfs(cwd)

# Updated calculation on blocks
total_blocks = disk_stat.f_blocks
free_blocks = disk_stat.f_bfree
used_blocks = total_blocks - free_blocks
disk_usage_percentage = (used_blocks / total_blocks) * 100

if disk_usage_percentage >= 80:
    message = "Disk usage exceeds 80%!"
    os.system(f"notify-send 'Disk Usage Alert' '{message}'")
else:
    print(f"Current disk usage is {disk_usage_percentage:.2f}%. Capacity is within normal limits.")
