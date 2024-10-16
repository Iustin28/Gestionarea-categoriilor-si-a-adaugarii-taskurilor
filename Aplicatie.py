import pandas as pd

def afisare_meniu():
    print("\n--- Meniu Principal ---")
    print("1. Adăugare categorii")
    print("2. Listare taskuri")
    print("3. Sortare taskuri")
    print("4. Filtrare taskuri")
    print("5. Adăugare task nou")
    print("6. Editare task")
    print("7. Ștergere task")
    print("8. Ieșire")


def afisare_meniu_sortare():
    print("\n--- Sortare Taskuri ---")
    print("1. Sortare ascendentă după task")
    print("2. Sortare descendentă după task")
    print("3. Sortare ascendentă după dată")
    print("4. Sortare descendentă după dată")
    print("5. Sortare ascendentă după persoana responsabilă")
    print("6. Sortare descendentă după persoana responsabilă")
    print("7. Sortare ascendentă după categorie")
    print("8. Sortare descendentă după categorie")


def afisare_meniu_filtrare():
    print("\n--- Filtrare Taskuri ---")
    print("1. Filtrare după task")
    print("2. Filtrare după dată")
    print("3. Filtrare după persoana responsabilă")
    print("4. Filtrare după categorie")

Lista_taskuri = {'Task': ['Work1','Work2','Work3','Work7','Work6'],
                 'DataLimita':['01-01-2022','02-02-2023','03-03-2024','06-03-2024','08-03-2024'],
                 'PersoanaResponsabila':['Persoana4','Persoana2','Persoana3','Persoana5','Persoana6'],
                 'Categorie':['Categorie1','Categorie2','Categorie3','Categorie0','Categorie9']
                 }

def main():
    while True:
        afisare_meniu()
        optiune = input("Alegeți o opțiune (1-8): ")

        if optiune == "1":
            # Adăugare categorii
            adaugare_categorii(categorii)
        elif optiune == "2":
            df = pd.read_csv('taskuri.csv')
            # df = pd.DataFrame(Lista_taskuri)
            # Listare taskuri
            print("Listarea taskurilor ascendentă după task\n")
            df_sortat = df.sort_values(by='Categorie')
            print(df_sortat)
        elif optiune == "3":
            afisare_meniu_sortare()
            opt_sortare = input("Alegeți o opțiune de sortare (1-8): ")
            df = pd.read_csv('taskuri.csv')
            # df = pd.DataFrame(Lista_taskuri)
            print(f"\n")
            if opt_sortare == "1":
                print("Listarea taskurilor ascendentă după task\n")
                df_sortat = df.sort_value(by='Task', ascending=True)
                print(df_sortat)
            elif opt_sortare == "2":
                print("Listarea taskurilor descendentă după task\n")
                df_sortat = df.sort_values(by='Task', ascending=False)
                print(df_sortat)
            elif opt_sortare == "3":
                print("Listarea taskurilor ascendentă după dată\n")
                df_sortat = df.sort_values(by='Data', ascending=True)
                print(df_sortat)
            elif opt_sortare == "4":
                print("Listarea taskurilor descendentă după dată\n")
                df_sortat = df.sort_values(by='Data', ascending=False)
                print(df_sortat)
            elif opt_sortare == "5":
                print("Listarea taskurilor ascendentă după persoana responsabilă\n")
                df_sortat = df.sort_values(by='Persoana Responsabila', ascending=True)
                print(df_sortat)
            elif opt_sortare == "6":
                print("Listarea taskurilor desscendentă după persoana responsabilă\n")
                df_sortat = df.sort_values(by='Persoana Responsabila', ascending=False)
                print(df_sortat)
            elif opt_sortare == "7":
                print("Listarea taskurilor ascendentă după categorie\n")
                df_sortat = df.sort_values(by='Categorie', ascending=True)
                print(df_sortat)
            elif opt_sortare == "8":
                print("Listarea taskurilor descendentă după categoriek\n")
                df_sortat = df.sort_values(by='Categorie', ascending=False)
                print(df_sortat)
            else:
             print("\nOptiunea nu este valida. Alege o optiune valida 1-8")
        elif optiune == "4":
            afisare_meniu_filtrare()
            opt_filtrare = input("Alegeți o opțiune de filtrare (1-4): ")
            # Apelați funcțiile de filtrare pe baza opțiunii
        elif optiune == "5":
            # Adăugare task nou
            print("Adăugare task nou...")
            # Aici se va apela o funcție de adăugare task
        elif optiune == "6":
            # Editare task
            print("Editare task...")
            # Aici se va apela o funcție de editare task
        elif optiune == "7":
            # Ștergere task
            print("Ștergere task...")
            # Aici se va apela o funcție de ștergere task
        elif optiune == "8":
            print("Ieșire din program.")
            break
        else:
            print("Opțiune invalidă, vă rugăm să alegeți din nou.")

main()