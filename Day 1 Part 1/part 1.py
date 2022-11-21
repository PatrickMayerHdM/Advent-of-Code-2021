import pathlib
text = pathlib.Path('Day 1 Part 1\input_test.txt').read_text().split('\n')
numbers = [int(line) for line in text]

i = 0
o = 1
higher = 0

while o < len(numbers):
  if numbers[o] > numbers[i]:
    higher = higher + 1
    i = i + 1
    o = o + 1

  else:
    i = i + 1
    o = o + 1

print(f"Higher ist jetzt; {higher}")