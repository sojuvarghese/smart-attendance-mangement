import pandas as pd
import random
from datetime import datetime, timedelta

# Load students
students = pd.read_excel("students.xlsx")

# Generate random leave records
leave_data = []
for sid in students['studentid']:
    num_leaves = random.randint(0, 10)  # each student takes 0–10 leaves
    for _ in range(num_leaves):
        leave_date = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365))
        leave_data.append([sid, leave_date, random.choice(["Sick", "Casual", "Academic"]), random.randint(1, 5)])

fact_leaves = pd.DataFrame(leave_data, columns=["studentid", "leave_date", "leave_type", "leave_days"])
fact_leaves.to_excel("fact_leaves.xlsx", index=False)

# Generate random dropout records
dropout_data = []
for sid in random.sample(list(students['studentid']), 200):  # assume 200 students left
    dropout_data.append([sid, random.choice([2024, 2025, 2026]), random.choice(["Financial", "Transfer", "Personal"])])

fact_dropouts = pd.DataFrame(dropout_data, columns=["studentid", "dropout_year", "reason"])
fact_dropouts.to_excel("fact_dropouts.xlsx", index=False)

print("Fact tables created: fact_leaves.xlsx and fact_dropouts.xlsx")
