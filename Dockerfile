FROM python:3.8.10

WORKDIR /app

COPY scripts/* /app/
RUN pip install git+https://github.com/SeraphimSerapis/libpyvss.git@master

