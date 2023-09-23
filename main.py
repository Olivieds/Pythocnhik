from student import Student
from cat import Cat

metelkina = Cat("Vitamina", 4, 0)
budnychenko = Student("Denys", 15.7, "S2816", 120.0)
solop = Student("Illya", 16.1, "S2816", 90.0)
oliynyk = Student("Kostya", 14.2, "S2816", 1200.0)
students = []
cats = []
students.append(budnychenko)
students.append(solop)
students.append(oliynyk)
for student in students:
    student.String()
iphone15price = 1000
job = 100
budnychenko.Buy(iphone15price)
solop.Buy(iphone15price)
oliynyk.Buy(iphone15price)
budnychenko.Earn(job)
solop.Earn(job)
oliynyk.Earn(job)
for student in students:
    student.String()

