# This script will consume memory by continuously appending large lists to an array.
memory_hog = []
while True:
    memory_hog.append([0] * 10**6)  # Allocate ~8MB per iteration
