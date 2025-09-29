#!/usr/bin/env python3
"""
Example demonstrating signal handling in the scheduler.

This example shows how to use the new signal handling features:
1. Schedulers will automatically stop on SIGTERM, SIGINT (Ctrl+C), and SIGBREAK (Ctrl+Break on Windows)
2. You can manually request shutdown using request_shutdown()
3. You can use wait_for_shutdown() to block until a signal is received
4. You can check if shutdown was requested using is_shutdown_requested()
"""

import time
import logging
from scheduler_pkg import scheduled, request_shutdown, is_shutdown_requested

# Setup logging to see what's happening
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Counter to track how many times the task has run
task_counter = 0

@scheduled(minute='*/1')  # Run every minute
def my_scheduled_task(scheduler, current_time):
    global task_counter
    task_counter += 1
    logger.info(f"Task executed #{task_counter} at {current_time}")
    
    # Simulate some work
    time.sleep(2)
    
    # Example: manually request shutdown after 5 executions
    if task_counter >= 5:
        logger.info("Task has run 5 times, requesting shutdown...")
        request_shutdown()


ftask_counter = 0
ftask_counter2 = 0

@scheduled("at * on * freq 100/hour")
def my_frequent_task(scheduled_plan, current_time):
    global ftask_counter
    ftask_counter += 1
    logger.info(f"Frequent task executed #{ftask_counter} at {current_time}")
    
    # Simulate some work
    time.sleep(1)

@scheduled("at * on * freq 120/hour")
def my_frequent_task2(scheduled_plan, current_time):
    global ftask_counter2
    ftask_counter2 += 1
    logger.info(f"Frequent task2 executed #{ftask_counter2} at {current_time}")
    
    # Simulate some work
    time.sleep(1)

def wait_for_shutdown(check_interval=1):
    """
    Wait for shutdown signal in a blocking manner.
    
    This function can be used in main threads to wait for termination signals
    instead of using infinite loops or sleep. It will return when a shutdown
    signal is received.
    
    Args:
        check_interval (float): How often to check for shutdown signal in seconds.
                               Default is 1 second.
    """
    try:
        while not is_shutdown_requested():
            time.sleep(check_interval)
    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt received, initiating shutdown...")
        request_shutdown()
    
    logger.info("Shutdown signal received, exiting wait_for_shutdown()")


def main():
    logger.info("Starting scheduler example with signal handling...")
    logger.info("Press Ctrl+C to gracefully stop the scheduler")
    logger.info("The scheduler will also stop automatically after the task runs 5 times")
    
    # The @ScheduledRun decorator has already started the scheduler in the background
    
    try:
        # Wait for shutdown signal (blocks until signal received)
        wait_for_shutdown()
    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt caught in main, requesting shutdown...")
        request_shutdown()
    
    # Give some time for background threads to finish
    timeout = 10
    logger.info(f"Waiting up to {timeout} seconds for background tasks to finish...")
    for i in range(timeout):
        time.sleep(1)
        if not is_shutdown_requested():
            break
    
    logger.info(f"Scheduler stopped. Task ran {task_counter} times total.")

if __name__ == "__main__":
    main()
