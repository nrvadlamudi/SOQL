import pandas as pd

input_file = "./queries.csv"

df = pd.read_csv(input_file, header=0)

malicious = df[df["Label"] == 1]
benign = df[df["Label"] == 0]

malicious.to_csv("malicious.csv", index=False)
benign.to_csv("benign.csv", index=False)
