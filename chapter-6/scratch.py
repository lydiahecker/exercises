def a(x):
    return b(x)

def b(x):
    try:
        return c(x-1)
    except:
        raise AssertionError("Something broke.")

def c(x):
    return d(x)

def d(x):
    return 4/x

print(a(1))