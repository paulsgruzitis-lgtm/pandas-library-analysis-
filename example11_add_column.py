import pandas as pd

def run():

    # Nolasa CSV
    df = pd.read_csv("data/students.csv")

    # Pievieno jaunu kolonnu
    df["Pilngadigs"] = True

    print(df)
