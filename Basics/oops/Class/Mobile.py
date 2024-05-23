# Create a class for mobiles evey mobile is having some features
# where totall number of camera ,processing speed ,Recording Facility.
# Creat a object of the mobile class with samsung ,oppo ,apple.Take feature for users for each obbject and display them 


class Mobile:
    def set_camera(self, no_of_camera):
        self.no_of_camera = no_of_camera
    def processing_speed(self,processing_speed):
        self.processing_speed = processing_speed
    def recording_facility(self,recording_facility):
        self.recording_facility = recording_facility
    
    def get_features(self):
        print(self.no_of_camera,self.processing_speed,self.recording_facility)


oppo=Mobile()
oppo.set_camera(4)
oppo.processing_speed("3.2Gbs")
oppo.recording_facility("8k 60FPS ")
oppo.get_features()

apple=Mobile()
apple.set_camera(3)
apple.processing_speed("3.0Gbs")
apple.recording_facility("4k 60FPS")
apple.get_features()

samsung=Mobile()
samsung.set_camera(5)
samsung.processing_speed("3.5Gbs")
samsung.recording_facility("8k 30FPS")
samsung.get_features()


# Create a constant inside a clas in python any constant value can be declared directly inside a class just like a normal variable.That constant values can be called directly  with the obect of the class