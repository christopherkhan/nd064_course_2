from concurrent import futures
from datetime import datetime
from signal import signal, SIGTERM

import json
import grpc
import geolocation_pb2
import geolocation_pb2_grpc
from kafka import KafkaProducer


class LocationService(geolocation_pb2_grpc.LocationServiceServicer):
    def Ingest(self, request, context):

        payload = {
            "person_id": request.person_id,
            "latitude": request.latitude,
            "longitude": request.longitude,
            "creation_time": request.creation_time
        }     

        TOPIC_NAME = 'geolocations'
        KAFKA_SERVER = 'kafka:9092'

        # publish to kafka queue
        producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER,
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        producer.send(TOPIC_NAME, payload)
        producer.flush()
        return geolocation_pb2.LocationItem(**payload)

def run_server():
    # Initialize gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    geolocation_pb2_grpc.add_LocationServiceServicer_to_server(LocationService(), server)

    print("Server starting on port 5005...")
    server.add_insecure_port("[::]:5005")
    server.start()

    def handle_sigterm():
        all_rpcs_done_event = server.stop(30)
        all_rpcs_done_event.wait(30)

    signal(SIGTERM, handle_sigterm)
    server.wait_for_termination()


if __name__ == "__main__":
    run_server()
