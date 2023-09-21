def fibonacci_memoization(n, memo):
    if n in memo:
        return memo[n]
    if n < 2:
        memo[n] = n
    else:
        memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
    return memo[n]

def fibonacci(n):
    memo = {}
    return fibonacci_memoization(n, memo)

n=8
print(fibonacci(n))

import psutil
import logging

# Configure the logging module
logging.basicConfig(
    filename='psutil_stats.log',  # Specify the log file name
    level=logging.INFO,          # Set the logging level to INFO
    format='%(asctime)s [%(levelname)s]: %(message)s',  # Define log message format
    datefmt='%Y-%m-%d %H:%M:%S'  # Define date and time format
)

# Define a function to log CPU and memory usage
def log_cpu_memory_usage():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    logging.info(f'CPU Usage: {cpu_percent}% - Memory Usage: {memory_percent}%')

# Run the logging function periodically
while True:
    log_cpu_memory_usage()
