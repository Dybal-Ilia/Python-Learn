class Integer:
    @classmethod
    def validate_coord(cls, coord):
        if not isinstance(coord, int):
            raise TypeError("Coordinates should be int")

    def __set_name__(self, owner, name):

        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        self.validate_coord(value)
        print(f"__set__: {self.name} = {value}")
        setattr(instance, self.name, value)

class Point3D:

    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x 
        self.y = y
        self.z = z

    
        
    

        
point = Point3D(1, 2, 3)
print(point.__dict__)