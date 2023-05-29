
sum = 0
with open("numbers.txt", mode="r") as file:
    for line in file:
        sum += int(line)

print('總共: ' + str(sum))