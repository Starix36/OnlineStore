FROM python:3.9-slim

WORKDIR /app

# Copy the application code into the container
COPY . .

RUN pip install pandas

# Command to run the revenue analysis script
CMD ["python", "revenue_analyser.py"]
