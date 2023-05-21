import random

ans = random.randint(1, 100)
min_num = 1
max_num = 100

while True:
    n = int(input(f'請{min_num} {max_num}輸入數字:'))
    
    if n == ans:
        print('恭喜答對')
        break
    elif n > ans:
        max_num = n
        print('太大了')
    elif n < ans:
        min_num = n
        print('太小了')