file = open("pary.txt", "r")
data = file.read()
lines = data.splitlines()


def get_primes() -> list[int]:
    primes = []
    for i in range(2, 101):
        is_prime = True
        for j in range(2, i):
            if i == j:
                continue
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


primes = get_primes()

# zad 4.1


def get_goldbach_nums(n: int) -> (int, int):
    max_diff = -1
    max_1 = -1
    max_2 = -1
    for i in range(0, len(primes)):
        for j in range(0, len(primes)):
            a = primes[i]
            b = primes[j]
            if a + b == n:
                if abs(b - a) > max_diff:
                    max_1 = a
                    max_2 = b
                    max_diff = abs(b - a)
    return (max_1, max_2)


print("zad 4.1:")
for line in lines:
    n = int(line.split(' ')[0])
    if n % 2 == 0:
        a, b = get_goldbach_nums(n)
        print("{} {} {}".format(n, a, b))

# zad 4.2


def find_longest(word: str) -> tuple[str, int]:
    cur_len = 1
    cur_letter = word[0]
    max_len = cur_len
    max_letter = cur_letter
    for i in range(1, len(word)):
        if cur_letter == word[i]:
            cur_len += 1
        else:
            cur_letter = word[i]
            cur_len = 1
        if cur_len > max_len:
            max_len = cur_len
            max_letter = cur_letter
    return (max_letter*max_len, max_len)


print("\nzad 4.2:")
for line in lines:
    word = line.split(' ')[1]
    res = find_longest(word)
    print("{} {}".format(res[0], res[1]))

# zad 4.3


def find_smallest(a: tuple[int, str], b: tuple[int, str]) -> tuple[int, str]:
    if a[0] < b[0]:
        return a
    elif a[0] > b[0]:
        return b
    else:
        for i in range(len(a[1])):
            if a[1][i] < b[1][i]:
                return a
            elif a[1][i] > b[1][i]:
                return b


to_check = []
for line in lines:
    c = line.split(' ')
    if int(c[0]) == len(c[1]):
        to_check.append((int(c[0]), c[1]))
smallest = to_check[0]
for i in range(1, len(to_check)):
    smallest = find_smallest(smallest, to_check[i])
print("\nzad 4.3:")
print("{} {}".format(smallest[0], smallest[1]))
