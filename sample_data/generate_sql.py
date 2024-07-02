import pandas as pd

df = pd.read_csv("wine-ratings-small.csv", index_col=0)
# Below is the sql template of inserting data into database
# The %s is the empty values which will be replace with real values from csv file
sql_tmpl = """INSERT INTO ratings(name, rating, region) VALUES("%s", "%s", "%s");\n"""
#create a sql file and the mode is append
sql_file = open("populate.sql", "a")

for _, row in df.iterrows(): #loop through index and values
    sql_file.write(sql_tmpl % (row['name'], row['rating'], row['region']))
    #print(row)
