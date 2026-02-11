# Task 2: Using math module
import math

# User input
num = float(input("Enter a number: "))

# Calculations
sqrt_num = math.sqrt(num)
log_num = math.log(num)        # Natural log (base e)
sine_num = math.sin(num)       # In radians

# Display results
print(f"Square root of {num} is: {sqrt_num}")
print(f"Natural log of {num} is: {log_num}")
print(f"Sine of {num} is: {sine_num}")