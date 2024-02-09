"""
Gets the random user API data and writes the data to a Kafka topic every 10 seconds
"""
import requests
import json
import time
from kafka import KafkaProducer
import logging

logging.basicConfig(level=logging.INFO)


class StreamKafka:
    def __init__(self, api_url: str) -> None:
        self.api_url = api_url

        self.set_producer()
        logging.info("Defined Producer and set URl")

    def set_producer(self):
        self.producer = KafkaProducer(bootstrap_servers=["localhost:9092"])

    def start(self):
        while True:
            resp = requests.get(self.api_url)
            data = resp.json()

            # Adding stream published timestamp which can be used later to track latency
            data["kafka_created_at"] = time.time_ns()

            logging.info(f"Response : {data}")
            self.producer.send("crypto", json.dumps(data).encode("utf-8"))
            time.sleep(2)


# def get_response(url: str = "https://api.coindesk.com/v1/bpi/currentprice.json")


if __name__ == "__main__":
    logging.info("Initiating Stream")
    """
    Find list of some free apis at: https://apipheny.io/free-api/#apis-without-key
    """
    stream = StreamKafka(api_url="https://api.coindesk.com/v1/bpi/currentprice.json")
    stream.start()
