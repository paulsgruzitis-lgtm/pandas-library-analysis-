import pandas as pd

def run():

    # Nolasa CSV
    df = pd.read_csv("data/students.csv")

    # Sakārto datus
    print(df.sort_values("Vecums"))
