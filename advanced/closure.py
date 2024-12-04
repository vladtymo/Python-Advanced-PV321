import math
# -------- scope --------
# login?

globalVariable = 123

def myFunc():
    login = "blabla123"
    globalVariable

# login?

# -------- closure --------

def outer():

    # data
    number = 1

    def inner():
        nonlocal number # get from outer scope
        print(number)
        number *= 2

    return inner

# print(number) - error

func = outer()

func()
func()
func()
func()
func()
func()
func()

# --------- syntax sugar ---------
print("Blala: " + str(2 * 2) + "!")
print(f"Blala: {2 * 2}!")