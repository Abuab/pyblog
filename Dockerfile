# syntax=docker/dockerfile:1

FROM python:3.6-slim-buster
MAINTAINER kevin
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN sed -i 's/flask\.\_compat/flask_script\.\_compat/' /usr/local/lib/python3.6/site-packages/flask_script/__init__.py
EXPOSE 8003
CMD ["python", "manage.py", "db", "init"]
CMD ["python", "manage.py", "db", "migrate"]
CMD ["python", "manage.py", "db", "upgrade"]
CMD ["python", "manage.py", "runserver", "-p", "8003", "-h", "0.0.0.0", "-d", "-r", "--threaded"]
