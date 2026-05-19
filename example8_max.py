import pandas as pd

def run():

    # Nolasa CSV
    df = pd.read_csv("data/students.csv")

    # Atrod lielāko vērtību
    print(df["Vecums"].max())
