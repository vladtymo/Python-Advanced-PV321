def withTitle(input_func):
    def output_func(*args):
        # extra logic
        count = len(args[0])
        print("-" * count)
        input_func(*args)
        print("-" * count)
        # extra logic

    return output_func

@withTitle
def showMessage(text):
    print(text)

showMessage("Hello decorator!")
showMessage("Hi decorator!")
showMessage("Bye decorator!")
