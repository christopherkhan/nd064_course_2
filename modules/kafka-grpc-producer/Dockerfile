FROM python

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY /app /app
WORKDIR /app
EXPOSE 5005

CMD ["python", "app.py"]