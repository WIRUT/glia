# Python base image
FROM python:3.9-slim-bullseye

# set working directory as app
WORKDIR /app

# copy requirements.txt file from local (source) to file structure of container (destination)
COPY requirements.txt requirements.txt

# install the python requirements
RUN pip3 install -r requirements.txt

# copy all items in current local directory (source) to current container directory (destination)
COPY . .

# command to start FastApi server
CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080" ]