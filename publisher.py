import paho.mqtt.client as mqtt
import random
import time

cliente = mqtt.Client()
cliente.connect("localhost", 1883)

for i in range(20):
    temperatura = round(random.uniform(15.0, 35.0), 2)
    cliente.publish("sensor/temperatura", temperatura)
    print(f"Enviado: {temperatura}")
    time.sleep(1)

cliente.disconnect()
