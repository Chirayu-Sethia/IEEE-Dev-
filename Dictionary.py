R1 = input("Type Roll Number")
M1 = input("Type final percentage")
print(R1)
print(float(M1))

R2 = input("Type Roll Number")
M2 = input("Type final percentage")
print(R2)
print(float(M2))

R3 = input("Type Roll Number")
M3 = input("Type final percentage")
print(R3)
print(float(M3)) 

R4 = input("Type Roll Number")
M4 = input("Type final percentage")
print(R4)
print(float(M4)) 

R5 = input(" Type Roll Number")
M5 = input("Type final percentage")
print(R5)
print(float(M5)) 

info = {R1 : M1, R2 : M2, R3 : M3, R4 : M4, R5 : M5}
print(info)

sorted_students_by_rollno = sorted(info.items(), key=lambda x:x[0])
print(sorted_students_by_rollno)

sorted_students_by_percentage = sorted(info.items(), key=lambda x:x[1])
print(sorted_students_by_percentage)
