import matplotlib.pyplot as plt
with open("expenses.txt",'r') as expenses_file:
    expenses = [float(line.strip()) for line in expenses_file]
    categories = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment',"Misc"]
    plt.pie(expenses, labels=categories)
    plt.title('Monthly Expenses')
    plt.show()