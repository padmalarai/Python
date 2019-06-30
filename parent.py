class parent:
    def __init__(self):
        print("constructor from parent")
        
    def test_func(self):
        print("test func from parent")

    def test1_func(self):
        print("test1 func from parent")

class child(parent):
    def __init__(self):
        super().__init__()
        print("constructosr from child")
        
    def test2_func(self):
        print("test func from child")

    def test1_func(self):
        super().test1_func()
        print("test1 func from child")

obj=child()
obj.test2_func()
obj.test1_func()
obj.test_func()
        

   
