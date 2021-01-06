# This script will install dependencies and modules
pip install pip --upgrade
pip install -r requirements.txt
pip install -e .
python setup.py bdist_wheel