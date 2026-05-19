import pandas as pd

def run():

    # Nolasa CSV
    df = pd.read_csv("data/students.csv")

    # Filtrē vecumu virs 21
    result = df[df["Vecums"] > 21]

    print(result)
