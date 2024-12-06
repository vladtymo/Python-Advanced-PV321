# ------------ generators
# ---- yield vs return


def testGenerator():
    print("--- first ---")
    yield 1
    print("--- second ---")
    yield 2
    print("--- third ---")
    yield 3


# print(testGenerator())

for i in testGenerator():
    print(i)


# fibonacci: 1 1 2 3 5 8 13 ...
def fibonacci_numbers():
    x, y = 1, 1
    while True:
        yield x
        sum = x + y
        x = y
        y = sum


for i in fibonacci_numbers():
    print(i)
    input()

# ------ generator expression
# syntax: [expression for var in collection (condition))]


def powOfTwo():
    for x in range(10):
        yield pow(2, x)


result = [pow(2, x) for x in range(10)]

for x in result:
    print(x)
