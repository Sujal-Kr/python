class grandparent:
    def intro(self):
        print("i am gradparent class")
    
class parentclass(grandparent):
    def intro(self):
        print("i am parent class")

class childclass(parentclass):
    def intro(self):
        print("i am child class")

obj=childclass()
obj.intro()

