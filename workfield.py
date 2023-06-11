import pandas as pd
import sqlite3

df = pd.read_csv('club.csv',  sep="\t")

conn = sqlite3.connect('football.db')

# dobavq ot csv v sql
#df.to_sql('clubs', conn, if_exists='append', index=False)

#printira vsichko ot sql
football_data = pd.read_sql("select * from clubs",  conn)

#printira ispanskite otbori
filter_row = football_data[football_data["country"] == "Spain"]

#smenq dyrjavata za printa
replace_country = football_data.replace("England", "UK")
print(replace_country)
conn.close()
