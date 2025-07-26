class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwds):
        if not isinstance(args[0], str):
            raise TypeError("Argument should be string")
        return args[0].strip(self.__chars)

    
s1 = StripChars(' !?:.,-|')
res = s1(" Hello, World! ")
print(res) 