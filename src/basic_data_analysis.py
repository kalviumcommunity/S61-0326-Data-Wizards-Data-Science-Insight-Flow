# Basic Data Analysis Script

# Sample dataset: A list of daily temperatures in Celsius for a week
temperatures = [22, 25, 19, 28, 24, 21, 26]

# Calculate basic statistics
total_sum = sum(temperatures)
average_temp = total_sum / len(temperatures)
minimum_temp = min(temperatures)
maximum_temp = max(temperatures)

# Print results in a readable format
print("Basic Data Analysis Results")
print(f"Sample Dataset: {temperatures}")
print(f"Sum of temperatures: {total_sum}°C")
print(f"Average temperature: {average_temp:.2f}°C")
print(f"Minimum temperature: {minimum_temp}°C")
print(f"Maximum temperature: {maximum_temp}°C")
