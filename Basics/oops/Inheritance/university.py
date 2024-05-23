#create a class UNIVERSITY that is having a function indicating the nae of uiversity 
#The university class is inherted by the admission cell that collects students name and reg no.
#The data collected by admission cell is further inherited by the exam section 
#Exam section generates the debbared list

class university:
    def name(self,name):
        self.name = name

class admission_cell(university):
    def collect_data(self,data):
        self.data = data

class exam_section(admission_cell):
    def get_debar_list(self):
        print("23mca839")


obj=exam_section()
obj.collect_data({
    "name":"sujal",
    "regno":"23mca10069"
})
obj.get_debar_list()




