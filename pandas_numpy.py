import pandas as pd

df1 = pd.DataFrame({
    "employee": ["Julia", "Marie", "Adam", "Nicole"],
    "department": ["Data Science", "Web Development", "Data Science", "Cyber Security"]
})

df2 = pd.DataFrame({
    "employee": ["Julia", "Adam", "David", "Marie"],
    "country": ["USA", "England", "Canada", "Germany"]
})
inner = pd.merge(df1, df2, on="employee", how="inner")

print("=" * 60)
print("Inner Merge")
print("- Returns only matching records from both DataFrames.")
print("=" * 60)

print(inner)
left = pd.merge(df1, df2, on="employee", how="left")

print("=" * 60)
print("Left Merge")
print("- Keeps all rows from the left DataFrame.")
print("=" * 60)

print(left)
right = pd.merge(df1, df2, on="employee", how="right")

print("=" * 60)
print("Right Merge")
print("- Keeps all rows from the right DataFrame.")
print("=" * 60)

print(right)
outer = pd.merge(df1, df2, on="employee", how="outer")

print("=" * 60)
print("Outer Merge")
print("- Keeps all rows from both DataFrames.")
print("=" * 60)

print(outer)