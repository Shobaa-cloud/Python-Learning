prices=[7,1,5,3,6,4]
min= prices[0]
max = 0
for i in prices:
    if i < min:
        min = i
    profit = i - min
    if profit > max:
        max = profit
print(max)