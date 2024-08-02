import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('vox1_meta.csv', delimiter='\t')

gender_mapping = {'m': 'Hombre', 'f': 'Mujer'}
data['Gender'] = data['Gender'].replace(gender_mapping)

# Distribución de sexos
gender_percentage = data['Gender'].value_counts(normalize=True)*100
plt.figure(figsize=(8, 6))
gender_percentage.plot(kind='bar', color=['skyblue', 'pink'])
plt.xlabel('Sexo')
plt.ylabel('%')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


colors = ['lightgreen', 'skyblue', 'pink', 'orange', 'yellow', 'purple', 'red', 'cyan', 'magenta', 'limegreen', 'grey']

# Distribución de nacionalidades
nation_mapping = {'USA': 'EEUU', 'UK': 'Reino Unido', 'Norway': 'Noruega', 'Ireland': 'Irlanda', 'Germany': 'Alemania', 'New Zealand': 'Nueva Zelanda', 'Italy': 'Italia'}
data['Nationality'] = data['Nationality'].replace(nation_mapping)
nationality_counts = data['Nationality'].value_counts(normalize=True)*100
top_nationalities = nationality_counts.head(10)
other_nationalities = nationality_counts[10:].sum()  
nationalities_combined = top_nationalities.append(pd.Series({'Otros': other_nationalities}))
plt.figure(figsize=(10, 6))
nationalities_combined.plot(kind='bar', color = colors)
plt.xlabel('Nacionalidad')
plt.ylabel('%')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
