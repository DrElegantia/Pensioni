import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Impostazioni per visualizzare tutte le colonne e righe
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)

# Funzione per pulire i dati rimuovendo punti e virgole e convertendo in float
def pulisci_dati(colonna):
    return colonna.replace({r'\.': '', ',': '.'}, regex=True).astype(float)

# Carica i dati dal file Excel per pensionati
pensionati = pd.read_excel('dati_pensioni_per_pensionato.xlsx')

# Rimuovi le colonne inutili e limita i dati
del pensionati['Unnamed: 0']
del pensionati['Unnamed: 2']
pensionati = pensionati[0:51]

# Pulisci le colonne 'Importo complessivo' e 'Pensionati'
pensionati['Importo complessivo'] = pulisci_dati(pensionati['Importo complessivo'])
pensionati['Pensionati'] = pulisci_dati(pensionati['Pensionati'])

# Carica i dati dal file Excel per pensioni
pensioni = pd.read_excel('dati_pensioni_per_pensione.xlsx')
del pensioni['Unnamed: 0.1']

# Rinominare la colonna e combinare i dati per la categoria
pensioni = pensioni.rename(columns={'Unnamed: 0': 'Categoria'})
pensioni['Categoria'] = pensioni['Classi di importo mensile'] + " " + pensioni['Categoria']
del pensioni['Classi di importo mensile']
pensioni = pensioni[0:51]

# Pulisci le colonne 'Importo complessivo' e 'Numero di'
pensioni['Importo complessivo'] = pulisci_dati(pensioni['Importo complessivo'])
pensioni['Numero di'] = pulisci_dati(pensioni['Numero di'])

# Unisci i dati su 'Categoria'
merged_data = pd.merge(pensionati, pensioni, on='Categoria')

# Estrai i dati necessari
categorie = merged_data['Categoria']
importo_pensionati = merged_data['Importo complessivo_x']  # Importo pensionati
importo_pensioni = merged_data['Importo complessivo_y']  # Importo pensioni
numero_pensionati = merged_data['Pensionati']  # Numero pensionati
numero_pensioni = merged_data['Numero di']  # Numero pensioni

# Crea i subplot (due righe, una colonna)
fig = make_subplots(rows=2, cols=1, subplot_titles=("Importo Complessivo Pensioni e Pensionati", "Numero di Pensioni e Pensionati"))

# Primo grafico: Importo complessivo
fig.add_trace(go.Scatter(x=categorie, y=importo_pensioni, mode='lines+markers', name='Importo Pensioni'),
              row=1, col=1)
fig.add_trace(go.Scatter(x=categorie, y=importo_pensionati, mode='lines+markers', name='Importo Pensionati'),
              row=1, col=1)

# Secondo grafico: Numero di pensioni e pensionati
fig.add_trace(go.Scatter(x=categorie, y=numero_pensioni, mode='lines+markers', name='Numero di Pensioni'),
              row=2, col=1)
fig.add_trace(go.Scatter(x=categorie, y=numero_pensionati, mode='lines+markers', name='Numero di Pensionati'),
              row=2, col=1)

# Impostazioni layout
fig.update_layout(height=2000, width=1900, title_text="Importo Complessivo e Numero di Pensioni e Pensionati per Categoria")

# Titoli degli assi
fig.update_xaxes(title_text="Categoria Pensionati", row=1, col=1)
fig.update_xaxes(title_text="Categoria Pensionati", row=2, col=1)
fig.update_yaxes(title_text="Importo Complessivo", row=1, col=1)
fig.update_yaxes(title_text="Numero di Pensioni e Pensionati", row=2, col=1)

# Mostra il grafico
fig.show()
