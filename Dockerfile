FROM python:3.10-alpine3.15

RUN apk update && apk add tzdata
ENV TZ=Europe/London

COPY ./ip_checker .
COPY example.json ip_data.json
COPY ./crontab .
COPY ./requirements.txt .

RUN pip install -r requirements.txt

RUN crontab crontab

CMD ["crond", "-f"]
