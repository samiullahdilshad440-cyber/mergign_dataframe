# 📘 Pandas Learning Repository

A beginner-friendly repository to learn **Pandas** through practical examples, simple explanations, dry runs, and memory tricks.

This repository is part of my Python Data Analysis learning journey.

---

# 📚 Topics Covered

- ✅ DataFrame Creation
- ✅ `pd.concat()`
  - Row-wise Concatenation (`axis=0`)
  - Column-wise Concatenation (`axis=1`)
  - `ignore_index=True`
- ✅ `pd.merge()`
  - Inner Merge
  - Left Merge
  - Right Merge
  - Outer Merge
  - One-to-One Merge
  - One-to-Many Merge

---

# 📂 Project Structure

```
Pandas-Learning
│
├── pandas_numpy.py
├── README.md
```

---

# 🔹 Pandas `concat()`

`concat()` is used to **combine multiple DataFrames**.

Think of it as **stacking notebooks together**.

---

## 1️⃣ Row-wise Concatenation (`axis=0`)

```python
result = pd.concat([df1, df2])
```

### Dry Run

```
df1

Julia
Marie


df2

Adam
Nicole
```

After concatenation

```
Julia
Marie
Adam
Nicole
```

### Memory Trick

```
axis = 0
      ⬇️

Adds Rows
```

---

## 2️⃣ Reset Index

```python
result = pd.concat([df1, df2], ignore_index=True)
```

Without `ignore_index`

```
0
1
0
1
```

With `ignore_index=True`

```
0
1
2
3
```

### Memory Trick

```
ignore_index=True

↓

Reset Index Only
```

Your data remains exactly the same.

---

## 3️⃣ Column-wise Concatenation (`axis=1`)

```python
result = pd.concat([df1, df2], axis=1)
```

### Dry Run

Before

```
df1

Julia
Marie
```

```
df2

USA
Germany
```

After

```
Julia     USA
Marie     Germany
```

Rows are matched using their **index**.

### Memory Trick

```
axis = 1
      ➡️

Adds Columns
```

---

# 🔹 Pandas `merge()`

`merge()` combines DataFrames using a **common column**.

Think of it as connecting information from different Excel sheets.

---

## Basic Merge

```python
result = pd.merge(df1, df2, on="employee")
```

### Dry Run

Employee Table

```
Julia
Marie
Adam
```

Country Table

```
Julia → USA
Marie → Germany
Adam → England
```

After Merge

```
Julia  Data Science  USA
Marie  Web Dev       Germany
Adam   Data Science  England
```

### Memory Trick

```
merge()

↓

Match using a common column 🔑
```

---

# Merge Types

## ✅ Inner Merge

```python
pd.merge(df1, df2, how="inner")
```

Returns only matching records.

```
🤝

Common Data Only
```

---

## ✅ Left Merge

```python
pd.merge(df1, df2, how="left")
```

Keeps every row from the left DataFrame.

```
⬅️

Left Never Loses Data
```

---

## ✅ Right Merge

```python
pd.merge(df1, df2, how="right")
```

Keeps every row from the right DataFrame.

```
➡️

Right Never Loses Data
```

---

## ✅ Outer Merge

```python
pd.merge(df1, df2, how="outer")
```

Keeps everything from both DataFrames.

```
🌍

Nothing is Lost
```

---

# One-to-One Merge

Each record matches exactly one record.

```
Julia

↓

USA
```

Result

```
Julia → USA
```

---

# One-to-Many Merge

Suppose every department has multiple programming languages.

Department Table

```
Data Science

↓

Python
R
```

Employee Table

```
Julia
Adam
```

Result

```
Julia → Python
Julia → R

Adam → Python
Adam → R
```

### Why are rows repeated?

Because **one department matches multiple programming languages**.

Pandas creates **one output row for every matching record**.

---

# concat() vs merge()

| concat() | merge() |
|-----------|----------|
| Combines DataFrames | Joins DataFrames |
| Uses axis/index | Uses common column |
| Adds rows or columns | Matches related data |
| Similar to stacking | Similar to SQL JOIN |

---

# 🧠 Quick Revision

```
concat()

↓

Combine DataFrames
```

```
axis = 0

↓

Rows ⬇️
```

```
axis = 1

↓

Columns ➡️
```

```
ignore_index=True

↓

Reset Index
```

```
merge()

↓

Join DataFrames
```

```
on="column"

↓

Matching Key 🔑
```

---

# 💡 Interview Questions

### What is the difference between `concat()` and `merge()`?

**concat()**

- Combines DataFrames
- Uses axis
- Adds rows or columns

**merge()**

- Joins DataFrames
- Uses a common column
- Similar to SQL JOIN

---

### When should you use `concat()`?

When you want to stack DataFrames vertically or horizontally.

---

### When should you use `merge()`?

When two DataFrames have related information through a common column.

---

# 🚀 What's Next

- ⏳ `join()`
- ⏳ `groupby()`
- ⏳ `pivot_table()`
- ⏳ `melt()`
- ⏳ `apply()`
- ⏳ `map()`
- ⏳ `sort_values()`
- ⏳ Missing Values
- ⏳ MultiIndex

---

# 🛠 Requirements

```bash
pip install pandas
```

---

# ⭐ Author

**Sami Khan**

Learning Python & Pandas one concept at a time.

If this repository helped you, consider giving it a ⭐.
