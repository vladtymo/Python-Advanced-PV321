def cube(x): return x * x * x
def increment(x): return x + 1

def changeArray(arr, modify):
    for i in range(len(arr)):
        arr[i] = modify(arr[i])

numbers = [3, 2, -10, 0, 99, 120, 34, 6]

print(f"Original: {numbers}")

changeArray(numbers, cube) 
changeArray(numbers, increment) 

changeArray(numbers, lambda x: x - 1) 
changeArray(numbers, lambda x: x * 2) 

print(f"Changed: {numbers}")