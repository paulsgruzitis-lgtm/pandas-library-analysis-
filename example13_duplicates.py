import pandas as pd

def run():

    # Nolasa CSV
    df = pd.read_csv("data/students.csv")

    # Noņem dublikātus
    print(df.drop_duplicates())
