import pandas as pd
import datetime

df = pd.DataFrame({'Task': ['Mananca', 'Mergi', 'Dormi', 'Visezi'], 'Data': [datetime.datetime(2022,10,2), datetime.datetime(2021,10,2),datetime.datetime(2020,10,2),datetime.datetime(2019,10,2) ],
                   'Persoana_Responsabila': ['Andrei', 'Ioana', 'Cristina', 'Marian'], 'Categorie':['Actiune','Plimbare',"Odihna",'Odihna']})

with open ('taskuri.csv', 'w+') as file:
    file.write(df.to_csv())

