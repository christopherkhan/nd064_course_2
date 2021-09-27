FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

ENV  DB_USERNAME="ct_admin"
ENV  DB_NAME="geoconnections"
ENV  DB_HOST="postgres"
ENV  DB_PORT="5432"
ENV DB_PASSWORD="d293aW1zb3NlY3VyZQ=="

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]