FROM python:3.9

RUN mkdir -p /opt/geopedia
WORKDIR /opt/geopedia

RUN apt-get update
RUN apt-get install zlib1g-dev -y

ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

ADD ./ /opt/geopedia/

EXPOSE 8000
