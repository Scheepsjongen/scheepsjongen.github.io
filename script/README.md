# Script

This script imports questions from the google docs file to the xml format used by site

## Usage

1. You should have python 3 installed
1. Follow [quickstart instructions](https://developers.google.com/docs/api/quickstart/python) for Google Docs Python SDK. You need to generate `credentials.json` and place it to `/script` directory.
1. Run `pip3 install -r ./requirements.txt`
1. Run `python3 ./create-xml.py`
1. File `../quiz/pre-2021-test.xml` should have been updated. 
