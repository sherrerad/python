#def es_primo(numero):
def funcion_desconocida(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

#primos = []
valores_recogidos = []

for num in range(1, 11):
    #if es_primo(num):
    if funcion_desconocida(num):
        #primos.append(num)
        valores_recogidos.append(num)

#print(primos)
print(valores_recogidos)
print("javi cambio")
