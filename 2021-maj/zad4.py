file = open("instrukcje.txt", "r")
data = file.read()
lines = data.splitlines()


def dopisz(current: str, letter: str) -> str:
    return current + letter


def zmien(current: str, letter: str) -> str:
    return current[:-1] + letter


def usun(current: str) -> str:
    return current[:-1]


def przesun(current: str, letter: str) -> str:
    arr = list(current)
    for i in range(0, len(arr)):
        if arr[i] == letter:
            if arr[i] == 'Z':
                arr[i] = 'A'
            else:
                arr[i] = chr(ord(arr[i])+1)
            return "".join(arr)
    return current


def execute(lines: list[str]) -> str:
    cur = ""
    for line in lines:
        if line.startswith("DOPISZ"):
            cur = dopisz(cur, line.split(' ')[1])
        elif line.startswith("ZMIEN"):
            cur = zmien(cur, line.split(' ')[1])
        elif line.startswith("USUN"):
            cur = usun(cur)
        elif line.startswith("PRZESUN"):
            cur = przesun(cur, line.split(' ')[1])
        else:
            raise Exception("Command not found!")
    return cur


# zad 4.1
print("zad 4.1:", len(execute(lines)))

# zad 4.2
cur_type = lines[0].split(' ')[0]
cur_len = 1
max_type = cur_type
max_len = cur_len

for i in range(1, len(lines)):
    command = lines[i].split(' ')[0]
    if cur_type == command:
        cur_len += 1
    else:
        cur_type = command
        cur_len = 1
    if cur_len > max_len:
        max_len = cur_len
        max_type = cur_type
print("zad 4.2: {} {}".format(max_type, max_len))

# zad 4.3
dic = dict()
for line in lines:
    if line.startswith("DOPISZ"):
        letter = line.split(' ')[1]
        if dic.get(letter):
            dic[letter] += 1
        else:
            dic[letter] = 1
max_value = max(dic.values())
max_key = None
for key in dic.keys():
    if dic[key] == max_value:
        max_key = key
        break
print("zad 4.3: {} {}".format(max_key, max_value))

# zad 4.4
print("zad 4.4: {}".format(execute(lines)))
