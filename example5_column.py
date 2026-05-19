import pandas as pd

def run():

    # Nolasa CSV
    df = pd.read_csv("data/students.csv")

    # Parāda kolonnu
    print(df["Vards"])
