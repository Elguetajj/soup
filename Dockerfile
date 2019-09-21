FROM python:3-alpine
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pipenv install -r requirements.txt
COPY . .
