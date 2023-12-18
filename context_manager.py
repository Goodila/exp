class Manager:
    def __init__(self, obj):
        self.__obj = obj


    def __enter__(self):
        self.__temp = self.__obj[:]
        return self.__temp


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__temp.append('no_exp')
            self.__obj[:] = self.__temp
        return True
    
lst = [1]
with Manager(lst) as s:
    # raise TypeError
    s.append('some')
    print(s)
print(s, "   real s")




