# Dockerfile for notification-service
FROM python:3.9-slim

WORKDIR /app

COPY notification-service.py /app/

RUN pip install flask

EXPOSE 5004

CMD ["python", "notification-service.py"]