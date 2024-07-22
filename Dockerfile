FROM python:3.12-slim

RUN mkdir /event_parser

WORKDIR /event_parser

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]