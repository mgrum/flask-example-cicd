FROM python:alpine
WORKDIR /code
COPY . .
COPY requirements.txt requirements.txt
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
RUN pip install -r requirements.txt
RUN pip install -e .
ENV FLASK_APP=flaskr.app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080
EXPOSE 8080
CMD ["flask","run"]