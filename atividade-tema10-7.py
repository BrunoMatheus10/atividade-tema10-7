# Lista de valores
valores = [10.0, 20.0, 30.0, 40.0, 50.0]

# Inicializar variáveis para o menor número e seu índice
menor_num = valores[0]
indice_menor_num = 0

# Encontrar o menor número e sua posição (índice)
for i in range(len(valores)): 
    if valores[i] < menor_num:
        menor_num = valores[i]
        indice_menor_num = i

# Mostrar os valores em tela
print("O menor número dessa lista é", menor_num, "e está na posição (índice)", indice_menor_num)
