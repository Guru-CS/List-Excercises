with open("WorldSeriesWinners.txt",'r') as winners:
    name=input("Enter Team Name: ").lower()
    winners_list=[line.strip().lower() for line in winners]
    count=winners_list.count(name)
    print(f"{name.capitalize()} has won the World Series {count} times.")