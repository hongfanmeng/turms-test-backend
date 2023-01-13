FROM python:3.11-alpine

WORKDIR /code
COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/
EXPOSE 80

CMD gunicorn turms_test.wsgi --bind 0.0.0.0:80 --workers 4