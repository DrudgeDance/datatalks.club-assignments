FROM python:3.9.1

RUN apt-get update && apt-get install -y wget
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY load_data.py .

ENTRYPOINT [ "python", "load_data.py" ]