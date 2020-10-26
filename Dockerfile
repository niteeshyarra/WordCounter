FROM python:3.9.0-buster

WORKDIR /home

COPY /home .

CMD ["python", "wordCounter.py"]

# FROM python:3

# ADD wordCounter.py /

# RUN pip install pystrich

# CMD [ "python", "./wordCounter.py" ]