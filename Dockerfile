FROM bukatovd/python:1

COPY ./server.py /app/
EXPOSE  8686

ENTRYPOINT [ "python3" ]
CMD [ "./app/server.py" ]

