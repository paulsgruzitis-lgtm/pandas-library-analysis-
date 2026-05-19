import pandas as pd

def run():

    data = {
        "Vards": ["Anna", "Juris"],
        "Vecums": [20, 25]
    }

    df = pd.DataFrame(data)

    print(df)
