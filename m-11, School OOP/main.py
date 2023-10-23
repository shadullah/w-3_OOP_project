from School import School,ClassRoom,Subject
from Person import Student,Teacher

def main():
    school = School('adam jee', 'moha mamd')

    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    Ten = ClassRoom('Ten')
    school.add_classroom(Ten)

    abul = Student('abir khan', eight)
    school.student_admission(abul)
    babul = Student('babul khan', eight)
    school.student_admission(babul)
    cabul = Student('sabul khan', eight)
    school.student_admission(cabul)

    physics_teachers = Teacher('shahjahan tapan rana')
    physics=Subject('physics', physics_teachers)
    eight.add_subject(physics)

    chemistry_teachers = Teacher('hajari nag')
    chemistry=Subject('chemistry', chemistry_teachers)
    eight.add_subject(chemistry)

    biology_teachers = Teacher('Azmol alahi')
    biology=Subject('biology', biology_teachers)
    eight.add_subject(biology)

    eight.take_semester_final()


    print(school)

if __name__ == '__main__':
    main()