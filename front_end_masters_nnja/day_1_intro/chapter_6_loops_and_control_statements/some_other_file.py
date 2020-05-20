import main_method

# Now that we have imported the module and run code, first the main_method function is executed followed by the function requested in this file. We do not want the function from the main method to run as well. To avoid this, we have to put __name__  in a conditional in main_method.py.

main_method.get_handle()

# After the conditional is added in main_method.py, only the code in this current file is executed.
