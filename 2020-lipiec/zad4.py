import math
from os import remove
file = open("identyfikator.txt", "r")
data = file.read()
lines = data.splitlines()

# zad 4.1
r = []
max_sum = 0
for line in lines:
    cur_sum = 0
    for i in range(3, len(line)):
        cur_sum += int(line[i])
    if cur_sum > max_sum:
        r = [line]
        max_sum = cur_sum
    elif cur_sum == max_sum:
        r.append(line)
print("zad 4.1:")
for l in r:
    print(l)

# zad 4.2


def is_palindrom(word: str) -> str:
    for i in range(0, math.ceil(len(word) / 2)):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True


r = []
for line in lines:
    id = ""
    num = ""
    for i in range(0, 3):
        id += line[i]
    for i in range(3, len(line)):
        num += line[i]
    if is_palindrom(id) or is_palindrom(num):
        r.append(line)
print("\nzad 4.2:")
for l in r:
    print(l)

# zad 4.3


def get_letter_value(letter: str) -> int:
    return ord(letter) - 55


def remove_letters(word: str) -> list[int]:
    r = []
    for i in range(0, 3):
        r.append(get_letter_value(word[i]))
    # We remove one control number
    for i in range(4, len(word)):
        r.append(int(word[i]))
    return r


def apply_wages(word: str) -> list[int]:
    r = []
    list = remove_letters(word)
    r.append(list[0] * 7)
    r.append(list[1] * 3)
    r.append(list[2] * 1)
    r.append(list[3] * 7)
    r.append(list[4] * 3)
    r.append(list[5] * 1)
    r.append(list[6] * 7)
    r.append(list[7] * 3)
    return r


def check(word: str) -> bool:
    control = sum(apply_wages(word)) % 10
    return control == int(word[3])


print("\nzad 4.3:")
for line in lines:
    if not check(line):
        print(line)
