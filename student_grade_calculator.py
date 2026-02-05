name = input("Enter student name: ")
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
total = m1 + m2 + m3
percentage = total / 3
print("\nStudent:", name)
print("Total marks:", total)
print("Percentage:", percentage)
if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
