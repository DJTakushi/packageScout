FROM ubuntu:18.04
COPY . /app
RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y vim
WORKDIR /app
CMD python3 packageScout.py
