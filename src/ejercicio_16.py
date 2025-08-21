import time

minutos = 0
segundos = 0

while minutos < 1:
    while segundos < 60:
        print(f"0{minutos:01d}:{segundos:02d}")
        time.sleep(1)
        segundos += 1
    minutos += 1
    segundos = 0

print("Reloj finalizado.")