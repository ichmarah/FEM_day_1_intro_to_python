def provideNumber():
    return input('Choose a a number: ')

# If the input is not a number, the error is caught and a message is printed for the user.


def isNumber():
    try:
        int(provideNumber())
    except ValueError:
        print(f'This is not a number.')


isNumber()

