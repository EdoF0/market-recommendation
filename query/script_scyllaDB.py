from cassandra.cluster import Cluster
import csv

cluster = Cluster(['indirizzo_IP'], port=9042, auth_provider={'username': 'nome_utente', 'password': 'password'})
session = cluster.connect()

print(session.execute("SELECT * FROM tabella limit 1").one())

#LEGGERE RIGHE contenente ogni riga una sql da cui formerà la matrice e poi lo salverà su un CSV
rows = [] # lista che dovro leggere a ogni riga delle select

file = open('file.csv', 'w')

header = [
    "categories1_artandentertainment",
    "categories1_automotive",
    "categories1_business",
    "categories1_careers",
    "categories1_education",
    "categories1_emotions",
    "categories1_famigliaegenitorialita",
    "categories1_famigliaegenitorialitaother",
    "categories1_familyandparenting",
    "categories1_finance",
    "categories1_foodanddrink",
    "categories1_healthandfitness",
    "categories1_hobbiesandinterests",
    "categories1_homeandgarden",
    "categories1_intentions",
    "categories1_lavoro",
    "categories1_lawgovtandpolitics",
    "categories1_news",
    "categories1_pets",
    "categories1_realestate",
    "categories1_religionandspirituality",
    "categories1_science",
    "categories1_sentiment",
    "categories1_shopping",
    "categories1_societa",
    "categories1_society",
    "categories1_sports",
    "categories1_styleandfashion",
    "categories1_technologyandcomputing",
    "categories1_travel",
    "categories1_uncategorized"
] #header csv

writer = csv.writer(file)
writer.writerow(header)

matrix = {}

list_length = len(header)

for key in header:
    matrix[key] = [None] * list_length

with open('filename.txt', "r") as f:
    for line in f.readlines():
        riga_splittata = line.strip().split(";")
        query = riga_splittata[0]
        var1 = riga_splittata[1]
        var2 = riga_splittata[2]

        query = session.execute(query).one()
        valore = query.media
        print(valore + " ")

        matrix[var1][header.index(var2)] = valore
        #writer.writerow(data)

count = 0
for key in matrix:
    list_values = matrix[key]
    header.insert(0, ' ')

    list_values.insert(0, header[count])
    writer.writerow(list_values)
    print(f"Key: {key}, List Values: {list_values}")
    count = count +1 

file.close()