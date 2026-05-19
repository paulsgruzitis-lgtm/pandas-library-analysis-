import pandas as pd

def run():

    # Nolasa CSV
    df = pd.read_csv("data/students.csv")

    # Atrod mazāko vērtību
    print(df["Vecums"].min())
