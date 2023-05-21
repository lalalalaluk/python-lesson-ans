import sys
# 你好
txt = sys.stdin.read()

input = txt.splitlines()

for one_input in input:
    max_list = []
    max_number = 0
    counter = 0
    for n in one_input:
        if int(n) >= max_number:
            counter += 1
            max_number = int(n)
        elif int(n) < max_number:
            max_list.append(counter)
            counter = 1
            max_number = int(n)
            continue
    max_list.append(counter)

    print(max(max_list))
