# Pandas Concatenation & Merge

A beginner-friendly repository demonstrating how to combine DataFrames
using **Pandas**.

## Topics Covered

-   `pd.concat()`
    -   Row-wise concatenation (`axis=0`)
    -   Column-wise concatenation (`axis=1`)
    -   `ignore_index=True`
-   `pd.merge()`
    -   Inner Merge
    -   Left Merge
    -   Right Merge
    -   Outer Merge

## Project Structure

``` text
.
├── concat_examples.py
├── merge_examples.py
└── README.md
```

## Concepts

### 1. `pd.concat()`

Used to combine multiple DataFrames.

``` python
result = pd.concat([df1, df2])
```

-   `axis=0` → Stack rows (default)
-   `axis=1` → Combine columns side by side
-   `ignore_index=True` → Reset the index

### 2. `pd.merge()`

Used to join DataFrames using a common column.

``` python
result = pd.merge(df1, df2, on="employee")
```

Merge types: - **Inner** → Only matching rows - **Left** → Keep all rows
from the left DataFrame - **Right** → Keep all rows from the right
DataFrame - **Outer** → Keep all rows from both DataFrames

## Learning Outcome

After completing these examples, you will understand:

-   DataFrame concatenation
-   Vertical vs. horizontal concatenation
-   Index handling
-   Joining DataFrames using common columns
-   Different merge strategies

## Requirements

-   Python 3.x
-   pandas

Install pandas:

``` bash
pip install pandas
```

## Author

**Sami Khan**

Happy Coding! 🚀
