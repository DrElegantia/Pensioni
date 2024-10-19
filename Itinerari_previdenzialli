import tabula

# Specifica il percorso del tuo file PDF
file_path = "https://www.itinerariprevidenziali.it/site/home/biblioteca/pubblicazioni/documento32059891.html"

# Specifica il numero della pagina contenente la tabella
page_number = 91

# Esegui l'estrazione dei dati
df_list = tabula.read_pdf(file_path, pages=page_number)

# Utilizza la seconda riga come intesta delle colonne
df = df_list[0].iloc[1:]

# Reimposta gli indici del DataFrame
df.reset_index(drop=True, inplace=True)

# Visualizza il DataFrame risultante
print(df)
