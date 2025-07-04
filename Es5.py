import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Esercizio 2
url = 'https://zenodo.org/record/5898311/files/vgsales.csv'
df = pd.read_csv(url)
df.head()

num_games = df['Name'].nunique()
print(f"Il numero di giochi è: {num_games}")

genre_counts = df['Genre'].value_counts()

plt.figure(figsize=(10, 5))
genre_counts.plot(kind='bar', color='skyblue')
plt.title('Conteggio dei giochi per genere')
plt.xlabel('Genere')
plt.ylabel('Conteggio')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

top_generi = genre_counts.nlargest(5).index
df_top = df[df['Genre'].apply(lambda x: x in top_generi)]
vendite_regioni = df_top.groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales']].sum()
vendite_regioni.plot(kind='bar', stacked=True, title='Vendite per regione per i primi 5 generi')
plt.ylabel('Milioni di unita')
plt.tight_layout()
plt.show()

#vedi lezione Aprile 07/04/2025