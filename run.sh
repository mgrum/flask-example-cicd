# This script will run the flask app with given variables
# It is not used to start flask from the docker container - See Dockerfile
export FLASK_APP=flaskr.app
export FLASK_ENV=stage
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=8080
flask run