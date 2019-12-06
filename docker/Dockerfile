FROM alpine

RUN apk add --update python3 

COPY server.py /server.py

EXPOSE  8686

CMD ["python3", "/server.py", "-p 8686"]