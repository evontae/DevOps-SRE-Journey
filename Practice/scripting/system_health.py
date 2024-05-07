'''System Health Dashboard:
Create a Python script that aggregates system health information (CPU load, disk usage, memory usage) and writes it to an output file formatted for easy reading. Optionally, extend this script to run at regular intervals using a scheduling tool like cron.'''

# Import OS module for getting information on the system
import psutil, datetime, time, schedule

# Get system health information, this include cpu percentage, disk usage, RAM, uptime and Network metrics
cpu_usage_percent = psutil.cpu_percent()
disk_usage = psutil.disk_usage('/')
memory_usage = psutil.virtual_memory()
network_usage = psutil.net_io_counters()
boot_time = psutil.boot_time()

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
    # Write metrics to a file neames system_health.txt, setting permissions to append
    with open("c:/Users/DTone/Desktop/SRE/DevOps-SRE-Journey/Practice/scripting/system_health.txt", "a") as file:
        file.write(f'Metrics as of: {formatted_time}\n\n')
        for name, value in health_information:
            file.write(f'{name}:\n')
            if isinstance(value, dict):
                for sub_name, sub_value in value.items():
                    file.write(f'  {sub_name}: {sub_value}\n')
            else:
                file.write(f'  {value}\n')
        file.write('\n')    
        
    print('System health has been writtien to system_health.txt')
schedule.every(1).minute.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for 1 second to avoid CPU intensive looping
