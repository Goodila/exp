class Defender: 
    def __init__(self, v) -> None:
        self.__v = v

    
    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp
    
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp

        return True
    


v1 = [1, 2, 3]
v2 = [2, 3, 1]

with Defender(v1) as dv:
    for i, a in enumerate(dv):
        dv[i] += v2[i]

print(v1)