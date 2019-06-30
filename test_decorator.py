def deco_func(func_name):
    def inner():
        print("its decorator func")
        print("after decorator func")
        func_name()
    return inner

@deco_func
def test_func():
    print("its test func")

def test2_func():
    print("its test2 func")


test_func

test2_func()
