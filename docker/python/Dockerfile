FROM python:3.7-alpine

RUN apk update && apk add --no-cache --virtual bash gcc musl-dev linux-headers jpeg-dev zlib-dev mariadb-dev libffi-dev
RUN ls
RUN chmod +x manage.py

# install pypi packages
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN rm /usr/bin/mysql*
COPY uwsgi.ini /uwsgi.ini
RUN pip freeze > newreqs.txt

CMD ["uwsgi", "--ini", "/uwsgi.ini"]
