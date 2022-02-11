def exception_check(a, b):
    try:
        num_out = a / b
    except ZeroDivisionError:
        print("The Error!")
    else:
        print(num_out)