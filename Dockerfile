FROM python:slim-buster

RUN pip install requests && \
    pip list

COPY ./*.py /app/
EXPOSE  8686

ENTRYPOINT [ "python3" ]
CMD [ "./app/server.py" ]