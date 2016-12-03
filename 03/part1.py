count = 0

def is_triangle(numbers):
    for j in range(3):
        l = list(numbers)
        this = l.pop(j)
        if this >= sum(l):
            return False
    return True

for i in input_lines():
    numbers = list(map(int, i.split()))
    count += is_triangle(numbers)

print(count)
