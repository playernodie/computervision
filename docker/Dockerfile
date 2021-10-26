
# docker build -t pythonforai .
FROM python:3.7.0

COPY requirements.txt /tmp/requirements.txt
WORKDIR /tmp/

RUN pip3 install -r requirements.txt
RUN jupyter serverextension enable --py jupyter_http_over_ws
RUN apt install git 