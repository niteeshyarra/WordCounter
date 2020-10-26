FROM python:3.9.0-buster

WORKDIR /home

COPY /home .

CMD ["python", "wordCounter.py"]