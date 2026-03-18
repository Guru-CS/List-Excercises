
rand_nums=[]
for _ in range(20):
    rand_nums.append(int(input("Enter An Integer: ")))
print(f"Highest Num: {max(rand_nums)}")
print(f"Lowest Num: {min(rand_nums)}")
print(f"Sum of Nums: {sum(rand_nums)}")
print(f"Avg of Nums: {sum(rand_nums)/len(rand_nums)}")