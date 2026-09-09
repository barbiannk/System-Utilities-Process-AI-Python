# You can use this file to work on the activity
## add in missing import
import sys
import psutil

def get_process_info():
    """
    Retrieves and displays information about all active system processes.
    Output includes PID, process name, memory usage %, and CPU usage %.
    """

    # Define column headers with consistent spacing
    header = f"{'PID':<10} {'Name':<25} {'Memory %':<10} {'CPU %':<10}"
    print(header)
    print("-" * len(header))
    
    # Iterate through all running processes and extract relevant info
    # Will use something like this
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent', 'cpu_percent']):
      ##uncommented for variables block
        try:
            ## All of these will bve retrieved from the for variable 'proc' above
            ##Extract values from the proc.info dictionary
            ## get the PID and name
            pid = proc.info['pid']
            name = proc.info['name']
            ## get the memory_percent
            ## and get the cpu_percent
            ## go back to 0.0 if returns none
            mem = proc.info['memory_percent'] or 0.0
            cpu = proc.info['cpu_percent'] or 0.0

            # Print formatted process details retrieved from above
            print(f"{pid:<10} {name:<25} {mem:<10.2f} {cpu:<10.2f}")

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Skip processes that can't be accessed or no longer exists
            continue

def main() -> int:
  print("Starting Program")
  print("================")
  get_process_info()
  ## add return statement for main
  return 0

if __name__ == "__main__":
    # Entry point for the script
    sys.exit(main())