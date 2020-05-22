FROM ubuntu:20.04

WORKDIR /Servidor
RUN apt-get update
RUN apt-get install -y ruby-thrift
EXPOSE 8080
CMD [ "ruby","Servidor.rb" ]