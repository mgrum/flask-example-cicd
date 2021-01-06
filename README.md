# flask-example-cicd

This is a simple python flask application to host a simple web app.

After starting the flask application you can access following URL's on the server:
| Function        | URL                                     |
|-----------------|-----------------------------------------|
| index           | `http://<server>:<port>/`               |
| hello           | `http://<server>:<port>/hello/`         |
| hello \<name>   | `http://<server>:<port>/hello/<name>`   |
| primes 100      | `http://<server>:<port>/primes/`        |
| primes \<count> | `http://<server>:<port>/primes/<count>` |

## Requirements

* python3
* python3-dev
* **Optional**: python3-venv

```
# example install for ubuntu
sudo apt-get update
sudo apt-get install python3 python3-dev python3-venv
```

## Simple instructions (Linux or WSL)

To **build/install** the flask application use

``` 
. build.sh
````

After that you can **run** the server on port **:8080** with

```
. run.sh
````

To test the application use

```shell
# install flake8 and pytest manually or use "reset-dev.sh"
pip install flake8 pytest 
pytest
````

## Docker instructions

Build the docker image in the project root folder with

```docker
docker build . -t flask-example:latest
```

To **run** the docker image in **interactive mode**

```docker
docker run --rm -it -p 8080:8080/tcp --name flask-example flask-example:latest
```

To **run** the docker image in **detached mode**

```docker
docker run --rm -d -p 8080:8080/tcp --name flask-example flask-example:latest
```

You can change the environmental variable for **flask** in the **Dockerfile**, for example you can change the port by changing `ENV FLASK_RUN_PORT=8080`

To stop the container use

```docker
docker stop flask-example
```


## Development instructions

You can debug the flask app with

```
python3 -m flask.app
```

### Virtual Environment

For local development you can use a [virtual environment](https://docs.python.org/3/tutorial/venv.html).

[How to install virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b). 

```
python3 -m venv "venv"
source venv/bin/activate
````

With `deactivate` you can disable the virtual environment again

### reset-dev.sh

You can also use the script **reset-dev.sh** to (re)create a virtual environment **venv** and also clean up build-files.

```
. reset-dev.sh
````

The script **reset-dev.sh** will do the following for you: 
* Delete virtual environment **venv**
* Create a new virtual environment **venv** without dependencies installed
* Activating **venv** if script is used from source
* Install development/testing tools in **venv**
    * flake8 (Linting)
    * pylint (Linting)
    * autopep8 (Formatting)
    * pytest (Testing)
* Remove all folders created by build/install
    * package info (*egg-info)    
    * build folder
    * dist folder
    * pycache folders
    * built cython files (*.so)
