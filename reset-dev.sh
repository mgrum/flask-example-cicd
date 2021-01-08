# This script will reset the local dev environment
# It will also create a new python virtual environment and activate it
echo "Deactivating venv if it exists..."
source venv/bin/activate
deactivate
echo "Deleting build and development files..."
find . -type d | grep -E "(venv|build|dist|__pycache__|.pytest_cache|egg-info)" | xargs rm -rf
find . -type f | grep -E "(\.pyc|\.pyd|\.pyo$|\.so)" | xargs rm -rf
echo "Creating new virtual environment..."
python3 -m venv venv
source venv/bin/activate
echo "Installing development dependencies..."
pip3 install pip --upgrade
pip3 install flake8 pylint autopep8 pytest
COLOR='\033[1;32m'
echo -e "${COLOR}Now you can build the project manually or by using build.sh"