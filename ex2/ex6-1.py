
total = int(input())

mod3_0 = 0
mod3_1 = 0
mod3_2 = 0

for i in range(total):
    num = int(input())
    if num % 3 == 0:
        mod3_0 += 1
    elif num % 3 == 1:
        mod3_1 += 1
    else:
        mod3_2 += 1

print(mod3_0, mod3_1, mod3_2)

