class parentclass:
    def intro(self):
        print("i am parent class")
    
class childclass(parentclass):
    def intro(self):
        print("i am child class")
    
obj=childclass()
obj.intro()
