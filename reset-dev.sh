# This script will reset the local dev environment
# It will also create a new python virtual environment and activate it
echo "Deactivating venv if it exists..."
source venv/bin/activate
deactivate
echo "Deleting build and development files..."
find . | grep -E "(venv|build|dist|__pycache__|.pytest_cache|\.pyc|\.pyd|\.pyo$|\.so|*egg-info)" | xargs rm -rf
echo "Creating new virtual environment..."
python3 -m venv venv
source venv/bin/activate
echo "Installing development dependencies..."
pip install pip --upgrade
pip install flake8 pylint autopep8 pytest
COL='\033[1;32m'
echo -e "${COL}Now you can build the project manually or by using build.sh"