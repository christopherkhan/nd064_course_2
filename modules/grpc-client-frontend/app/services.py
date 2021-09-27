import grpc
import json
from datetime import datetime
from geolocation_pb2_grpc import LocationServiceStub
from geolocation_pb2 import LocationItem

def write_topic(payload):
    person_id = int(payload["person_id"])
    latitude = payload["latitude"]
    longitude = payload["longitude"]
    creation_time = payload["creation_time"]

    channel = grpc.insecure_channel("kafka-producer:5005")
    client=LocationServiceStub(channel)
    
    # current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
    # create message
    geolocation_request = LocationItem(person_id=person_id,latitude=latitude, longitude=longitude,creation_time=creation_time)
    
    # make request; this will post message to server.
    try:
        geolocation_response = client.Ingest(geolocation_request)
    except grpc.RpcError as e:
        return {"Status": e.code()}
    else:
        return {"Status": 201}