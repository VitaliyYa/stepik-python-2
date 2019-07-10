try:
    foo()
except ZeroDivisionError as e:
    print("ZeroDivisionError")
except AssertionError as e:
    print("AssertionError")
except ArithmeticError as e:
    print("ArithmeticError")
