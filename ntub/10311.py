import sys

txt = sys.stdin.read()

a = txt.splitlines()

for e in a[1:]:
  a, b = e.split(',')
  a = int(a)
  b = int(b)
  if abs(a - b) != 2:
    print('N')
    continue

  trigger = 0
  for a1 in range(2, a):
    if a % a1 == 0:
      print('N')
      trigger = 1
      break
  if trigger == 1:
    continue

  for b1 in range(2, b):
    if b % b1 == 0:
      print('N')
      trigger = 1
      break
  if trigger == 1:
    continue
  print('Y')
