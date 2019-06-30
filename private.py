class test:
    __var="test variable"
    def __function1(self):
        print("Functional from test class")
        print(test.__var)

obj=test()
obj._test__function1()
print(obj._test__var)
