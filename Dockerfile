FROM python:3.6

WORKDIR /app
COPY ./src/requirements.txt /app

RUN export PATH=/usr/lib/postgresql/X.Y/bin/:$PATH
RUN pip install --upgrade pip; pip install -r /app/requirements.txt



