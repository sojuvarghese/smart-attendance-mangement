import pandas as pd
fac_ids = list(range(1, 201))
fac_names = [f"Faculty_{i}" for i in fac_ids]
df = pd.DataFrame({
    "faculty_id": fac_ids,
    "faculty_name": fac_names
})

df.to_excel("faculty.xlsx", index=False)
print("200 records crreated !")
