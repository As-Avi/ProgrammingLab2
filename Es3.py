import pandas as pd
import numpy as np
from datasets import load_dataset
import matplotlib.pyplot as plt  # Corretto l'import
import matplotlib.colors as mcolors

# Esercizio 1
df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv")
primi_10 = df.sort_values('total_litres_of_pure_alcohol', ascending=False, inplace=False).head(10)
print(primi_10)

df_mean = df[['beer_servings', 'spirit_servings', 'wine_servings']].mean(axis=1)
print(df_mean)

# Correzione: Calcolo corretto di 'alcohol_index'
df['alcohol_index'] = (df['beer_servings'] + df['wine_servings'] + df['spirit_servings']) / 3

# Paese con il massimo 'alcohol_index'
print(df.country[df['alcohol_index'].idxmax()])

# Ordinamento per 'alcohol_index' e selezione del primo paese
print(df.sort_values('alcohol_index', ascending=False).head(1)['country'])

# Paese con 'alcohol_index' massimo
print(df[df['alcohol_index'] == df['alcohol_index'].max()]['country'])

# Paesi con 'beer_servings' > 100
print(df[df['beer_servings'] > 100])  # Corretto 'beer_servinfs'

# Grafico a barre per i primi 10 paesi
plt.bar(primi_10['country'], primi_10['total_litres_of_pure_alcohol'])
plt.xlabel('Country')
plt.ylabel('Total Litres of Pure Alcohol')
plt.title('Top 10 Countries by Alcohol Consumption')
plt.xticks(rotation=90)
plt.show()


# Esercizio 2
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

paesi = df['country'].unique()
for paese in paesi:
    dati_paese = df[df['job_country'] == paese]
    dati_lavoro = dati_paese.groupby('job_title_short')['salaey_year_avg'].mean()
    dati_lavoro.plot(kind='barh')
    plt.title(f"Average Salary by Job Title in {paese}")
    plt.xlabel('Average Salary')
    plt.ylabel('Job Title')
    plt.show()
    
    print(dati_lavoro.keys)