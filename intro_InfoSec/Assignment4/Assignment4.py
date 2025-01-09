#--------------------
# CS 458            |
# Assignment 4      |
# Nam Gyu Lee       |
#--------------------

import random
from collections import Counter
import time
import matplotlib.pyplot as plt

# Part 1 - (a)
import hashlib

hash = hashlib.sha256('Nam Gyu Lee'.encode())
value = hash.hexdigest()

print("\nPart 1 - (a)")
print(f"SHA-256 Hash value in hexadecimal: {value}")

# Part 1 - (b), (c)
# Function of generating random number and append to rand_input list
def random_input(num_input):
    random_inputs = []
    for i in range(num_input):
        rand_num = random.randint(0, 10 ** 8)
        random_inputs.append(str(rand_num))
    
    return random_inputs

# Function of counting bits
def count_bits(random_inputs):
    bits_counts = []
    for input in random_inputs:
        # SHA-256 calculation
        hash_value = hashlib.sha256(input.encode()).hexdigest()

        # After convert hexadecimal to binary, count 1-bits
        bits_count = bin(int(hash_value, 16)).count("1")
        bits_counts.append(bits_count)
    
    return bits_counts

# function that measures the time it takes to hash
def hashing_time(num_input):
    inputs = random_input(num_input)
    start_time = time.time()

    bits_counts = count_bits(inputs)
    end_time = time.time()
    
    time_difference = end_time - start_time
    hashing_sec = num_input / time_difference

    return time_difference, hashing_sec, bits_counts


num_input = 10000
times, second, bits_counts = hashing_time(num_input)
# Count the frequency of 1-bit
histogram = Counter(bits_counts)

# Print 1-bit count histogram
print("\nPart 1 - (b)")
print("1-bits count histogram:")
for bit_count, frequency in sorted(histogram.items()):
    print(f"{bit_count} bits: {frequency} occurrences")

# Visualize histogram
plt.bar(histogram.keys(), histogram.values(), color='blue', alpha=0.7)
plt.xlabel("Number of 1-bits")
plt.ylabel("Frequency")
plt.title("Histogram of 1-bits Counts with SHA-256")
plt.show()

print("\nPart 1 - (c)")
print(f"Overall time for {num_input} hashes: {times:.6f} seconds")
print(f"Hashes per second: {second:.2f}")

num_2_128 = 2 ** 128
num_2_256 = 2 ** 256

time_2_128 = num_2_128 / second
time_2_256 = num_2_256 / second

# Convert seconds to year
years_2_128 = time_2_128 / (60 * 60 * 24 * 365)
years_2_256 = time_2_256 / (60 * 60 * 24 * 365)
print(f"Time to compute 2^128 hashes: {years_2_128:.2e} years")
print(f"Time to compute 2^256 hashes: {years_2_256:.2e} years")
print("")