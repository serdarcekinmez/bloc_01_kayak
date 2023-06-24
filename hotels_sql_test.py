
import pandas as pd
import sqlite3

data = pd.read_csv('frenchhotels.csv')

conn = sqlite3.connect('french_hotels.db')

# Divide the data into chunks to see if it works
chunk_size = 1000 ### no need to chunk . Functions speedily
chunks = [data[i:i+chunk_size] for i in range(0,data.shape[0],chunk_size)]

for i, chunk in enumerate(chunks):
    chunk.to_sql('french_hotels', conn, if_exists='append' if i > 0 else 'replace', index=False)
    print(f'Chunk {i+1} of {len(chunks)} written to database')

conn.close()

