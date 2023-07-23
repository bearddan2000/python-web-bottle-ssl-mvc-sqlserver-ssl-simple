FROM python:latest

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY bin/ /app

COPY cert /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "/app/app.py"]
