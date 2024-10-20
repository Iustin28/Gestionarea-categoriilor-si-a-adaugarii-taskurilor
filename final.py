import datetime
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

def editare_task():
    df = pd.read_csv('Taskuri.csv')
    #df = pd.DataFrame(Lista_taskuri)
    df_sortat = pd.DataFrame(df.sort_index())
    len_df_sortat = int(len(df_sortat))
    if len_df_sortat == 0:
        print('Lista este goala, nu ai ce edita')
    else:
        print(f"{df_sortat}\n")
        opt_editare = input(f'Te rog alege o valoarea dintre 0-{len_df_sortat-1}: ')
        while True:
            if opt_editare.isdigit() == True and  int(opt_editare) < len_df_sortat :
                break
            else:
                opt_editare = input(f'Te rog alege o valoarea dintre 0-{len_df_sortat - 1}: ')
        opt_editare = int(opt_editare)
        opt_coloana = input(f'Te rog alege coloana pe care vrei sa o editezi : Task/Data/Persoana Responsabila/Categorie : ')
        while True:
            if  opt_coloana in ['Task','Data','Persoana responsabila','Persoana Responsabila','PersoanaResponsabila','Categorie']:
                break
            else:
                opt_coloana = input(f'Te rog alege coloana pe care vrei sa o editezi : Task/DataLimita/PersoanaResponsabila/Categorie : ')
        if opt_coloana == 'Persoana responsabila' or opt_coloana == 'Persoana Responsabila':
            opt_coloana = 'PersoanaResponsabila'
        if opt_coloana == 'Data':
            print(f"cu ce valoare vrei sa modifici informatia de pe coloana {opt_editare} si anume {df_sortat[opt_coloana][opt_editare]} ")
            year = int(input('An: '))
            month = int(input('Luna: '))
            day = int(input('Zi: '))
            valoare_editata = datetime.date(year, month, day)
        else:
            valoare_editata = input(f"cu ce valoare vrei sa modifici informatia de pe coloana {opt_editare} si anume {df_sortat[opt_coloana][opt_editare]}: ")
        df[opt_coloana][opt_editare] = valoare_editata
        # df.__getitem__(opt_coloana).__setitem__(opt_editare, valoare_editata)
        # df.loc.__setitem__((slice(None), (opt_coloana, opt_editare)), valoare_editata)
        df.to_csv('Taskuri.csv',index=False)
    return



Lista_taskuri = {'Task': ['Work1','Work2','Work3','Work7','Work6'],
                 'DataLimita':['01-01-2022','02-02-2023','03-03-2024','06-03-2024','08-03-2024'],
                 'PersoanaResponsabila':['Persoana4','Persoana2','Persoana3','Persoana5','Persoana6'],
                 'Categorie':['Categorie1','Categorie2','Categorie3','Categorie0','Categorie9']
                 }
def citeste_categorii():
    try:
        df = pd.read_csv("categorii.csv")
        return df['Categorie'].tolist()
    except FileNotFoundError:
        return []


def salveaza_categorii(categorii):
    df = pd.DataFrame({'Categorie': categorii})
    df.to_csv("categorii.csv", index=False)


def adaugare_categorii():
    categorii = citeste_categorii()
    while True:
        categorie_noua = input(
            "Introduceți o nouă categorie (sau apăsați Enter pentru a reveni la meniul principal): ").strip()

        if not categorie_noua:
            break

        if categorie_noua in categorii:
            print(f"Eroare: Categoria '{categorie_noua}' există deja.")
        else:
            categorii.append(categorie_noua)
            print(f"Categoria '{categorie_noua}' a fost adăugată cu succes.")

    salveaza_categorii(categorii)
    print("Categoriile au fost salvate.")

def adaugare_taskuri():
    task = input('Introdu un task ')
    data = input ('introdu data')


def filtrare():

    optiune_filtrare = input("Alegeți o opțiune (1-4): ")
    if optiune_filtrare == "1":  #filtrare dupa task
        task = input("Alegeți un task: ")
        with open('taskuri.csv') as file:
            for row in file:
                if task in row:
                    print(row)
    elif optiune_filtrare == "2":  #filtrare dupa data
        print('Enter the date you wanna start to see the task from: ')
        year1 = int(input('Enter a year'))
        month1 = int(input('Enter a month'))
        day1 = int(input('Enter a day'))
        data1 = datetime.date(year1, month1, day1)
        print("Enter a limit date: ")
        year2 = int(input('Enter a year'))
        month2 = int(input('Enter a month'))
        day2 = int(input('Enter a day'))
        data2 = datetime.date(year2, month2, day2)
        df = pd.read_csv('taskuri.csv')
        with open('taskuri.csv') as file:
            df=pd.read_csv(file)
            # print(df)
            df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d')
            filtrate = df[(df['Data'] >= pd.to_datetime(data1)) & (df['Data'] <= pd.to_datetime(data2))]
            print(filtrate)

    elif optiune_filtrare == "3":
        pers = input("Alegeți o persoana responsabila: ")
        with open('taskuri.csv') as file:
            for row in file:
                if pers in row:
                    print(row)

    elif optiune_filtrare == "4":
        categorie = input("Alegeți o categorie: ")
        with open('taskuri.csv') as file:
            for row in file:
                if categorie in row:
                    print(row)

def stergere_task():
    try:
        #df = pd.read_csv("taskuri.csv")
        df = pd.DataFrame(Lista_taskuri)
        print("\n--- Lista Taskuri ---")
        for i, row in df.iterrows():
            print(
                f"{i + 1}. Task: {row['Task']}, Data: {row['DataLimita']}, Persoana: {row['PersoanaResponsabila']}, Categorie: {row['Categorie']}")

        task_id = input("\nIntroduceți numărul taskului pe care doriți să îl ștergeți: ")

        while True:
            if task_id.isdigit() == True and int(task_id) < len(df):
                break
            else:
                task_id = input('Introduceti un numar valid:')

        task_id = int(task_id) -1
        # Confirmare ștergere task
        task_de_sters = df.loc[task_id, 'Task']
        confirmare = input(f"Sigur doriți să ștergeți taskul '{task_de_sters}'? (da/nu): ").strip().lower()

        if confirmare == "da":
            df = df.drop(task_id).reset_index(drop=True)

            df.to_csv('taskuri.csv', index=False)
            print(f"Taskul '{task_de_sters}' a fost șters cu succes.")
        else:
            print("Ștergerea taskului a fost anulată.")
    except ValueError:
        print("Input invalid. Introduceți un număr valid.")
    print(df)
    return

def main():
    while True:
        afisare_meniu()
        optiune = input("Alegeți o opțiune (1-8): ")

        if optiune == "1":
            # Adăugare categorii
            adaugare_categorii()
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
                df_sortat = df.sort_values(by='Task', ascending=True)
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
            editare_task()
        elif optiune == "7":
            # Ștergere task
            print("Ștergere task...")
            stergere_task()
            # Aici se va apela o funcție de ștergere task
        elif optiune == "8":
            print("Ieșire din program.")
            break
        else:
            print("Opțiune invalidă, vă rugăm să alegeți din nou.")

main()