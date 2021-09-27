# Simple gRPC Client Test function

import grpc
import json
from datetime import datetime
from geolocation_pb2_grpc import LocationServiceStub
from geolocation_pb2 import LocationItem

channel = grpc.insecure_channel("kafka-producer:5005")
client=LocationServiceStub(channel)

# create message
person_id = int(input("Enter Person ID: "))
latitude = input("Enter latitude: ")
longitude = input("Enter latitude: ")
current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')

geolocation_request = LocationItem(person_id=person_id, latitude=latitude, longitude=longitude,creation_time=current_time)
# make request; the post method will write this message into kakfa queue.
try:
    geolocation_response = client.Ingest(geolocation_request)
except grpc.RpcError as e:
    print(e.code())
else:
    print(geolocation_response)
    print(grpc.StatusCode.OK)
