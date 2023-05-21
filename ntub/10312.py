import sys

text = sys.stdin.read()

test_data = text.splitlines()

for t in test_data[1:]:
  a, b ,c ,d = map(int , t.split(','))
  for i in range(0, a):
    if b * i + c * (a-i) == d:
      print(f'{i},{a-i}')