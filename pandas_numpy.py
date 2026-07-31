import pandas as pd

df1 = pd.DataFrame({
    'employee': ['Julia', 'Marie', 'Adam', 'Nicole'],
    'department': ['Data Science', 'Web Development', 'Data Science', 'Cyber Security'],
    'Year': ['2005', '2008', '2011', '2002']
})
df2 = pd.DataFrame({
    'employee': ['Nicole', 'Adam', 'Julia', 'Marie'],
    'country': ['Canada', 'England', 'USA', 'Germany'],
    'salary': [22000, 16000, 20000, 17500]
})

result = pd.merge(df1, df2,)

print("=" * 60)
print("Inner Merge default")
print("- Combines DataFrames using the common column.")
print("- Returns only matching records from both DataFrames.")
print("=" * 60)
print(result)


left = pd.merge(df1, df2, on="employee", how="left")
print("=" * 60)
print("Left Merge")
print("- Keeps all rows from the left DataFrame (df1).")
print("- Matching values are taken from the right DataFrame (df2).")
print("=" * 60)
print(left)

right = pd.merge(df1, df2, on="employee", how="right")

print("=" * 60)
print("Right Merge")
print("- Keeps all rows from the right DataFrame (df2).")
print("- Matching values are taken from the left DataFrame (df1).")
print("=" * 60)

print(right)

outer = pd.merge(df1, df2, on="employee", how="outer")

print("=" * 60)
print("Outer Merge")
print("- Keeps all rows from both DataFrames.")
print("- Missing matches are filled with NaN.")
print("=" * 60)

print(outer)