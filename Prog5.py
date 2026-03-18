with open('charge_accounts.txt','r') as accounts:
    input1=0
    while True:
        input1=input("Enter Account Number: ")
        if len(str(abs(input1)))!=7:
            print("Invalid Input")
        else:
            break
    nums=accounts.readline().strip()
    acc_list = [int(i) for i in nums]
    try:
        acc_list.index(input1)
        print("Valid Input")
    except:
        print("Invalid Input")
    