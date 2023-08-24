FROM python:3.11-slim

WORKDIR /api

COPY . /api

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python3", "app.py"]