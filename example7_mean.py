import pandas as pd

def run():

    # Nolasa CSV
    df = pd.read_csv("data/students.csv")

    # Aprēķina vidējo vērtību
    print(df["Vecums"].mean())
