import pandas as pd

def run():

    # Nolasa CSV
    df = pd.read_csv("data/students.csv")

    # Saglabā jaunu CSV failu
    df.to_csv("data/output.csv", index=False)

    print("Fails saglabāts")
