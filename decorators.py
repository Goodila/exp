def decorator(func, *args, **kwargs):
    def wrap():
        print("do first thing")
        func(*args, **kwargs)
        print("do second thing")
    return wrap

@decorator
def some_func():
    print("i do myself like simple func")


some_func()
