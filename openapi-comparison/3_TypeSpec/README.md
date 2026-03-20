# How to run
## Setup
`pip install -r requirements.txt`  
`npm install -g @typespec/compiler`  
`npm install @typespec/http @typespec/rest @typespec/openapi3`
## Start flask server
`python server.py`
## Visualize api docs
`tsp compile api.tsp --emit @typespec/openapi3`  
`cd tsp-output/@typespec/openapi3/`  
`npx swagger-ui-watcher api.yaml`
## Access api doc at
`localhost:8000`