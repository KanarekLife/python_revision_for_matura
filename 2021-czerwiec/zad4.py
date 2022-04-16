import math
file = open("napisy.txt", "r")
data = file.read()
lines = data.splitlines()

# zad 4.1
r = 0
for c in data:
    if c.isdigit():
        r += 1
print("zad 4.1: ", r)

# zad 4.2
r = ""
for i in range(1, len(lines)+1):
    if i % 20 == 0:
        line = lines[i - 1]
        pos = i // 20
        r += line[pos-1]
print("zad 4.2: ", r)

# zad 4.3


def is_palindrom(word: str) -> bool:
    for i in range(0, math.ceil(len(word) / 2)):
        if word[i] != word[len(word) - 1 - i]:
            return False
    return True


r = ""
for line in lines:
    if is_palindrom(line[49] + line):
        word = line[len(line)-1] + line
        r += word[len(word) // 2]
    elif is_palindrom(line + line[0]):
        word = line + line[0]
        r += word[len(word) // 2]
print("zad 4.3: ", r)

# zad 4.4
r = ""
halt = False
for line in lines:
    nums = []
    for c in line:
        if c.isdigit():
            nums.append(int(c))
    if len(nums) % 2 == 1:
        nums = nums[:-1]
    for i in range(0, len(nums), 2):
        num = nums[i]*10 + nums[i+1]
        if num >= 65 and num <= 90:
            r += chr(num)
            if r.endswith("XXX"):
                halt = True
                break
    if halt:
        break
print("zad 4.4: ", r)
