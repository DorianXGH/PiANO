from flask import Flask
import time
import math

ON_RPI = False

if ON_RPI:

    import dht22
    import RPi.GPIO as GPIO

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    instance = dht22.DHT22(pin=5)

app = Flask(__name__)

@app.route("/metrics")
def metrics():
    dht22_data = ""
    if ON_RPI:
        result = instance.read()
        if result.is_valid():
            dht22_data = "piano_temperature " + str(result.temperature) + " piano_humidity "+ str(result.humidity)
    else:
        epoch_time = int(time.time())
        dht22_data = "piano_temperature " + str(math.sin(epoch_time*0.01)) + "\npiano_humidity "+ str(math.cos(epoch_time*0.01))
    

    return dht22_data, 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0')