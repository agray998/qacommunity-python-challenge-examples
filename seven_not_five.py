nums = ""
for i in range(2000, 3201):
    nums += (str(i) + ',') * (i % 7 == 0 and i % 5 != 0)

print(nums)