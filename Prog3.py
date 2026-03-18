months = [
    "January", "February", 
    "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

rainfall = []
for month in months:
    rainfall.append(float(input(f"Enter Inches of Rainfall for {month}: ")))
highest = [i for i, x in enumerate(rainfall) if x == max(rainfall)]
highest_months=[]
for i in highest:
    highest_months.append(months[i])
lowest = [i for i, x in enumerate(rainfall) if x == min(rainfall)]
lowest_months=[]
for i in lowest:
    lowest_months.append(months[i])
print(f"Month(s) with Most Rainfall: {highest_months}")
print(f"Month(s) with Least Rainfall: {lowest_months}")
print(f"Total Rainfall: {sum(rainfall)} Inches")
print(f"Avg Rainfall: {sum(rainfall)/len(rainfall):.2f} Inches")