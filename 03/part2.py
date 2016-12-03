count = 0

def is_triangle(numbers):
    for j in range(3):
        l = list(numbers)
        this = l.pop(j)
        if this >= sum(l):
            return False
    return True

def gen():
    for i in input_lines():
        yield list(map(int, i.split()))

horizontal = zip(*gen())
chained = list(chain.from_iterable(horizontal))
for i in range(0, len(chained), 3):
    numbers = chained[i:i + 3]
    count += is_triangle(numbers)

print(count)
