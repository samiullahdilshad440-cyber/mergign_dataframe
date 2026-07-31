---
# 🔹 Merge Using the `how` Parameter

The `how` parameter controls **which rows are included** when merging two DataFrames.

```python
result = pd.merge(df1, df2, on="employee", how="inner")
```
---

## Example DataFrames

### DataFrame 1 (Employee Details)

| employee | department      |
| -------- | --------------- |
| Julia    | Data Science    |
| Marie    | Web Development |
| Adam     | Data Science    |
| Nicole   | Cyber Security  |

---

### DataFrame 2 (Employee Country)

| employee | country |
| -------- | ------- |
| Julia    | USA     |
| Adam     | England |
| David    | Canada  |
| Marie    | Germany |

Notice:

- **Nicole** exists only in **df1**
- **David** exists only in **df2**

This helps us understand how each merge type works.

---

# 1️⃣ Inner Merge

```python
result = pd.merge(df1, df2, on="employee", how="inner")
```

### Output

| employee | department      | country |
| -------- | --------------- | ------- |
| Julia    | Data Science    | USA     |
| Marie    | Web Development | Germany |
| Adam     | Data Science    | England |

### Explanation

Only employees present in **both DataFrames** are returned.

---

# 2️⃣ Left Merge

```python
result = pd.merge(df1, df2, on="employee", how="left")
```

### Output

| employee | department      | country |
| -------- | --------------- | ------- |
| Julia    | Data Science    | USA     |
| Marie    | Web Development | Germany |
| Adam     | Data Science    | England |
| Nicole   | Cyber Security  | NaN     |

### Explanation

All rows from the **left DataFrame** are kept.

If no matching record exists in the right DataFrame, Pandas fills the missing values with **NaN**.

---

# 3️⃣ Right Merge

```python
result = pd.merge(df1, df2, on="employee", how="right")
```

### Output

| employee | department      | country |
| -------- | --------------- | ------- |
| Julia    | Data Science    | USA     |
| Adam     | Data Science    | England |
| David    | NaN             | Canada  |
| Marie    | Web Development | Germany |

### Explanation

All rows from the **right DataFrame** are kept.

Since **David** doesn't exist in the left DataFrame, the department becomes **NaN**.

---

# 4️⃣ Outer Merge

```python
result = pd.merge(df1, df2, on="employee", how="outer")
```

### Output

| employee | department      | country |
| -------- | --------------- | ------- |
| Julia    | Data Science    | USA     |
| Marie    | Web Development | Germany |
| Adam     | Data Science    | England |
| Nicole   | Cyber Security  | NaN     |
| David    | NaN             | Canada  |

### Explanation

Outer Merge keeps **every row** from both DataFrames.

If a record doesn't have a match, the missing values are filled with **NaN**.

---

# 🧠 Dry Run

### Employees in DataFrame 1

```
Julia
Marie
Adam
Nicole
```

↓

### Employees in DataFrame 2

```
Julia
Adam
David
Marie
```

---

## 🤝 Inner Merge

```
Common Employees

✔ Julia
✔ Marie
✔ Adam
```

Result

```
Julia
Marie
Adam
```

Only common employees are returned.

---

## ⬅️ Left Merge

```
Keep Everything From Left

Julia
Marie
Adam
Nicole
```

Nicole has no matching country.

```
Nicole → NaN
```

---

## ➡️ Right Merge

```
Keep Everything From Right

Julia
Adam
David
Marie
```

David has no matching department.

```
David → NaN
```

---

## 🌍 Outer Merge

```
Take Everything

Julia
Marie
Adam
Nicole
David
```

No employee is removed.

---

# 💡 Memory Trick

### 🤝 Inner Merge

```
Common Records Only
```

---

### ⬅️ Left Merge

```
Keep Every Row
From Left DataFrame
```

---

### ➡️ Right Merge

```
Keep Every Row
From Right DataFrame
```

---

### 🌍 Outer Merge

```
Keep Everything
From Both DataFrames
```

---

# 📌 Quick Summary

| Merge Type    | Keeps                             |
| ------------- | --------------------------------- |
| `how="inner"` | Only matching rows                |
| `how="left"`  | All rows from the left DataFrame  |
| `how="right"` | All rows from the right DataFrame |
| `how="outer"` | All rows from both DataFrames     |

---

# 🎯 Rule to Remember

- 🤝 **Inner** → Common rows only.
- ⬅️ **Left** → Left DataFrame is always complete.
- ➡️ **Right** → Right DataFrame is always complete.
- 🌍 **Outer** → Keep every row from both DataFrames.

> **Easy Formula:**  
> **The `how` parameter decides which rows survive after the merge.**
