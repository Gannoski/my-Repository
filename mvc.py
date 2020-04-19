class MySingleton(object):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MySingleton, cls).__new__(cls)
            cls.y = 10
        return cls._instance


x = MySingleton()
print(x.y)
x.y = 20
z = MySingleton()
print(z.y)
    



