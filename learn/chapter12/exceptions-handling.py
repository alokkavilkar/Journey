a = input("Enter number:")

try:
    # risky code that might leads to generate error.
    a = int(a)
except Exception as e: 
    # handle error that generate error
    print('Please enter a valid number only', e)
else:
    # if exception not occur enter here.
    if a > 10:
      print('Entered number is greater than 10')
finally:
    print("Enter here does'nt matter exception occur or not.")

# Error and exception is like error occurs and crash program and exception does'nt crash it.
# Common Exception Types
# ArithmeticError: Base class for arithmetic errors.
# ZeroDivisionError: Raised when dividing by zero.
# OverflowError: Raised when a calculation exceeds maximum limit for a numeric type.
# FloatingPointError: Raised when a floating point operation fails.
# AssertionError: Raised when an assert statement fails.
# AttributeError: Raised when an attribute reference or assignment fails.
# EOFError: Raised when the input() function hits an end-of-file condition (EOF).
# ImportError: Raised when an import statement fails.
# ModuleNotFoundError: A subclass of ImportError that is raised when a module cannot be found.
# IndexError: Raised when a sequence subscript is out of range.
# KeyError: Raised when a dictionary key is not found.
# KeyboardInterrupt: Raised when the user hits the interrupt key (Ctrl+C or Delete).
# MemoryError: Raised when an operation runs out of memory.
# NameError: Raised when a local or global name is not found.
# UnboundLocalError: A subclass of NameError for referencing a local variable before it is assigned.
# OSError: Raised for system-related errors.
# FileNotFoundError: Raised when a file or directory is requested but doesn't exist.
# PermissionError: Raised when trying to run an operation without the adequate access rights.
# TimeoutError: Raised when a system function timed out at the system level.
# RuntimeError: Raised when an error doesn't fall under any other category.
# RecursionError: Raised when the maximum recursion depth is exceeded.
# SyntaxError: Raised when the parser encounters a syntax error.
# IndentationError: Raised when there's incorrect indentation.
# TabError: Raised when there's a mix of tabs and spaces in the indentation.
# TypeError: Raised when an operation or function is applied to an object of inappropriate type.
# ValueError: Raised when a function receives an argument of the correct type but inappropriate value.
# StopIteration: Raised by the next() function to indicate that there are no further items produced by the iterator.
# StopAsyncIteration: Raised by an asynchronous iterator’s __anext__() method to stop the iteration.
