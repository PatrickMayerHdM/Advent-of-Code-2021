import pathlib
text = pathlib.Path('Day 1\input_test.txt').read_text().split('\n')
numbers = [int(line) for line in text]

i = 0
o = 1
higher = 0

while i < len(numbers):
  if numbers[o] > numbers[i]:
    print(True)
    i = i + 1
    o = o + 1

  else:
    print(False)
    i = i + 1
    o = o + 1



