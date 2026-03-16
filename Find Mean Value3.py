import pandas as pd

data = {"Marks":[70,80,90,60]}
df = pd.DataFrame(data)

print("Average Marks:", df["Marks"].mean())