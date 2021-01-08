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

## Requirements

* python3
* python3-dev
* **Optional**: python3-venv

```bash
# example installation for ubuntu
sudo apt-get update
sudo apt-get install python3 python3-dev python3-venv
```

## Simple instructions (Linux or WSL)

To **build/install** the flask application use

```bash
. build.sh
```

After that you can **run** the server on port **:8080** with

```bash
. run.sh
```

To test the application use

```bash
# install flake8 and pytest manually or use "reset-dev.sh"
pip install flake8 pytest 
pytest
```

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

### In-Built flask debugger
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

* --no-debugger
* --no-reload

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

### Virtual Environment

For local development you can use a [virtual environment](https://docs.python.org/3/tutorial/venv.html).

[How to install virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b). 

```bash
# example for linux
python3 -m venv "venv"
source venv/bin/activate
````

With `deactivate` you can disable the virtual environment again

### Reset development environment

You can also use the script **reset-dev.sh** to reset the project with

```bash
. reset-dev.sh
```

The script **reset-dev.sh** will do the following for you: 
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

Now you can build the project manually or with `. build.sh`