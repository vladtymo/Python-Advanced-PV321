def printList(list, title):
    print("-----------" + title + "-----------")
    for i in list:
        print(i)


# ------- list - dynamic collection
numbers = [123, -45.3, 10, 999, 4, 4.5, -2, -4, -560, 1]

print(f"Count: {len(numbers)}")

numbers.append(560)
numbers.extend([1, 7])

# numbers.pop(0) # remove first
numbers.pop()  # remove last
numbers.remove(10)

printList(numbers, "Numbers")

print(f"Count of 4: { numbers.count(4)}")

threeDigitNumbers = filter(lambda x: abs(x) >= 100 and abs(x) <= 999, numbers)

printList(threeDigitNumbers, "3-digits")

numbers.sort()
numbers.reverse()

printList(numbers, "Sorted")

# --------- list copy

# copy = numbers        # - shallow copy (copy reference)
copy = numbers.copy()  # - deep copy (copy all elements)

numbers[0] = 777

print(f"Shallow list: {copy[0]}")
