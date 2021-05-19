FROM ubuntu:18.04

RUN apt update && apt install curl -y

WORKDIR /usr/src

COPY input.sh .

CMD ./input.sh