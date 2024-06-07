class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y=y

    def __str__(self):
        return f"{self.x},{self.y}"
    
    def __add__(self,other):
        
        return Vector(self.x+other.x,self.y+other.y)
    
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.x)
    


V1=Vector(3,4)
V2=Vector(2,6)

print(V1+V2)
print(V1-V2)
        