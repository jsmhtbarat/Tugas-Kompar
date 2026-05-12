# Import Pool for multiprocessing
from multiprocessing import Pool

# Import time module to simulate processing delay
import time


# Function executed by each process
# Each process performs the SAME task
# but with DIFFERENT data
def calculate_square(number):

    # Display the number being processed
    print(f"Processing number: {number}")

    # Simulate computation time
    time.sleep(1)

    # Calculate square value
    result = number * number

    # Display calculation result
    print(f"Square result of {number} = {result}")

    # Return result to the main process
    return result


# Main program entry point
if __name__ == "__main__":

    # Different data values to process
    data = [1, 2, 3, 4, 5, 6, 7, 8]

    # Create 4 parallel worker processes
    # Pool distributes data automatically
    with Pool(processes=4) as pool:

        # map() sends each data item
        # to calculate_square() in parallel
        results = pool.map(calculate_square, data)

    # Display final combined results
    print("\nAll Results:")
    print(results)
