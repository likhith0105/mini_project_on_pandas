import pandas as pd

data = {
    "Name":["A","B","C"],
    "Marks":[85,70,90]
}

df = pd.DataFrame(data)

print(df.sort_values(by="Marks"))