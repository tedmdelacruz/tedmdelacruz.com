FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD app /code/

RUN pip install -r /code/requirements.txt
RUN apt-get update && apt-get install -y netcat

