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

def citire_taskuri():
    try:
        df = pd.read_csv("taskuri.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Task', 'DataLimita', 'PersoanaResponsabila', 'Categorie'])
    return df

def salvare_taskuri(df):
    df.to_csv("taskuri.csv", index=False)

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
        categorie_noua = input("Introduceți o nouă categorie (sau apăsați Enter pentru a reveni la meniul principal): ").strip()
        if not categorie_noua:
            break
        if categorie_noua in categorii:
            print(f"Eroare: Categoria '{categorie_noua}' există deja.")
        else:
            categorii.append(categorie_noua)
            print(f"Categoria '{categorie_noua}' a fost adăugată cu succes.")
    salveaza_categorii(categorii)
    print("Categoriile au fost salvate.")

def adaugare_task():
    df = citire_taskuri()
    task = input("Introduceți numele taskului: ").strip()
    year = int(input("Introduceți anul limită: "))
    month = int(input("Introduceți luna limită: "))
    day = int(input("Introduceți ziua limită: "))
    data_limita = datetime.date(year, month, day).strftime('%Y-%m-%d')
    persoana_responsabila = input("Introduceți persoana responsabilă: ").strip()
    categorie = input("Introduceți categoria: ").strip()

    # df = df.append({'Task': task, 'DataLimita': data_limita, 'PersoanaResponsabila': persoana_responsabila, 'Categorie': categorie}, ignore_index=True)
    # salvare_taskuri(df)
    # print(f"Taskul '{task}' a fost adăugat cu succes.")
    nou_task = {
        'Task': task,
        'DataLimita': data_limita,
        'PersoanaResponsabila': persoana_responsabila,
        'Categorie': categorie
    }
    df = pd.concat([df, pd.DataFrame([nou_task])], ignore_index=True)
    salvare_taskuri(df)
    print(f"Taskul '{task}' a fost adăugat cu succes.")

def editare_task():
    df = citire_taskuri()
    if df.empty:
        print("Nu există taskuri de editat.")
        return

    print("\n--- Lista Taskuri ---")
    print(df)
    opt_editare = int(input(f'Alegeți indicele taskului pe care doriți să-l editați (0-{len(df)-1}): '))
    while opt_editare not in range(len(df)):
        opt_editare = int(input(f'Alegeți un indice valid (0-{len(df)-1}): '))

    opt_coloana = input("Alegeți coloana de editat (Task/Data/PersoanaResponsabila/Categorie): ").strip()
    if opt_coloana == 'Data':
        year = int(input('An: '))
        month = int(input('Luna: '))
        day = int(input('Zi: '))
        valoare_editata = datetime.date(year, month, day).strftime('%Y-%m-%d')
    else:
        valoare_editata = input(f"Introduceți noua valoare pentru {opt_coloana}: ")

    df.at[opt_editare, opt_coloana] = valoare_editata
    salvare_taskuri(df)
    print("Taskul a fost actualizat cu succes.")

def stergere_task():
    df = citire_taskuri()
    if df.empty:
        print("Nu există taskuri de șters.")
        return

    print("\n--- Lista Taskuri ---")
    for i, row in df.iterrows():
        print(f"{i}. Task: {row['Task']}, Data: {row['DataLimita']}, Persoana: {row['PersoanaResponsabila']}, Categorie: {row['Categorie']}")

    task_id = int(input(f"Alegeți numărul taskului pe care doriți să-l ștergeți (0-{len(df)-1}): "))
    while task_id not in range(len(df)):
        task_id = int(input(f"Alegeți un număr valid (0-{len(df)-1}): "))

    task_de_sters = df.at[task_id, 'Task']
    confirmare = input(f"Sigur doriți să ștergeți taskul '{task_de_sters}'? (da/nu): ").strip().lower()

    if confirmare == "da":
        df = df.drop(task_id).reset_index(drop=True)
        salvare_taskuri(df)
        print(f"Taskul '{task_de_sters}' a fost șters cu succes.")
    else:
        print("Ștergerea taskului a fost anulată.")

def filtrare():
    df = citire_taskuri()
    if df.empty:
        print("Nu există taskuri de filtrat.")
        return

    afisare_meniu_filtrare()
    optiune_filtrare = input("Alegeți o opțiune (1-4): ")

    if optiune_filtrare == "1":
        task = input("Introduceți numele taskului: ").strip()
        filtrate = df[df['Task'].str.contains(task, case=False, na=False)]
        print(filtrate)
    elif optiune_filtrare == "2":
        year1 = int(input("Introduceți anul de start: "))
        month1 = int(input("Introduceți luna de start: "))
        day1 = int(input("Introduceți ziua de start: "))
        data1 = datetime.date(year1, month1, day1).strftime('%Y-%m-%d')

        year2 = int(input("Introduceți anul limită: "))
        month2 = int(input("Introduceți luna limită: "))
        day2 = int(input("Introduceți ziua limită: "))
        data2 = datetime.date(year2, month2, day2).strftime('%Y-%m-%d')

        filtrate = df[(df['DataLimita'] >= data1) & (df['DataLimita'] <= data2)]
        print(filtrate)
    elif optiune_filtrare == "3":
        persoana = input("Introduceți persoana responsabilă: ").strip()
        filtrate = df[df['PersoanaResponsabila'].str.contains(persoana, case=False, na=False)]
        print(filtrate)
    elif optiune_filtrare == "4":
        categorie = input("Introduceți categoria: ").strip()
        filtrate = df[df['Categorie'].str.contains(categorie, case=False, na=False)]
        print(filtrate)

def sortare():
    df = citire_taskuri()
    if df.empty:
        print("Nu există taskuri de sortat.")
        return

    afisare_meniu_sortare()
    optiune_sortare = input("Alegeți o opțiune de sortare (1-8): ")

    if optiune_sortare == "1":
        df = df.sort_values(by='Task', ascending=True)
    elif optiune_sortare == "2":
        df = df.sort_values(by='Task', ascending=False)
    elif optiune_sortare == "3":
        df = df.sort_values(by='DataLimita', ascending=True)
    elif optiune_sortare == "4":
        df = df.sort_values(by='DataLimita', ascending=False)
    elif optiune_sortare == "5":
        df = df.sort_values(by='PersoanaResponsabila', ascending=True)
    elif optiune_sortare == "6":
        df = df.sort_values(by='PersoanaResponsabila', ascending=False)
    elif optiune_sortare == "7":
        df = df.sort_values(by='Categorie', ascending=True)
    elif optiune_sortare == "8":
        df = df.sort_values(by='Categorie', ascending=False)

    print(df)

def main():
    while True:
        afisare_meniu()
        optiune = input("Alegeți o opțiune (1-8): ").strip()

        if optiune == "1":
            adaugare_categorii()
        elif optiune == "2":
            df = citire_taskuri()
            print(df)
        elif optiune == "3":
            sortare()
        elif optiune == "4":
            filtrare()
        elif optiune == "5":
            adaugare_task()
        elif optiune == "6":
            editare_task()
        elif optiune == "7":
            stergere_task()
        elif optiune == "8":
            print("Ieșire.")
            break
        else:
            print("Opțiune invalidă. Vă rugăm să încercați din nou.")

main()
