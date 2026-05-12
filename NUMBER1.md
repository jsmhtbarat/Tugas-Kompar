# Tugas-Kompar
# Number 1 Data parallelism  (for even NRP), shows  when the code execute different data

from multiprocessing import Pool
import time

# Function executed in parallel
def calculate_square(number):
    print(f"Processing number: {number}")
    time.sleep(1)

    result = number * number

    print(f"Square result of {number} = {result}")

    return result


if __name__ == "__main__":

    # Different data
    data = [1, 2, 3, 4, 5, 6, 7, 8]

    # Create 4 parallel processes
    with Pool(processes=4) as pool:
        results = pool.map(calculate_square, data)

    print("\nAll Results:")
    print(results)
