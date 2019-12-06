FROM alpine:3.9

RUN apk add --update python py-pip &&\
    pip install Flask

COPY server.py /server.py

EXPOSE  8686

CMD ["python", "/server.py", "-p 8686"]