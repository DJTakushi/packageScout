FROM ubuntu:18.04
COPY . /app
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-venv
RUN python3 -m pip install --upgrade build
RUN python3 -m pip install stdeb
RUN apt-get install -y vim
WORKDIR /app
CMD python3 packageScout.py
