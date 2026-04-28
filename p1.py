# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_exam_dataset_2000.csv")

# Show first 5 rows
print("Dataset Preview:")
print(df.head())

# Basic Info
print("\nDataset Info:")
print(df.info())

# ===============================
# 📊 1. Overall Performance
# ===============================

print("\nOverall Statistics:")
print(df.describe())

print("\nAverage Percentage:", df["Percentage"].mean())
print("Highest Percentage:", df["Percentage"].max())
print("Lowest Percentage:", df["Percentage"].min())

# ===============================
# 📚 2. Subject-wise Analysis
# ===============================

subjects = ["Math", "Science", "English"]

for subject in subjects:
    print(f"\n{subject} Average:", df[subject].mean())

# ===============================
# 🏆 3. Top 10 Students
# ===============================

top_students = df.sort_values(by="Percentage", ascending=False).head(10)
print("\nTop 10 Students:")
print(top_students)

# ===============================
# ⚠️ 4. Weak Students (Below 40%)
# ===============================

weak_students = df[df["Percentage"] < 40]
print("\nWeak Students Count:", len(weak_students))

# ===============================
# 🎯 5. Grade Distribution
# ===============================

grade_counts = df["Grade"].value_counts()
print("\nGrade Distribution:")
print(grade_counts)

# Plot Grade Distribution
plt.figure()
grade_counts.plot(kind='bar')
plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.show()
# 2️⃣ Grade Distribution Pie Chart
plt.figure()
df["Grade"].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Grade Distribution")
plt.ylabel("")
plt.show()
# ===============================
# 📈 6. Subject Comparison Chart
# ===============================

avg_marks = [df[sub].mean() for sub in subjects]

plt.figure()
plt.bar(subjects, avg_marks)
plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()

# ===============================
# 📊 7. Percentage Distribution
# ===============================

plt.figure()
plt.hist(df["Percentage"], bins=20)
plt.title("Percentage Distribution")
plt.xlabel("Percentage")
plt.ylabel("Number of Students")
plt.show()

# ===============================
# 📌 8. Pass / Fail Analysis
# ===============================

pass_count = len(df[df["Grade"] != "F"])
fail_count = len(df[df["Grade"] == "F"])

print("\nPass Students:", pass_count)
print("Fail Students:", fail_count)

plt.figure()
plt.bar(["Pass", "Fail"], [pass_count, fail_count])
plt.title("Pass vs Fail")

# Create extended dataset CSV with more subjects, attendance, and gender
import random

num_students = 2000

data = []

for i in range(1, num_students + 1):
    student_id = f"S{i:04d}"
    name = f"Student_{i}"
    gender = random.choice(["Male", "Female"])
    attendance = random.randint(50, 100)  # percentage

    math = random.randint(30, 100)
    science = random.randint(30, 100)
    english = random.randint(30, 100)
    hindi = random.randint(30, 100)
    sst = random.randint(30, 100)
    computer = random.randint(30, 100)

    total = math + science + english + hindi + sst + computer
    percentage = round(total / 600 * 100, 2)

    if percentage >= 80:
        grade = 'A'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 40:
        grade = 'C'
    else:
        grade = 'F'

    data.append([
        student_id, name, gender, attendance,
        math, science, english, hindi, sst, computer,
        total, percentage, grade
    ])

df = pd.DataFrame(data, columns=[
    "Student_ID", "Name", "Gender", "Attendance(%)",
    "Math", "Science", "English", "Hindi", "SST", "Computer",
    "Total", "Percentage", "Grade"
])

file_path = "/mnt/data/student_exam_dataset_2000_full.csv"
df.to_csv(file_path, index=False)

file_path
plt.show()