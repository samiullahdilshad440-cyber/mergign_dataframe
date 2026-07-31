---

# 🔹 Merge on Multiple Columns

Sometimes, one column is **not enough** to uniquely identify a record. In such cases, Pandas allows you to merge using **multiple columns**.

```python
result = pd.merge(df4, df6, on=["employee", "department"])
```

## Example

### DataFrame 1 (Employee Details)

| employee | department | salary |
|----------|------------|--------|
| Julia | Data Science | 20000 |
| Marie | Web Development | 17500 |
| Adam | Data Science | 16000 |
| Nicole | Cyber Security | 22000 |

---

### DataFrame 2 (Programming Languages)

| employee | department | prog_lang |
|----------|------------|-----------|
| Julia | Data Science | Python |
| Julia | Data Science | R |
| Adam | Data Science | Python |
| Adam | Data Science | R |
| Marie | Web Development | HTML |
| Nicole | Cyber Security | SQL |

---

## Merge

```python
result = pd.merge(df4, df6, on=["employee", "department"])
```

### Output

| employee | department | salary | prog_lang |
|----------|------------|--------|-----------|
| Julia | Data Science | 20000 | Python |
| Julia | Data Science | 20000 | R |
| Adam | Data Science | 16000 | Python |
| Adam | Data Science | 16000 | R |
| Marie | Web Development | 17500 | HTML |
| Nicole | Cyber Security | 22000 | SQL |

---

## 🧠 Dry Run

Pandas checks **both columns** before merging.

```
employee        department

Julia       ✔   Data Science ✔

↓

Merged
```

```
employee        department

Adam        ✔   Data Science ✔

↓

Merged
```

Both conditions must be **TRUE**.

---

## ❌ Incorrect Example

Suppose `df6` looks like this:

| department | prog_lang |
|------------|-----------|
| Data Science | Python |
| Data Science | R |

Now run

```python
pd.merge(df4, df6, on=["employee", "department"])
```

This will produce

```text
KeyError: 'employee'
```

### Why?

Because `df6` does **not** contain the **employee** column.

For a merge on multiple columns, **every column listed in `on=[...]` must exist in both DataFrames.**

---

## 💡 Memory Trick

### Merge on One Column

```python
pd.merge(df1, df2, on="employee")
```

```
Employee ✔

↓

Merge
```

---

### Merge on Multiple Columns

```python
pd.merge(df1, df2, on=["employee", "department"])
```

```
Employee ✔
      AND
Department ✔

↓

Merge
```

---

## 📌 Rule to Remember

✅ One column

```python
on="employee"
```

Only **employee** must exist in both DataFrames.

---

✅ Multiple columns

```python
on=["employee", "department"]
```

Both **employee** and **department** must exist in both DataFrames.

If even one column is missing, Pandas raises a **KeyError**.

---

### Quick Summary

| Merge Type | Requirement |
|------------|-------------|
| `on="employee"` | `employee` must exist in both DataFrames |
| `on=["employee", "department"]` | Both columns must exist in both DataFrames |
| Missing column | `KeyError` |

> **Easy Formula:**  
> **More columns in `on` = More conditions that must match.** 🔑
