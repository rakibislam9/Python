from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom


school = School("ABC", "Dinajpur")

Eight = ClassRoom("Eight")
Nine = ClassRoom("Nine")
Tan = ClassRoom("Ten")
Ellivan = ClassRoom("Ellivan")

school.add_classroom(Eight)
school.add_classroom(Nine)
school.add_classroom(Tan)
school.add_classroom(Ellivan)



Rakib = Student("Rakib",Eight)
Shahin = Student("ShHIN",Nine)
Emon = Student("Emon",Tan)
Talha = Student("Talha",Ellivan)
Sifad = Student("Sifad",Nine)


school.student_addmission(Rakib)
school.student_addmission(Shahin)
school.student_addmission(Emon)
school.student_addmission(Talha)
school.student_addmission(Sifad)


Abul = Teacher("Abul sir")
Babul = Teacher("Babul sir")
Kodus = Teacher("Kodus sir")


bangla = Subject("Bangls",Abul)
physics = Subject("physics",Babul)
chemistry = Subject("chemistry",Kodus)
boilogy = Subject("boilogy",Babul)


Eight.add_subject(bangla)
Eight.add_subject(physics)
Eight.add_subject(chemistry)
Eight.add_subject(boilogy)
Nine.add_subject(bangla)
Nine.add_subject(physics)
Nine.add_subject(chemistry)
Nine.add_subject(boilogy)
Tan.add_subject(bangla)
Tan.add_subject(physics)
Tan.add_subject(chemistry)
Tan.add_subject(boilogy)
Ellivan.add_subject(bangla)
Ellivan.add_subject(physics)
Ellivan.add_subject(chemistry)
Ellivan.add_subject(boilogy)



Eight.take_semester_final_exam()
Nine.take_semester_final_exam()
Tan.take_semester_final_exam()

print(school)