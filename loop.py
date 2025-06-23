import psutil
import time
import socket

threshold_percentage = 50
included_processes = ['CTFarm.exe']  # Processes to monitor, not terminate
computer_name = socket.gethostname()
log_file = f"{computer_name}.txt"

def log_cpu_usage():
    with open(log_file, "a") as f:
        for process in psutil.process_iter(['name', 'cpu_percent']):
            process_name = process.info['name']
            cpu_percent = process.info['cpu_percent']
            if cpu_percent > threshold_percentage and process_name not in ['System Idle Process', 'python.exe']:
                f.write(f"{process_name} : {cpu_percent}%\n")

def main():
    while True:
        processes_exceeded_threshold = False

        for process in psutil.process_iter(['name', 'cpu_percent']):
            process_name = process.info['name']
            cpu_percent = process.info['cpu_percent']

            if process_name in included_processes and cpu_percent > threshold_percentage:
                print(f"[Monitor] {process_name} is using high CPU: {cpu_percent}%")

            if cpu_percent > threshold_percentage:
                processes_exceeded_threshold = True

        if processes_exceeded_threshold:
            log_cpu_usage()

        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    main()
