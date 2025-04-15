import logging
import os

from flask import Flask
import paho.mqtt.client as mqtt
log = logging.getLogger()

mqtt_url = os.environ['MQTT_URL']
mqtt_port = int(os.environ['MQTT_PORT'])
app = Flask(__name__)

@app.route('/open', methods=['GET'])
def ping():
    send_message()
    return '', 200

def send_message():
    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="http_gate", protocol=mqtt.MQTTv5)

    mqttc.connect(mqtt_url, mqtt_port)
    mqttc.loop_start()
    msg_info = mqttc.publish("door/state", "1", qos=0)
    log.info(f"Message is sent: {msg_info}")
    mqttc.disconnect()
    mqttc.loop_stop()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
