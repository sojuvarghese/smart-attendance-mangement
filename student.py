import pandas as pd
student_ids = list(range(1, 5001))
student_names = [f"Student_{i}" for i in student_ids]
df = pd.DataFrame({
    "studentid": student_ids,
    "studentname": student_names
})

df.to_excel("students.xlsx", index=False)
print("Excel file 'students.xlsx' created successfully with 5000 records!")
