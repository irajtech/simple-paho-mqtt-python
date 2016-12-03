import ssl
import paho.mqtt.client as paho

def on_message(clnt, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mqttc = paho.Client()
mqttc.on_message = on_message
#Using SSL/TLS connection
mqttc.username_pw_set("USERNAME", "PASSWORD")
#Setting - broker may not provide certificate to validate
mqttc.tls_set("path to broker certificate", cert_reqs=ssl.CERT_NONE)
#Setting - to avoid ssl.SSLError: ('Certificate subject does not match remote hostname.',)
mqttc.tls_insecure_set(True)
mqttc.connect("BROKER ADDRESS", 8883)
mqttc.subscribe("TOPIC NAME")
# Setting this stay connected
mqttc.loop_forever()
