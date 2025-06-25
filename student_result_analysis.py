import pandas as pd

# Ask how many students to enter
n = int(input("Enter number of students: "))
students = []

for i in range(n):
    print(f"\nEnter details for student {i+1}:")
    roll = input("Roll No: ")
    name = input("Name: ")
    math = int(input("Marks in Math: "))
    physics = int(input("Marks in Physics: "))
    chemistry = int(input("Marks in Chemistry: "))
    students.append({
        "Roll No": roll,
        "Name": name,
        "Math": math,
        "Physics": physics,
        "Chemistry": chemistry
    })

# Convert to DataFrame
df = pd.DataFrame(students)

# Calculate total, average, and grade
df["Total"] = df[["Math", "Physics", "Chemistry"]].sum(axis=1)
df["Average"] = df["Total"] / 3

def assign_grade(avg):
    if avg >= 85:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'Fail'

df["Grade"] = df["Average"].apply(assign_grade)

# Save to Excel
df.to_excel("Student_Result_Analysis2.xlsx", index=False)
print("\nStudent results saved to 'Student_Result_Analysis2.xlsx'")

