
FROM python:3.9

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip3 install -r requirements.txt

ENV PATH_PREFIX=""
ENV SECRET_KEY=""
ENV DATABASE_NAME=""
ENV DATABASE_USER=""
ENV DATABASE_PASSWORD=""
ENV DATABASE_HOST=""
ENV DATABASE_PORT=3306

RUN mkdir /app
ADD run.sh /app
WORKDIR /app
RUN chmod +x run.sh

RUN useradd noRoot -s /bin/bash

RUN chown -R noRoot /code
RUN chmod -R 500 /code 
RUN chown -R noRoot /app

USER noRoot
WORKDIR /code

CMD /bin/bash -c '/app/run.sh'
