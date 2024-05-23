# every university is having three basic pillars fees collection ,examination,placement a student has to clear all the requriment of these three basic pilars. 
# there are some research body that provide a special scheme for student  as well as the research paper publishing platform  a student can get a professional job only after clearing all the criteria of a university and publishing a research paper





class UniversitySection:
    def __init__(self, name):
        self.name = name

    def university_norms(self):
        print(f"{self.name} follows the university norms.")

class FeeCollectionSection(UniversitySection):
    def __init__(self):
        super().__init__("Fee Collection Section")
    
    def collect_fees(self, student_id, amount):
        print(f"Collecting fees of {amount} from student {student_id}.")

class ExaminationCenter(UniversitySection):
    def __init__(self):
        super().__init__("Examination Center")
    
    def conduct_exam(self, course_code):
        print(f"Conducting exam for course {course_code}.")

class PlacementTester(UniversitySection):
    def __init__(self):
        super().__init__("Placement Tester")
    
    def conduct_test(self, company_name):
        print(f"Conducting placement test for {company_name}.")

class ResearchBody:
    def __init__(self):
        self.name = "Research Body"
    
    def special_scheme(self, student_id):
        print(f"Providing special scheme to student {student_id}.")

    def publish_research_paper(self, student_id, paper_title):
        print(f"Student {student_id} published a research paper titled '{paper_title}'.")

class Student(FeeCollectionSection, ExaminationCenter, PlacementTester, ResearchBody):
    def __init__(self, student_id):
        FeeCollectionSection.__init__(self)
        ExaminationCenter.__init__(self)
        PlacementTester.__init__(self)
        ResearchBody.__init__(self)
        self.student_id = student_id

    def meet_all_requirements(self):
        self.university_norms()
        self.collect_fees(self.student_id, 1500)
        self.conduct_exam("CS101")
        self.conduct_test("Google")
        self.special_scheme(self.student_id)
        self.publish_research_paper(self.student_id, "AI in Education")
        print(f"Student {self.student_id} has met all requirements and is eligible for a professional job.")

# Example usage
def main():
    student = Student("S123")
    student.meet_all_requirements()

if __name__ == "__main__":
    main()
