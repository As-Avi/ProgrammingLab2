import pandas as pd
import numpy as np
import seaborn as sns
import random as rd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


#Esercizio 1
def lancio_moneta():
    risultato = rd.randint(0,1)
    return risultato

def frequenza_risultati(n):
    testa = 0
    croce = 0
    for i in range(n):
        risultato = lancio_moneta()
        if risultato == 0:
            testa += 1
        else:
            croce += 1
    perc_testa = (testa / n) * 100
    perc_croce = (croce / n) * 100
    return perc_testa, perc_croce

#n = int(input())
#print("Frequenza risultati dopo " + str(n) + " lanci: " + str(frequenza_risultati(n))) 

for i in range(100):
    x = rd.randint(10, 20000)
    perc_testa, perc_croce = frequenza_risultati(x)
    #print(f"Testa: {perc_testa:.2f}%, Croce: {perc_croce:.2f}%")
        
plt.bar(['Testa', 'Croce'], [perc_testa, perc_croce], color=['blue', 'orange'])
plt.title("Frequenza risultati dopo 100 lanci")
plt.xlabel('Testa/Croce')
plt.ylabel('Frequenza (%)')
plt.show()


#Esercizio 2
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
df.head()

# Quante righe e colonne ha il dataset?
righe, colonne = df.shape
print(f"Il dataset ha {righe} righe e {colonne} colonne.")

# Controlla quanti valori mancanti ci sono per colonna
print(df.isnull().sum())

# Riempi i valori mancanti nella colonna 'Embarked' con il valore più frequente
x = df['Embarked'].mode()[0]
df['Embarked'] = df['Embarked'].fillna(x)

# Rimuovi le righe dove il valore di 'Age' è mancante
#if df['Age'].isnull().sum() > 0:
    #df = df.dropna(subset=['Age'])

df = df.dropna(subset=['Fare'])   

# Controlla se ci sono righe duplicate
duplicates_rows = df[df.duplicated()]
if duplicates_rows.empty:
    print("Non ci sono righe duplicate.")
else:
    print(f"Ci sono {duplicates_rows.shape[0]} righe duplicate.")

# Calcola l'età media dei passeggeri per ogni classe (Pclass), se ci sono valori mancanti di età riempili con il valore medio
age_by_class = df.groupby('Pclass')['Age'].mean()
print("Età media per classe:")
print(age_by_class)

# Visualizza la distribuzione dell'età per classe

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Age', hue='Pclass', multiple='stack', kde=True)
plt.title("Distribuzione dell'età per classe")
plt.xlabel("Età")
plt.ylabel("Frequenza")
plt.legend(title='Classe', loc='upper right')
plt.show()

# Visualizza la distribuzione dell'età per classe dividendo e mmostrando insieme i dati di uomini e donne

plt.figure(figsize=(10, 6))
sns.boxplot(x='Pclass', y='Age', hue='Sex', data=df)
plt.title("Distribuzione dell'età per classe e genere")
plt.show()


#Esercizio 3
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
df.head()

# Esplora la distribuzione delle specie (conta quanti campioni ci sono per specie)
print("Distribuzione delle specie:")
print(df['species'].value_counts())

# Calcola la lunghezza e la larghezza media dei petali per specie
print("Lunghezza e larghezza media dei petali per specie:")
print(df.groupby('species')[['petal_length', 'petal_width']].mean())

# Visualizza le dimensioni dei petali per specie (scatterplot)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='petal_length', y='petal_width', hue='species')
plt.title('Dimensioni dei petali per specie')
plt.xlabel('Lunghezza petalo (cm)')
plt.ylabel('Larghezza petalo (cm)')
plt.show()

# Crea una nuova colonna per l'area del petalo e analizzala
df['petal_area'] = df['petal_length'] * df['petal_width']
print("Statistiche dell'area del petalo per specie:")
print(df.groupby('species')['petal_area'].describe())

# Grafico della distribuzione dell'area del petalo per specie (boxplot)
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='species', y='petal_area')
plt.title("Distribuzione dell'area del petalo per specie")
plt.xlabel('Specie')
plt.ylabel('Area del petalo (cm²)')
plt.show()
