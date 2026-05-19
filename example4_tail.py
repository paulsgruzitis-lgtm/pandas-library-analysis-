import pandas as pd

def run():

    # Nolasa CSV
    df = pd.read_csv("data/students.csv")

    # Parāda pēdējās rindas
    print(df.tail())
