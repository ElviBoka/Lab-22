from models import Teacher, Student, Course

# Mësuesit
t1 = Teacher(1, "Ardit Kola", "ardit.kola@shkolla.al")
t2 = Teacher(2, "Elona Hoxha", "elona.hoxha@shkolla.al")

# Kurset
c1 = Course("PY101", "Python Bazë", 2, t1)
c2 = Course("DB102", "Baza të të Dhënave", 3, t1)
c3 = Course("WD103", "Web Design", 2, t2)

# Studentët
s1 = Student(10, "Elira Deda", 12)
s2 = Student(11, "Klodian Meta", 11)
s3 = Student(12, "Ardi Lila", 12)
s4 = Student(13, "Sara Gega", 11)
s5 = Student(14, "Brikena Gjoni", 10)
s6 = Student(15, "Noel Hoxha", 10)

# Regjistrime
c1.add_student(s1)
c1.add_student(s2)
try:
    c1.add_student(s3)  # tejkalim kapaciteti
except ValueError as e:
    print("Gabim:", e)

c2.add_student(s3)
c2.add_student(s4)
c3.add_student(s5)

# R1: Raporti i kurseve
print("\nKURSET:")
for course in [c1, c2, c3]:
    emrat = ", ".join([s.full_name for s in course.students])
    print(f'- {course.code} "{course.title}" — {len(course.students)}/{course.capacity} studentë: {emrat}')

# R2: Raporti i mësuesve
print("\nMËSUESIT:")
for teacher in [t1, t2]:
    kurselist = ", ".join([c.code for c in teacher.courses])
    print(f'- {teacher.full_name}: {kurselist}')

# R3: Kursi me më shumë dhe më pak regjistrime
all_courses = [c1, c2, c3]
max_course = max(all_courses, key=lambda c: len(c.students))
min_course = min(all_courses, key=lambda c: len(c.students))
print("\nMAKS/MIN:")
print(f'- Max: {max_course.code} ({len(max_course.students)})')
print(f'- Min: {min_course.code} ({len(min_course.students)})')
