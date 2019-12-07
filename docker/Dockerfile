FROM amd64/python:3

RUN pipenv install requests

COPY server.py /app
EXPOSE  8686

ENTRYPOINT [ "python" ]
CMD [ "./app/server.py" ]

