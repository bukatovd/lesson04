FROM alpine:3.9

RUN set -xe && \
    apk add --no-cache --progress python3 wget curl &&\
    apk del build-dependencies &&\
    rm -rf /var/cache/apk/* &&\
    mkdir /home/socket &&\
    cp ../socket/server.py /home/socket/

CMD ["tail", "-f", "/dev/null"]