# How to run
## Setup
`pip install -r requirements.txt`
## Start flask server
`python server.py`
## Visualize api docs
`npx aglio -i api.apib -s`
## Access api doc at
`localhost:3000`
## Convert to openapi
`npx apib2swagger -i api.apib --yaml -o api.yaml`