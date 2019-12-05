FROM alpine:3.9

RUN apk add --no-cache --progress python3 &&\
    rm -rf /var/cache/apk/* &&\
    mkdir /home/socket &&\
    cp ../socket/server.py /home/socket/

CMD ["tail", "-f", "/dev/null"]