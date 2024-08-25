# Convert strings to integers
hours = int(input())
minutes = int(input())
# Check for input error
if hours < 0 or minutes < 0 or minutes >= 60:
    print("Input Error!") 
# Calculate the total time in minutes
total_time = hours * 60 + minutes
# Check for free parking conditions
if total_time <= 15:
    print("No charge, thanks.") 
# Calculate the charge
if hours < 3:
    charge = 10
else:
    # For every hour or part thereof past 2 hours, add 10 Baht
    charge = 10 + ((hours - 2) * 10)
print(f"Total amount due is {charge} Bahts.")