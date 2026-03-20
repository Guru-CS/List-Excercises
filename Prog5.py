with open('charge_accounts.txt','r') as accounts:
    input1=0
    while True:
        input1=int(input("Enter Account Number: "))
        if len(str(abs(input1)))!=7:
            print("Invalid Input")
        else:
            break
    nums=accounts.readlines()
    acc_list = [int(i.strip()) for i in nums]
    try:
        acc_list.index(input1)
        print("Valid Input")
    except:
        print("Invalid Input")
    