FROM debian:bookworm

RUN apt update

RUN apt install python3 python3-flask python3-psutil -y

RUN mkdir /webapp

WORKDIR /webapp

COPY Python/main.py ./

EXPOSE 5000

ENTRYPOINT ["python3","./main.py"]

