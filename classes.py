import pandas as pd
class_ids = list(range(1, 6))
class_names = [f"class_{i}" for i in class_ids]
df = pd.DataFrame({
    "class_id": class_ids,
    "class_name": class_names
})

df.to_excel("classes.xlsx", index=False)
print("created !")
