

class ValueException(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueException('too high',x)
    elif x<0:
        raise ValueException('too low',x)

try:
    test_value(1000)
    test_value(-10)
except ValueException as v:
    print('value exception thrown',v.message)
finally:
    print('done')