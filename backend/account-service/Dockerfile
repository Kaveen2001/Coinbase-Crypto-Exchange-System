# Dockerfile for account-service
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy  into the container
COPY account_service.py /app/

# Install the dependencies specified in requirements.txt
RUN pip install flask

# Expose the port that the app will run on
EXPOSE 5001

# Command to run the application
CMD ["python", "account_service.py"]