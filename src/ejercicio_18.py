a, b = 1, 1

print("Secuencia de Fibonacci:")
print(a)
print(b)

while b <= 1000:
    siguiente_numero = a + b
    print(siguiente_numero)
    a = b
    b = siguiente_numero