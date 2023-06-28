from cassandra.cluster import Cluster,ExecutionProfile, EXEC_PROFILE_DEFAULT
from cassandra.auth import PlainTextAuthProvider
import csv

ip_address = '2.36.116.197'
username = 'cassandra'
password = 'cassandra'

auth_provider = PlainTextAuthProvider(username=username, password=password)

profile = ExecutionProfile(
    request_timeout=9999000
)

cluster = Cluster(['2.36.116.197'], port=9042, auth_provider=auth_provider, execution_profiles={EXEC_PROFILE_DEFAULT: profile}, control_connection_timeout= None)
session = cluster.connect()

#print(session.execute("SELECT * FROM market.market limit 1").one())

#LEGGERE RIGHE contenente ogni riga una sql da cui formerà la matrice e poi lo salverà su un CSV
rows = [] # lista che dovro leggere a ogni riga delle select

file = open('file.csv', 'a')
# \   col1 col2 col3 ..
#col1 2    3    4 
#col2 5    6    7
#col2 8    9    10 

# colInteresse colStimare interesse valore
# col1         col2        5
#

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
#writer.writerow(["colInteresse", "colStimare", "interesse Valore"])

queryExample = "select avg(categories1_artandentertainment) as media from market.market where categories1_automotive > 90 allow filtering;categories1_artandentertainment;categories1_automotive"

riga_splittata = queryExample.strip().split(";")
# query = riga_splittata[0] + ";"
# var1 = riga_splittata[1]
# var2 = riga_splittata[2]

# print(query)
# query = session.execute(query).one()
# valore = query.media
# writer.writerow([var1, var2 ,valore])


with open('listaQueryAggiustamentoFiltro.txt', "r") as f:
    for line in f.readlines():
        riga_splittata = line.strip().split(";")
        query = riga_splittata[0] + ";"
        var1 = riga_splittata[1]
        var2 = riga_splittata[2]

        print(query)
        query = session.execute(query).one()
        valore = query.media
        writer.writerow([var1, var2 ,valore])

file.close()