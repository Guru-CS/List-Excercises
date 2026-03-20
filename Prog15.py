# In the student sample programs for this book, you will find a text file named 1994_Weekly_Gas_Averages.txt. The file contains the average gas price for each week in the year 1994. (There are 52 lines in the file.) Using matplotlib, write a Python program that reads the contents of the file then plots the data as either a line graph or a bar chart. Be sure to display meaningful labels along the X and Y axes, as well as the tick marks.

import matplotlib.pyplot as plt
with open("1994_Weekly_Gas_Averages.txt", 'r') as file:
    gas_prices = [float(line.strip()) for line in file]
weeks = list(range(1, len(gas_prices) + 1))
plt.plot(weeks, gas_prices, marker='o')
plt.xlabel('Week')
plt.ylabel('Gas Price')
plt.title('1994 Weekly Gas Averages')
plt.show()