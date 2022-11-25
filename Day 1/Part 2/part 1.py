import pathlib
text = pathlib.Path('Day 1\Part 2\input_test.txt').read_text().split('\n')
numbers = [int(line) for line in text]

i = 0
o = 1
z = 2
t = 3
higher = 0
sum_1 = 0
sum_2 = 0

while t < len(numbers):
  sum_1 = numbers[i] + numbers[o] + numbers[z]
  sum_2 = numbers[o] + numbers[z] + numbers[t]

  if sum_2 > sum_1:
    higher = higher + 1
    i = i + 1
    o = o + 1
    z = z + 1
    t = t + 1

  else:
    i = i + 1
    o = o + 1
    z = z + 1
    t = t + 1

print(f"Higher ist jetzt: {higher}")