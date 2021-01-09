FROM python:3.9-alpine
WORKDIR /code
COPY . .
COPY requirements.txt requirements.txt
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install -r requirements.txt \
    && pip install -e . \
    && apk del .build-deps
ENV FLASK_APP=flaskr.app
ENV FLASK_ENV=stage
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080
EXPOSE 8080
CMD ["flask","run"]