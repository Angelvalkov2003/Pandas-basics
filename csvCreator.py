import pandas as pd

column = ["Levski","CSKA","Botev"]
titled_columns = {"name": column,
                 "country": ["Bulgaria", "Bulgaria", "Bulgaria"]}
data = pd.DataFrame(titled_columns)

data.to_csv("club.csv",index=False, sep="\t")#pravi s tab razdelenieto
print(data)