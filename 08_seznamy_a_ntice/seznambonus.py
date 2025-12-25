# A nakonec projekt na přemýšlení.
# Zkus co nejjednodušeji udělat takový seznam, aby platilo:
# seznam[5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][0] == 5
# Může seznam obsahovat sám sebe?

seznam = [None]*10
seznam[0] = seznam
for _ in range(16):
    seznam = [seznam]*10
seznam[0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0] = 5
print(seznam[5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][0])  # vypíše 5      

# Ano, seznam může obsahovat sám sebe.
# V tomto případě jsme vytvořili seznam, 
# který obsahuje sám sebe na různých úrovních zanoření.
# Tento kód vytvoří seznam, který je zanořen do sebe 18krát, 
# a na nejhlubší úrovni nastaví hodnotu 5.
# Když pak přistoupíme k této hodnotě pomocí řetězce indexů, 
# získáme 5.
