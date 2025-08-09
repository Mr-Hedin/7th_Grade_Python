"""
Welcome to the Great Algorithm Race! 🏎️
Let's see which search algorithm is faster!
"""

import time
import random
import algorithms

# Here we're calling the prepare_a_list function from the algorithms module we created.
data_set = algorithms.prepare_a_list()

# We'll find a random target value to search that is within the range of the data_set we just generated.
search_value = random.randint(1,len(data_set))

# Below, we'll start calling our toolkit of functions to time them!

# To race the algorithms, we need to run them multiple times and take the average time to get a fair comparison.

# To time an algorithm we'll use time.time()... to get the time. time.time() returns the current time in seconds since the beginning of the program.

# We'll use the time.time() function to get the start time 
# run the algorithm
# then use the time.time() function again to get the end time of the algorithm.

# We'll then find the difference between the end time and start time to get the time it took to run the algorithm.



# Out of our algorithms, we'll time our linear search and binary search first. 
# Since these two algorithms are very similar, timing them is a good comparison.
start_time = time.time()
algorithms.linear_search(data_set, search_value)
end_time = time.time()
linear_time = end_time - start_time
print(linear_time)

start_time = time.time()
algorithms.binary_search(data_set, search_value)
end_time = time.time()
binary_time = end_time - start_time
print(binary_time)

# We'll also time our other algorithms to see how they perform.
# Let's time them using the same process.

start_time = time.time()
algorithms.calculate_sum(data_set)
end_time = time.time()
sum_time = end_time - start_time
print(sum_time)

start_time = time.time()
algorithms.calculate_average(data_set)
end_time = time.time()
average_time = end_time - start_time
print(average_time)

start_time = time.time()
algorithms.find_min(data_set)
end_time = time.time()
min_time = end_time - start_time
print(min_time)

start_time = time.time()
algorithms.find_max(data_set)
end_time = time.time()
max_time = end_time - start_time
print(max_time)


# Side note: if we were thinking efficiently, we could have used the same process for all of our algorithms.
# We could have created a function that takes an algorithm as an argument in order to time it.
# This would have made our code more flexible and reusable, but functions as arguments are often trickier than they seem, so we'll save that for another day!



"""Display the race results in a fun way."""
print("\n🏆 Race Results 🏆")
print("=" * 40)

# Convert times to milliseconds for easier reading
linear_ms = linear_time * 1000
binary_ms = binary_time * 1000

print(f"Linear Search:")
print(f"⏱️  Time: {linear_ms:.2f} milliseconds")

print(f"\nBinary Search:")
print(f"⏱️  Time: {binary_ms:.2f} milliseconds")

# Determine the winner
print("\n🎯 And the winner is...")
if binary_time < linear_time:
    print("🥇 BINARY SEARCH! 🥇")
    print(f"Binary Search was {(linear_time/binary_time):.1f}x faster!")
elif linear_time < binary_time:
    print("🥇 LINEAR SEARCH! 🥇")
    print(f"Linear Search was {(binary_time/linear_time):.1f}x faster!")
else:
    print("🤝 It's a tie!")
