from examples.example1_dataframe import run as ex1
from examples.example2_read_csv import run as ex2

while True:
    print("\n===== PANDAS PIEMĒRI =====")
    print("1 - DataFrame")
    print("2 - CSV nolasīšana")
    print("0 - Iziet")

    choice = input("Izvēle: ")

    if choice == "1":
        ex1()

    elif choice == "2":
        ex2()

    elif choice == "0":
        break

    else:
        print("Nepareiza izvēle")
