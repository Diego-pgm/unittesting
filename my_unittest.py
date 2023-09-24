from rectangle import Rectangle

def assert_equal(*args):
    try:
        assert expresion == response
        print("Test passed")
    except Exception:
        print("Test failed.")

rectangle = Rectangle(3,3)
expresion = rectangle.get_area()
response = 10
assert_equal(expresion, response)
