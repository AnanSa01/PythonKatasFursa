def do_n_times(func, n):
    """
    Executes the given function n times.

    Args:
        func: the function to execute
        n: the number of times to execute the function
    """
    result = ""
    for _ in range(n):
        result += f"{func()}\n"
    return result


def say_hello():
    """A function that prints 'Hello!'."""
    return "Hello!"


def print_message():
    """A function that prints 'Python is fun!'."""
    return "Python is fun!"


if __name__ == '__main__':
    print("Calling function 3 times:")
    print(do_n_times(say_hello, 3))

    print("Calling another function 5 times:")
    do_n_times(print_message, 5)

    # Expected output:
    # Calling function 3 times:
    # Hello!
    # Hello!
    # Hello!
    # Calling another function 5 times:
    # Python is fun!
    # Python is fun!
    # Python is fun!
    # Python is fun!
    # Python is fun!