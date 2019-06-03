FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip3 install -r requirements.txt
ADD . /app/
CMD python /app/fontes/manage.py makemigrations blog
