class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        #composition
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject]  = teacher

    def student_admission(self, student, classroom_name):
        if classroom_name in self.classrooms:
            #TODO: set student it, roll no. at the time of admission
            self.classrooms[classroom_name].add_student(student)
        else:
            print(f'no classroom as named {classroom_name}')

class ClassRoom:
    def __init__(self,name) -> None:
        self.name = name
        #composition
        self.students=[]

    def add_student(self, student):
        serial_id = f'{self.name} - {len(self.students)+1}'
        student.id = serial_id
        student.classroom = self.name
        self.students.append(student)

    def __str__(self) -> str:
        return f'{self.name}-{len(self.students)}'
    
    def get_top_students(self):
        pass
