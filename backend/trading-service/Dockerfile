# Dockerfile for trading-service
FROM python:3.9-slim

WORKDIR /app

COPY trading-service.py /app/

RUN pip install flask

EXPOSE 5002

CMD ["python", "trading-service.py"]