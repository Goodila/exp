def decorator(func):
    def wrap(*args, **kwargs):
        print("do first thing")
        res = func(*args, **kwargs)
        print("do second thing")
        return res 

    return wrap

@decorator
def some_func():
    print("i do myself like simple func")


some_func()
