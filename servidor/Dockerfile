FROM ubuntu:20.04
WORKDIR /servidor
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN python3 -m pip install thrift
EXPOSE 8080
CMD [ "python3","ServidorCalculadora.py" ]


