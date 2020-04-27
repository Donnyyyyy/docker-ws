FROM alpine

COPY . /app/

RUN python server.py
