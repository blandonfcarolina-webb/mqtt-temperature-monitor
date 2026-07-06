## MQTT Temperature Monitor

Simulated IoT temperature monitoring system using MQTT for data transmission
and Matplotlib for real-time visualization. Built with Python and Mosquitto broker.

---

## Overview

This project simulates a basic IoT data pipeline in which a sensor publishes
temperature readings over MQTT, and a subscriber receives, displays, and
visualizes the data in real time. It demonstrates the publisher/subscriber
pattern commonly used in IoT and industrial monitoring systems.

---

## System Architecture
[publisher.py] --> MQTT Broker (Mosquitto) --> [suscriptor.py]
Simulates sensor                               Receives & plots data
Publishes to: sensor/temperatura               Displays alert threshold

---

## Technologies Used

- **Python 3.x** — core logic for publishing and subscribing
- **paho-mqtt** — MQTT client library for Python
- **Matplotlib** — real-time data visualization
- **Mosquitto** — local MQTT broker

---

## Requirements

- Python 3.6 or higher
- Mosquitto broker installed and running locally on port 1883
- Python dependencies:

```bash
pip install paho-mqtt matplotlib
```

---

## Project Structure

| File | Role |
|------|------|
| `publisher.py` | Simulates a temperature sensor — generates random values and publishes them to the MQTT broker |
| `suscriptor.py` | Subscribes to the MQTT topic, receives temperature data, and plots it with an alert threshold line |
| `monitor_temp.py` | Standalone monitoring script — runs publisher and subscriber logic independently |

---

## How It Works

### publisher.py
Connects to the local Mosquitto broker and publishes 20 simulated temperature
readings (ranging from 15.0°C to 35.0°C) to the topic `sensor/temperatura`,
one per second:

```python
for i in range(20):
    temperatura = round(random.uniform(15.0, 35.0), 2)
    cliente.publish("sensor/temperatura", temperatura)
    time.sleep(1)
```

### suscriptor.py
Subscribes to `sensor/temperatura` and processes each incoming message through
the `on_message` callback, which appends the value and a time counter to lists
for plotting:

```python
def on_message(cliente, userdata, mensaje):
    temperatura = float(mensaje.payload)
    datos.append(temperatura)
    tiempos.append(contador[0])
    contador[0] += 1
```

After the session ends (user presses Enter), it generates a Matplotlib chart
showing temperature over time with a dashed green alert threshold at 30°C:

```python
plt.axhline(y=30, color="green", linestyle="--", label="Límite de alerta")
```

---

## How to Run

1. Start the Mosquitto broker:
```bash
mosquitto
```

2. In a first terminal, start the subscriber:
```bash
python suscriptor.py
```

3. In a second terminal, run the publisher:
```bash
python publisher.py
```

4. Press **Enter** in the subscriber terminal when done — a temperature chart
will appear with the alert threshold line.

---

## Sample Output

The subscriber terminal prints each received value:

Recibido: 27.43
Recibido: 31.08
Recibido: 19.75
...

The Matplotlib chart displays temperature readings over time, with a dashed
green line marking the 30°C alert threshold.

---

## Author

Carolina Blandon Falcon  
[linkedin.com/in/c-blandon98](https://linkedin.com/in/c-blandon98)
