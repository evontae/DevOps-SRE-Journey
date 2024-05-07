'''System Health Dashboard:
Create a Python script that aggregates system health information (CPU load, disk usage, memory usage) and writes it to an output file formatted for easy reading. Optionally, extend this script to run at regular intervals using a scheduling tool like cron.'''

# Import OS module for getting information on the system, datetime and time for getting the current time and setting a time interval for the scheduler, also including schedule to run the script
import psutil, datetime, time, schedule

# Get system health information, this include cpu percentage, disk usage, RAM, uptime and Network metrics
cpu_usage_percent = psutil.cpu_percent()
disk_usage = psutil.disk_usage('/')
memory_usage = psutil.virtual_memory()
network_usage = psutil.net_io_counters()
boot_time = psutil.boot_time()

# Place system metrics in a dict so that printing will be easier
health_information = [
    ('CPU Usage', f'Percent:{cpu_usage_percent}%'),
    ('Disk Usage', f'Percent:{disk_usage.percent}%'),
    ('Memory Usage', f'Percent:{memory_usage.percent}%'),
    ('Network Metrics', {'Bytes Sent': network_usage.bytes_sent,
                         'Bytes Received': network_usage.bytes_recv,
                        'Packets Sent': network_usage.packets_sent,
                        'Packets Received': network_usage.packets_recv}),
    ('System Uptime' ,f'Time:{datetime.datetime.fromtimestamp(boot_time)}')
]
# Geting current time will use in the writing to show metrics at a certain time
ctime = datetime.datetime.now()
formatted_time = ctime.strftime('%I:%M %b %d %Y')

# Setting up function to run task every hour
def job():
    # Open System Health file, append the write, loop through the dict to print the metrics, a time stamp is added for each write
    with open("c:/Users/DTone/Desktop/SRE/DevOps-SRE-Journey/Python/Practice/system_health.txt", "a") as file:
        file.write(f'Metrics as of: {formatted_time}\n\n')
        # Prints the name and vaule
        for name, value in health_information:
            file.write(f'{name}:\n')
            # Checks for inner dicts in the dict to print the metrics as well
            if isinstance(value, dict):
                for sub_name, sub_value in value.items():
                    file.write(f'  {sub_name}: {sub_value}\n')
            else:
                file.write(f'  {value}\n')
        file.write('\n')    
    # Print message to the console to say the script has been run    
    print('System health has been writtien to system_health.txt')
schedule.every(1).hour.do(job)

# Loop to start the script and run it, the loop sleeps most of an hour to save processing power
while True:
    schedule.run_pending()
    time.sleep(3500)  # Sleep for 3500 seconds to avoid CPU intensive looping
