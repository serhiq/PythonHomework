"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

# наследовать надо от `Exception`
# цитата из https://docs.python.org/3/library/exceptions.html: 
#  programmers are encouraged to derive new exceptions from the Exception class or one of its subclasses, and not from BaseException
# и https://docs.python.org/3/tutorial/errors.html#tut-userexceptions:
#  Exceptions should typically be derived from the Exception class, either directly or indirectly.
class LowFuelError(BaseException):
    pass


class NotEnoughFuel(BaseException):
    pass


class CargoOverload(BaseException):
    pass
