def factorial(n):
    """
    Calculate the factorial of a number.

    Args:
    n (int): Input integer for factorial calculation.

    Returns:
    int: Factorial of the input number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def is_prime(n):
    """
    Check if a number is prime.

    Args:
    n (int): Input integer to check for primality.

    Returns:
    bool: True if the input number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_fibonacci(n):
    """
    Generate a list of Fibonacci numbers up to a given number.

    Args:
    n (int): Maximum value for generating Fibonacci sequence.

    Returns:
    list: List of Fibonacci numbers up to the input maximum value.
    """
    fibonacci_list = []
    a, b = 0, 1
    while a <= n:
        fibonacci_list.append(a)
        a, b = b, a + b
    return fibonacci_list
