FROM python:3.12.4-alpine3.20

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN mkdir logs

CMD ["python", "app/main.py"]
