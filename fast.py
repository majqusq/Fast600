import random
import os

nums = []

print('How many draws?')


while True:
    try:
        drawAmount = int(input())
        if drawAmount > 0:
            break
        else:
            print('Amount of draws must be higher than 0')
    except ValueError:
        print('Amount of draws must be a number')
    

for l in range(drawAmount):
    losowanie = []
    loop = [1,2,3,4,5,6]
    for i in loop:      
        x = random.randint(1,32)
        if x not in losowanie:
            losowanie.append(x)
        else:
            loop.append(1)
    nums.extend(losowanie)       
values = []
nums.sort()
highest = {}
temporary = {}
for num in nums:
    amount = nums.count(num)
    temporary[num]=amount
    if num not in values:
        if num in [1,2,3,4,5,6,7,8,9]:
            print(num,'  ',end='')
            for lol in range(amount):
                print('=',end='')
            print(amount,'')
            values.append(num)
        else:
            print(num,' ',end='')
            for lol in range(amount):
                print('=',end='')
            print(amount,'')
            values.append(num)
print(max(temporary))
        

print(highest)

os.system('pause')
