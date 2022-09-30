
def power_numbers(*numbers):
    return list(map(square, numbers))


def square(number):
    if not isinstance(number, int):
        raise TypeError("Expected int, got %s" % (type(number),))
    return number ** 2


# =================================================================== #

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers, filter_type):
    if filter_type == ODD:
        return list(filter(is_odd, numbers))
    elif filter_type == EVEN:
        return list(filter(is_even, numbers))
    elif filter_type == PRIME:
        return list(filter(is_prime, numbers))
    else:
        raise Exception("Unknown type filter " + filter_type)


def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return num % 2 != 0


def is_prime(num):
    if not isinstance(num, int):
        raise TypeError("Expected int, got %s" % (type(num)))

    if (num <= 1):
        return False

    if (num % 2 == 0):
        return num == 2

    for i in range(2, int(num / 2)):
        if num % i == 0:
            return False
    return True


