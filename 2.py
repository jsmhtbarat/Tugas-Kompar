# Import ThreadPoolExecutor for multithreading
from concurrent.futures import ThreadPoolExecutor

# Import time module to simulate task duration
import time


# Task 1: Download data
def download_data():

    # Display task status
    print("Starting data download...")

    # Simulate downloading time
    time.sleep(2)

    # Display completion message
    print("Download completed")


# Task 2: Process data
def process_data():

    print("Starting data processing...")

    # Simulate processing time
    time.sleep(3)

    print("Processing completed")


# Task 3: Save report
def save_report():

    print("Saving report...")

    # Simulate saving time
    time.sleep(1)

    print("Report successfully saved")


# Main program entry point
if __name__ == "__main__":

    # Create thread pool with 3 worker threads
    with ThreadPoolExecutor(max_workers=3) as executor:

        # Execute different tasks simultaneously
        executor.submit(download_data)
        executor.submit(process_data)
        executor.submit(save_report)
