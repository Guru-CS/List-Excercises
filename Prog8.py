with open("popular_names.txt", "r") as names:
    name_list = names.readlines()
    name_list = [i.strip().lower() for i in name_list]
    inp_name = input("Enter a name: ")
    if inp_name.strip().lower() in name_list:
        print("That name was popular.")
    else:
        print("That name was not popular.")