
# pull official base image
FROM python:3.8.0-alpine
# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /music_service

# Set the working directory to /music_service
WORKDIR /music_service

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1

# add current dir to the container dir
ADD . /music_service/

## install dependencies

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/music_service/requirements.txt

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install -r requirements.txt

# copy project from current dir to docker dir
COPY . /music_service/
