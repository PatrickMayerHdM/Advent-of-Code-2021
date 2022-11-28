from typing import Iterator, Tuple

movement = Tuple[str, int]

def movement () -> Iterator[movement]:
    with open("Day 2\input.txt") as f:
        for line in f:
            amd, arg = line.split()
            amount = int(arg)
            yield amd, amount
test = movement()
print(test)