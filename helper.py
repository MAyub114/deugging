def func(num):
    ic(num)
    return 2*num

def foo(a, b):
    ic()
    print(f"Compares {a} and {b}")

    if a > b:
        ic()
        print(f"{a} is greater than {b}")
    else:
        ic()
        print(f"{a} is less than or equal to {b}")