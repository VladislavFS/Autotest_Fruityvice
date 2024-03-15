FROM python:3.12-alpine
WORKDIR ./usr/lessons
COPY . .
RUN apk update && apk upgrade && apk add bash
RUN pip install -r requirements.txt
CMD python -m pytest -n4