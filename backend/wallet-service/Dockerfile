# Dockerfile for wallet-service
FROM python:3.9-slim

WORKDIR /app

COPY wallet-service.py /app/

RUN pip install flask

EXPOSE 5003

CMD ["python", "wallet-service.py"]