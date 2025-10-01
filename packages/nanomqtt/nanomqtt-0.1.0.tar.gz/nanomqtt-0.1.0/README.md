# NanoMQTT
A lightweight wrapper around Paho MQTT client

## Install
```bash
pip install nanomqtt
```

## Example usage - Thingspeak

```python
import random

from nanomqtt import Client

client = Client(
    host="mqtt3.thingspeak.com",
    port=1883,
    topic="<topicid>", # channel
    client_id="<clientid>",
    user="<userid>",
    password="<password>",
    verbose=True, # send messages?
    sample_period=1 # delay between messages (in seconds)

)

while True:
    client.send(fields=[random.randint(0,1)]) # send a random integer between 0 and 1 to the channel in field 1
```