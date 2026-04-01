# List of delivery times in minutes
delivery_times = [25, 40, 35, 50, 20]

# Threshold to consider a delivery as delayed
delay_threshold = 30

delayed_deliveries = 0

# Count number of delayed deliveries
for delivery_time in delivery_times:
    if delivery_time > delay_threshold:
        delayed_deliveries += 1

# Calculate delay percentage
total_deliveries = len(delivery_times)
delay_percentage = (delayed_deliveries / total_deliveries) * 100

# Display results
print("Total Deliveries:", total_deliveries)
print("Delayed Deliveries:", delayed_deliveries)
print("Delay Percentage:", delay_percentage)