import time

numero = int(input("Digite um número: "))

milhas = numero * 1.61 // 1
km = numero // 1.61

print(numero, "km em milhas:", milhas)
print(numero, "milhas em km:", km)

time.sleep(2)