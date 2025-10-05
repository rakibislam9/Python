class GPA:
    def __init__(self, mark):
        self.mark = mark
       
        

    def getMark(self):
        return  self.mark
    

    def  number(self,point):
        if point > 0:
            self.mark += point


    def result(self,point):
        if 33 <= point <= 45 :
            return  "C"
        elif  46 <= point <= 55:
            return "B"
        elif  56 <= point <= 65:
            return 'A-'
        elif 66 <= point <= 79:
            return"A"
        elif 80 <= point <= 100:
            return "A+"
        elif point < 33:
            return 'F'
        else:
            return  "Invalid Maeks"


Students = {
    "Shifat": 32,
    "Talha": 50,
    "Emon":78,
    "Rakib":91,
    "Shahin":62,
}

print("=====  Result Sheet =====")
print("Name\tMarks\tGrade")
print("-------------------------")

for name, mark in Students.items():
    TotalMark = GPA(mark)
    grade = TotalMark.result(mark)
    print(f'{name}\t{mark}\t{grade}')

