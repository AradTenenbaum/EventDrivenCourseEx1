FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY *.py .

RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["python", "order_service.py"]
