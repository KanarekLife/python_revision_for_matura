file = open("dane4.txt", "r")
data = file.read()
lines = data.splitlines()
nums = []
for line in lines:
    nums.append(int(line))

# zad 4.1
min_luka = -1
max_luka = -1

for i in range(1, len(nums)):
    luka = abs(nums[i] - nums[i-1])
    if min_luka > luka or min_luka < 0:
        min_luka = luka
    if max_luka < luka or max_luka < 0:
        max_luka = luka

print("zad 4.1")
print("max luka: {}".format(max_luka))
print("min luka: {}".format(min_luka))

# zad 4.2


def is_regular(input: list[int]) -> bool:
    luka = abs(input[1] - input[0])
    if len(input) > 2:
        for i in range(2, len(input)):
            if abs(input[i] - input[i-1]) != luka:
                return False
    return True


def get_longest_regular(nums: list[int]) -> tuple[int, int, int]:
    max_len = -1
    start_value = -1
    end_value = -1
    for i in range(0, len(nums)):
        for j in range(i+2, len(nums)):
            input = []
            for c in range(i, j):
                input.append(nums[c])
            if is_regular(input) and len(input) > max_len:
                max_len = len(input)
                start_value = input[0]
                end_value = input[len(input) - 1]
    return (max_len, start_value, end_value)


print("zad 4.2")
print(get_longest_regular(nums))

# zad 4.3


def find_most_frequent(nums: list[int]) ->


dic = dict()
 for i in range(1, len(nums)):
      luka = abs(nums[i] - nums[i-1])
       if dic.get(luka):
            dic[luka] += 1
        else:
            dic[luka] = 1
