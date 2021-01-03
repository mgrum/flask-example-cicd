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

</br>


## Simple instructions

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

If you want to use a python virtual environment you can run

```
python3 -m venv "venv"
source venv/bin/activate
````

With `deactivate` you can disable the virtual environment again

The script **reset-dev.sh** will do the following for you: 
* Delete virtual environment **venv**
* Create a new virtual environment **venv** without dependencies installed
* Activating **venv** if script is used from source
* Install **flake8** and **pytest** in created virtual environment
* Remove all folders created by build/install
    * package info (*egg-info)    
    * build folder
    * built cython files (*.so)
    * pycache folders

```
. reset-dev.sh
````

