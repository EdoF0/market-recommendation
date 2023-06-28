lista_colonne = []
file1 = open('categories1.txt', 'r')

lines = file1.readlines()
for line in lines:
    lista_colonne.append(line.strip())
    
lista_query_no_aggiustamento_no_filtro = []
lista_query_no_aggiustamento_filtro = []
lista_query_aggiustamento_no_filtro = []
lista_query_aggiustamento_filtro = []

for colonna in lista_colonne:
    lista_query_no_aggiustamento_no_filtro.append(f"select avg({colonna}) as media from market.market;{colonna};{colonna}")
    for colonna2 in lista_colonne:
        if (colonna != colonna2):
            lista_query_no_aggiustamento_filtro.append(f"select avg({colonna}) as media from market.market where {colonna2} > 60 allow filtering;{colonna};{colonna2}")
            lista_query_aggiustamento_no_filtro.append(f"select avg(market.proportion100({colonna},{colonna2},sum_categories1)) as media from market.market;{colonna};{colonna2}")
            lista_query_aggiustamento_filtro.append(f"select avg(market.proportion100({colonna},{colonna2},sum_categories1)) as media from market.market where {colonna2} > 60 allow filtering;{colonna};{colonna2}")

with open('listaQuerySQL.txt', 'w') as file:
    for i in lista_query_aggiustamento_no_filtro:
        file.write(i)