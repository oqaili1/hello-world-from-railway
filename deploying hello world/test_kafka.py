from kafka import KafkaProducer, KafkaConsumer

BOOTSTRAP = "centerbeam.proxy.rlwy.net:32605"

# Producer: send a test message
producer = KafkaProducer(bootstrap_servers=BOOTSTRAP)
producer.send("test-topic", b"Hello from a remote machine")
producer.flush()

print("Message sent.")

# Consumer: read it back
consumer = KafkaConsumer(
    "test-topic",
    bootstrap_servers=BOOTSTRAP,
    auto_offset_reset="earliest",
    consumer_timeout_ms=5000
)

for msg in consumer:
    print("Received:", msg.value.decode())