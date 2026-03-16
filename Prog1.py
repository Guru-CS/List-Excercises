days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
amounts = []

for day in days:
    amount = float(input(f"Enter Sales for {day}: "))
    amounts.append(amount)
    
print(f"Total Sales for the Week: {sum(amounts)}")