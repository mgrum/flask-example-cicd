# flask-example-cicd

This is a simple python flask application to host a simple web app.

After starting the flask application you can access following URL's on the server:

| Function        | URL                                     |
|-----------------|-----------------------------------------|
| index           | `http://<server>:<port>/`               |
| json            | `http://<server>:<port>/json/`          |
| hello           | `http://<server>:<port>/hello/`         |
| hello \<name>   | `http://<server>:<port>/hello/<name>`   |
| primes 100      | `http://<server>:<port>/primes/`        |
| primes \<count> | `http://<server>:<port>/primes/<count>` |

## How to run

You can run the application in 2 ways:

* [Build and run the **docker** image](#docker-instructions)
* [Build and run the code from **source**](#build-from-source)

# Docker instructions

Requirements:
* [Docker](https://docs.docker.com/desktop/) installed

Build the docker image in the project root folder with:

```docker
docker build . -t flask-example-cicd:latest
```

To **run** the docker image in **interactive mode**:

```docker
docker run --rm -it -p 8080:8080/tcp --name flask-example flask-example-cicd:latest
```

To **run** the docker image in **detached mode**:

```docker
docker run --rm -d -p 8080:8080/tcp --name flask-example flask-example-cicd:latest
```

You can change the environmental variable for **flask** in the [Dockerfile](Dockerfile), for example you can change the port by changing `ENV FLASK_RUN_PORT=8080`.

Stop the running container:

```docker
docker stop flask-example
```

# Build from source

Requirements:
* python3
* python3-dev
* python3-pip
* gcc (to compile cython)
* musl-dev (to compile cython)

## Instructions for Debian/Ubuntu

1. Install requirements:

```bash
apt update
apt install gcc musl-dev python3 python3-dev python3-pip
```
2. Build/Install project:

```bash
. build.sh
```

3. Run the server on **localhost:8080**:

```bash
. run.sh
```

# Development

## Virtual Environment

For local development you can use a [virtual environment](https://docs.python.org/3/tutorial/venv.html) → [How to install virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b). 

Create a virtual environment:

```bash
# linux example
python3 -m venv "venv"
source venv/bin/activate
````

With `deactivate` you can disable the virtual environment.

## Debugging

### Built-In flask debugger
You can debug the flask app by running following commands:

<details><summary>Linux (Bash)</summary>
<pre>
export FLASK_APP=flaskr.app
export FLASK_ENV=<b>development</b>
flask run
</pre></details>

<details><summary>Windows (CMD)</summary>
<pre>
set FLASK_APP=flaskr.app
set FLASK_ENV=<b>development</b>
flask run
</pre></details>

<details><summary>Windows (PowerShell)</summary>
<pre>
$env:FLASK_APP = "flaskr.app"
$env:FLASK_ENV = "<b>development</b>"
flask run
</pre></details>

### External Debugger

When using an external debugger, the app should still be in debug mode, but it an be useful to disable the built-in debugger and reloader, which can interfere.

* `flask run --no-debugger`
* `flask run --no-reload`
* `flask run --no-debugger --no-reload`

<details>
<summary>Example configuration for <b>VS Code</b></summary>

.vscode/launch.json

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "flaskr/app.py",
                "FLASK_ENV": "development",
                "FLASK_RUN_PORT" : "8080",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run",
                "--no-debugger"
            ],
            "jinja": true
        }
    ]
}
```
</details>

## Testing

To run unit tests:

```bash
# install pytest manually or use "reset-dev.sh"
pip3 install pytest 
pytest
```
## Reset development environment

You can use the script [reset-dev.sh](reset-dev.sh) to reset your development environment:

```bash
. reset-dev.sh
```

The script will do following:
* (Re)create the virtual environment **venv** without dependencies installed
* Activating **venv** in current terminal
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
    * built cython files (*.so, *.pyd)

Now you can build the project manually or with [build.sh](build.sh).