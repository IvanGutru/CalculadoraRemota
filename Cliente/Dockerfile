FROM ubuntu:20.04
WORKDIR /Cliente
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
EXPOSE 8080
CMD [ "python3","ClienteCalculadora.py" ]