import pandas as pd

def run():

    # Nolasa CSV
    df = pd.read_csv("data/students.csv")

    # Pārbauda tukšās vērtības
    print(df.isnull())
