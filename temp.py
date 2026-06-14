import pandas as pd

df = pd.read_csv("data/raw/data.csv")
df = df.reset_index(names = "sentence_id")
df = df.drop_duplicates(subset = "Sentence", keep = "first")
print(len(df))

print(len(df.Sentence.unique()))