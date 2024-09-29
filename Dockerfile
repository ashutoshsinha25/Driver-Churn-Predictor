FROM python:3.9-slim-buster

WORKDIR /flask-docker

RUN apt-get update && \
    apt-get install -y libgomp1 && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . . 

ENV FLASK_RUN_PORT=8000
EXPOSE 8000

CMD ["python", "-m", "flask", "--app", "main.py",  "run", "--host=0.0.0.0"]