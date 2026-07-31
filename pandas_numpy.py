import pandas as pd
df4 = pd.DataFrame({
    "employee": ["Julia", "Marie", "Adam", "Nicole"],
    "department": ["Data Science", "Web Development", "Data Science", "Cyber Security"],
    "salary": [20000, 17500, 16000, 22000]
})

df6 = pd.DataFrame({
    "employee": [
        "Julia",
        "Julia",
        "Adam",
        "Adam",
        "Marie",
        "Nicole"
    ],
    "department": [
        "Data Science",
        "Data Science",
        "Data Science",
        "Data Science",
        "Web Development",
        "Cyber Security"
    ],
    "prog_lang": [
        "Python",
        "R",
        "Python",
        "R",
        "HTML",
        "SQL"
    ]
})

result1 = pd.merge(df4, df6, on=["employee", "department"])
print(result1)