from rectangle import Rectangle

def assert_equal(*args):
    try:
        assert expresion == response
        print('Test passed!')
    except AssertionError:
        print('Test Failed :(')
        exit(1)

rectangle = Rectangle(3,3)
expresion = rectangle.get_area()
response = 9
assert_equal(expresion, response)
