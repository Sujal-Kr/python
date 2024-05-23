# create a class university that displays the name of name university.
# there is a class research body that provides the research funding sechems for the students. 
# to complete the pg courses a student has to join any university plus any university funding body



class university:
    def display_name(self,name):
        print(name)

    
class research_body:
    def get_funding():
        return True
    
class student(university,research_body):
    def complete_pg_course(self,name):
        self.display_name(name)
        self.get_funding()
        print("course completed")


sujal = student()
sujal.complete_pg_course("VIT")


# for a university  there are there are basic pillars 
# 1.fee collection section
# 2.examination center
# 3.placement tester
# all these 3 pillars must follow a same university norms but provide  seprate functionality


