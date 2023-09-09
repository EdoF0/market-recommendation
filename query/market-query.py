from cassandra.cluster import Cluster,ExecutionProfile, EXEC_PROFILE_DEFAULT
from cassandra.auth import PlainTextAuthProvider
import csv
import sys

ip_address = '127.0.0.1'
username = 'cassandra'
password = 'cassandra'

auth_provider = PlainTextAuthProvider(username=username, password=password)

profile = ExecutionProfile(
    request_timeout=9999000
)

cluster = Cluster([ip_address], port=9042, auth_provider=auth_provider, execution_profiles={EXEC_PROFILE_DEFAULT: profile}, control_connection_timeout= None)
session = cluster.connect()

rows = []

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

parametro1 = sys.argv[1]
parametro2 = sys.argv[2]

# open with empty string newline to not write two newlines with csv.writer
# https://stackoverflow.com/questions/3191528/csv-in-python-adding-an-extra-carriage-return-on-windows
file = open(parametro1, 'a', newline='')

writer = csv.writer(file, delimiter=";")

with open(parametro2, "r") as f:
    i=1
    for line in f.readlines():
        print("[" + str(i) + "]")

        riga_splittata = line.strip().split(";")
        query = riga_splittata[0] + ";"
        var1 = riga_splittata[1]
        var2 = riga_splittata[2]

        print("  " + query)
        valore = session.execute(query).one()[0]
        writer.writerow([var1, var2, valore, query[:-1]])
        file.flush()

        print("  -> " + str(valore))
        i += 1;

file.close()
