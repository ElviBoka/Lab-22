# Email pa @
try:
    Teacher(3, "Gabim", "gabimemail.com")
except ValueError as e:
    print("Gabim email:", e)

# Kapacitet 0
try:
    Course("ERR101", "Gabim Kurs", 0, t1)
except ValueError as e:
    print("Gabim kapacitet:", e)

# Student dy herë
try:
    c2.add_student(s3)
except ValueError as e:
    print("Gabim dyfishim:", e)
