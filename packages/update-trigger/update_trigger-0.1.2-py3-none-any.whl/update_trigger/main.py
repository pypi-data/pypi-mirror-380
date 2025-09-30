import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv

load_dotenv('../.env')


class MqttService:
    def __init__(self, broker: str, port: int, topic: str, client_id: str):
        self._broker = broker
        self._port = port
        self._topic = topic
        self._client_id = client_id

        self._client = mqtt.Client(
            callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
            userdata=None,
            protocol=mqtt.MQTTv5
        )
        self._client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
        self._client.username_pw_set(
            username=os.environ["MQTT_USERNAME"],
            password=os.environ["MQTT_PASSWORD"]
        )
        self._client.connect(
            host=self._broker,
            port=self._port,
            keepalive=60
        )
        self._client.loop_start()

    def send_message(self):
        try:
            result = self._client.publish(
                topic=self._topic,
                payload="update",
                qos=1
            )
            result.wait_for_publish(5)
            status = result.is_published()
            if status:
                print("Message sent!")
            else:
                print(f"Error sending message: {result}")
        except Exception as e:
            print(f"Erro: {e}")
        finally:
            self._client.loop_stop()
            self._client.disconnect()


def main():
    service = MqttService(
        broker=os.environ["MQTT_BROKER"],
        port=int(os.environ["MQTT_PORT"]),
        client_id='',
        topic='actions',
    )
    service.send_message()


if __name__ == '__main__':
    main()
