#programmed By Eric Thomas and Rayan Haq
# Loyola CS151, Professor Zee
# Due date 10/1/24
# Lab assignment: 03

import math

# Ask user for hill type and speed
hill_type = input("Enter the hill type (normal/large): ").lower()
speed = float(input("Enter the jumper's speed (in meters per second): "))

# Initialize variables for constants
height = 0
points_per_meter = 0
par = 0

# Set constants based on hill type using if statements
if hill_type == "normal":
    height = 46
    points_per_meter = 2
    par = 90
elif hill_type == "large":
    height = 70
    points_per_meter = 1.8
    par = 120
else:
    print("Invalid hill type! Please enter either 'normal' or 'large'.")
    exit()

# Distance and time calculations
time_in_air = math.sqrt((2 * height) / 9.8)
distance = speed * time_in_air

# Points calculation
points = 60 + (distance - par) * points_per_meter

# Output the results
print(f"Distance traveled: {distance:.2f} meters")
print(f"Points scored: {points:.2f}")

# Display feedback based on points scored
if points >= 61:
    print("Great job for doing better than par!")
elif points <= 10:
    print("What happened?? Sorry, you didn’t go very far.")
