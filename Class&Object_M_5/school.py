class student:
    def __init__(self,name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id



    def __repr__(self):
        return f'student with name: {self.name}, class : {self.current_class}, id: {self.id}'
    

class teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id


    def __repr__(self):
        return f'Teacher: {self.name}, subject: {self.subject}'
    


class School:
    def __init__(self,name):
        self.name = name
        self.teacher = []
        self.student = []


    def add_teacher(self,name,subject):
        id = len(self.teacher) + 101
        teachers = teacher(name, subject, id)
        self.teacher.append(teachers)


    def Eneoll(self,name,fee):
        if fee < 6500:
            return 'Not enough fee'
        else:
            id = len(self.student) + 1
            students = student(name, 'C' ,id)
            self.student.append(students)
            return f'{name} is Enroll with id {id}, Extra money {fee - 6500}'
        

    def __repr__(self):
        print('Wellcome to ', self.name)
        print('------------- YOUR TEACHER ------------')
        for teachers in self.teacher:
            print(teachers)

        print('------------- UOR STUDENT -------------')
        for Student in self.student:
            print(Student)
        return 'All Done for now'
    


phitron = School('phitron')



phitron.Eneoll('Rakib',5400)
phitron.Eneoll('Shahin',6400)
phitron.Eneoll('Syme',9000)
phitron.Eneoll('Emon',7000)
phitron.Eneoll('Talha',4400)


phitron.add_teacher('Jonkar','Python')
phitron.add_teacher('Rahat','C++')
phitron.add_teacher('Foysal','web deboloment')


print(phitron)

