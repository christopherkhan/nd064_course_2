FROM python:3.7

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY /app /app
WORKDIR /app
EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]