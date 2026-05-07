import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt

datos = []
tiempos = []
contador = [0]

def on_message(cliente, userdata, mensaje):
    temperatura = float(mensaje.payload)
    datos.append(temperatura)
    tiempos.append(contador[0])
    contador[0] += 1
    print(f"Recibido: {temperatura}")

cliente = mqtt.Client()
cliente.on_message = on_message
cliente.connect("localhost", 1883)
cliente.subscribe("sensor/temperatura")
cliente.loop_start()

input("Presioná Enter cuando termines de recibir datos...\n")

cliente.loop_stop()
cliente.disconnect()

plt.plot(tiempos, datos)
plt.axhline(y=30, color="green", linestyle="--", label="Límite de alerta")
plt.legend()
plt.title("Temperatura del sensor - MQTT")
plt.xlabel("Tiempo (s)")
plt.ylabel("Temperatura (°C)")
plt.show()
