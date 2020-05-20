# __main__ --> is point of execution when having multiple modules. Module with __main__ executes first
# Is used when you want to use code from one module into another file without having to type the same code again. You import the module with the main code into another file.


def get_handle():
    handle = input('Type your Twitter handle: ')
    length = len(handle)
    print(f'Your Twitter handle is {handle} and is {length} characters long')


if __name__ == '__main__':
    get_handle()

# We import this module in some_other_file.py.
