FROM python:3.7.3

# install environment dependencies
RUN apt-get update -yqq\
    && apt-get install -yqq --no-install-recommends \
    netcat \
    && apt-get -q clean

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
COPY ./requirements.txt /usr/src/app

# install requirements
RUN pip install -r requirements.txt

# add entrypoint.sh
COPY ./api/entrypoint.sh /usr/src/app

COPY . /usr/src/app

ENTRYPOINT ["./entrypoint.sh"]
