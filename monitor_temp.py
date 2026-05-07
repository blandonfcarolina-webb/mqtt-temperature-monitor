import matplotlib.pyplot as plt
import random

datos = []
tiempos = []

for i in range(50):
    temperatura = round(random.uniform(15.0, 35.0), 2)
    datos.append(temperatura)
    tiempos.append(i*5)

plt.plot(tiempos, datos)
plt.axhline(y = 30, color = "green", linestyle = "--", label = "Límite de alerta")
plt.title("Temperatura del sensor")
plt.xlabel("Tiempo (s)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.show()
