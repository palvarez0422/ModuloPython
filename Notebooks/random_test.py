import numpy as np
import matplotlib as plt

# Seed the random number generator
np.random.seed(42)

# Initialize random numbers: random_numbers
random_numbers = np.empty(100000)

# Generate random numbers by looping over range(100000)
for i in range(100000):
    random_numbers[i] = np.random.random()

# Plot a histogram
_ = plt.hist(random_numbers)

_ = plt.xlabel('value')

# Show the plot
plt.show()

if __name__ == '__main__':
    print('Hola mundo')



