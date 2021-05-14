from prometheus_api_client import PrometheusConnect
import time
prom = PrometheusConnect(url ="http://localhost:9090", disable_ssl=True)


while True:
    a = prom.custom_query(query="piano_humidity[1m]")
    hum = a[0]["values"]
    s = 0
    for h in hum:
        s += float(h[1])
    meanhum = s/len(hum)

    b = prom.custom_query(query="piano_temperature[1m]")
    temp = a[0]["values"]
    s = 0
    for t in temp:
        s += float(t[1])
    meantemp = s/len(temp)

    if (meanhum > 0.7) or (meanhum < -0.7) or (meantemp > 0.7) or (meantemp < -0.7):
        print("Abnormal conditions")
    else:
        print("OK")
    time.sleep(30)