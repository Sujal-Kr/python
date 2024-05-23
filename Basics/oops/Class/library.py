#create a class library having 2 diffrent sections
#mca-> in which all the book code starts with MCA101.
#only 3 books are available in mca section 
#java
#python
#c++

#physics-> where the code starts from PHY101
#only 3 books are available in section
#thermodynamis
#optics
#quantum_physics

#ask the user which section he wants to visit and display all the books available
#in that section


class Library:
    def custom_section(self):
        section=input("Section: ").lower().strip()
        match section:
            case "mca":print("Java\npython\nc++")
            case "physics":print("Thermodynamic\nQuantum\nOptics")
            case _:print("Invalid section")
            
x=Library()
x.custom_section()
