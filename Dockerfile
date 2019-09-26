FROM python:3-alpine
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install -r requirements.txt
COPY . .
CMD [ "python", "pipenv run soup.py" ]
