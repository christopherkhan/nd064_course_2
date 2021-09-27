# How to Run UdaConnect

### Steps
1. Run the following commands to set up environment
    `kubectl apply -f deployment/db-configmap.yaml`
    `kubectl apply -f deployment/db-secret.yaml`
    `kubectl apply -f deployment/person-api.yaml`
            implements the Person API
    `kubectl apply -f deployment/location-api.yaml`
            implements the Location API    
    `kubectl apply -f deployment/postgres.yaml`
            set up Postgres database
    `kubectl apply -f deployment/udaconnect-app.yaml`
            set up the Udaconnect front end app
    `kubectl apply -f deployment/kafka.yaml`
            set up Kafka 
    `kubectl apply -f deployment/kafka-producer.yaml`
            set up Kafka producer . wil write location data to kafka
            implements grpc server
    `kubectl apply -f deployment/kafka-consumer.yaml`
            posts location data to Location API
    `kubectl apply -f deployment/grpc-client-frontend.yaml`
            grpc client for grpc server.
            Writes location data over grpc to grpc server


2. Seed the database against the `postgres` pod.
(`kubectl get pods` will provide the name assigned to the postgres pod `POD_NAME`)  
   `sh scripts/run_db_command.sh <POD_NAME>` 

Note: The first time you run this project, you will need to seed the database with dummy data. Use the command `sh scripts/run_db_command.sh <POD_NAME>` against the `postgres` pod. (`kubectl get pods` will give you the `POD_NAME`). Subsequent runs of `kubectl apply` for making changes to deployments or services shouldn't require you to seed the database again!

### Verifying it Works
Once the project is up and running, you should be able to see 8 deployments and 8 services in Kubernetes:
`kubectl get pods` and `kubectl get services` - should both return the following: 
    kafka
    kafka-producer
    kafka-consumer
    location-api
    person-api
    postgres
    udaconnect-app
    grpc-client-frontend
    zookeeper (required for kafka)

The following pages will load in browser
* `http://localhost:30000/` - Frontend ReactJS ApplicationThese pages should also load on your web browser:
* `http://localhost:30001/` - Base path for Person API
* `http://localhost:30002/` - Base path for Locations API


* `http://localhost:30008/` - Index page for grpc client. Provides details for testing grpc client


## NOTE
* You can access a running Docker container using `kubectl exec -it <pod_id> sh`. 
