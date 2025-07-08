import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": ["bantee", "sharma", "akash", "bob", "alice"],
    "place": ["Delhi", "Mumbai", "Chennai", "Kolkata", "Bangalore"],
    "salary": [50000, 60000, 55000, 70000, 65000],
    "date": ["2023-01-10", "2023-02-15", "2023-03-20", "2023-04-25", "2023-05-30"],
    "department": ["HR", "Finance", "IT", "Marketing", "Sales"],
    "age": [28, 32, 25, 29, 31],
    "experience_years": [3, 7, 2, 5, 6]
})

print(df)