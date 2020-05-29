FROM python:3.7

RUN pip install django

ADD ./ /app

WORKDIR /app

CMD python ../manage.py runserver 0:8000