import paho.mqtt.client as mqtt
import time


class Client:
    __ces = "\x1b[39;49m"  # Color ending sequence
    __prefix = "\x1b[39;49m" + "[MQTT]" + __ces
    __status_ok = "\033[1;39;49m[" + "\033[1;32;49m OK" + "\033[1;39;49m ]" + __ces
    __status_nok = "\033[1;39;49m[" + "\033[1;31;49m NOK" + "\033[1;39;49m ]" + __ces
    def __init__(self, host, port, topic, client_id, user, password, sample_period = 15, keepalive_interval=60, verbose=False):
        """Simple framework to overlay paho's mqtt client package"""
        self.host = host
        self.port = int(port)
        self.topic = f"channels/{topic}/publish"
        self.client_id = client_id
        self.user = user
        self.password = password
        self.sample_period = sample_period
        self.keepalive_interval = keepalive_interval

        self.verbose = verbose

        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, self.client_id)
        self.client.username_pw_set(self.user, self.password)

        self.client.on_connect = self.__on_connect
        self.client.on_disconnect = self.__on_disconnect
        self.client.on_message = self.__on_message

        self.client.enable_logger()

        print(f"{self.__prefix} Attempting to connect to \033[33;49m" + f"{self.host}:{self.port}" + self.__ces)

        self.client.connect(self.host, self.port)
        self.client.loop_start()

    def get_paho_client(self):
        return self.client

    def send(self, fields, qos=0, retain=False, properties=None):
        """Send message to predefined client"""
        if not isinstance(fields, list):
            print(f"{self.__prefix} \033[31;49m" + f"ERROR: parameter fields must be a list!" + self.__ces)
            raise TypeError(fields)

        if (len(fields) < 1):
            print(f"{self.__prefix} \033[31;49m" + f"ERROR: parameter fields can't be empty!" + self.__ces)
            raise SyntaxError(fields)

        field_partition = ""

        if (self.verbose):
            verbose_value = ""

        for field_index in range(len(fields)):

            field_value = str(fields[field_index])
            field_number = field_index + 1

            if field_index > 0:
                field_partition += "&"

            field_partition += f"field{field_number}={field_value}"
            if (self.verbose):
                verbose_value += f"- Field {field_number}: \x1b[33;49m{field_value} {self.__ces}\n"

        self.data = field_partition + "&status=MQTTPUBLISH"
        print(f"{self.__prefix} \033[36;49m" + f"DATA: {self.data}" + self.__ces)

        if (self.verbose):
            print(verbose_value)

        try:
            self.client.publish(
                topic=self.topic,
                payload=self.data,
                qos=qos,
                retain=retain,
                properties=properties
            )

            time.sleep(self.sample_period)

        except OSError:
            self.client.reconnect()

    def __on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(f"{self.__prefix} Connection status {self.__status_ok} with result code: \033[33;49m" + str(rc) + self.__ces)
        else:
            print(f"{self.__prefix} Connection status {self.__status_nok} with result code: \033[33;49m" + str(rc) + self.__ces)

    def __on_disconnect(self, client, userdata, flags, rc=0):
        print(f"{self.__prefix} Disconnected with result code: \033[33;49m" + str(rc) + self.__ces)

    def __on_message(self, client, userdata, msg):
        print(f"{self.__prefix} Received a message on topic: \033[33;49m" + msg.topic + "\033[39;49m | message: \033[33;49m" + msg.payload + self.__ces)
