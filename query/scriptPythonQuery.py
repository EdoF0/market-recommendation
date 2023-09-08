lista_colonne = []
file1 = open('categories1.txt', 'r')

lines = file1.readlines()
for line in lines:
    lista_colonne.append(line.strip())
    
lista_query_user_interest = []

for given in lista_colonne:
    for target in lista_colonne:
        if (given != target):
            lista_query_user_interest.append(f"select market.interest(AVG(market.userinterest({given},{target},sum_categories1)), SUM(market.weight({given},sum_categories1))) as interest_{given}_{target} from market.market;{given};{target}")       



with open('listaQuerySQL.txt', 'w') as file:
    for i in lista_query_user_interest:
        file.write(i+'\n')


def divide_file(input_file, output_prefix, lines_per_file=48):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    total_lines = len(lines)

    for i in range(0, total_lines, lines_per_file):
        chunk = lines[i:i + lines_per_file]
        output_file = f"{output_prefix}_{i // lines_per_file + 1}.txt"

        with open(output_file, 'w') as outfile:
            outfile.writelines(chunk)

if __name__ == "__main__":
    input_file = "listaQuerySQL.txt"
    output_prefix = "gruppoQuery"
    lines_per_file = 48
    divide_file(input_file, output_prefix, lines_per_file)