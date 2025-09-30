# stashapp-tools
This library primarily serves as a API wrapper for [Stash](https://github.com/stashapp/stash) written in python

## Requirements
Developed using python 3.11.X with attempts to make things as backwards compatible where possible, if you are having issues please try using python 3.11

## Installation 

##### To install from PyPI use this command:
`pip install stashapp-tools`

##### To install directly from this repo use this command:
`pip install git+https://github.com/stg-annon/stashapp-tools`

## Usage
```python
import stashapi.log as log
from stashapi.stashapp import StashInterface

stash = StashInterface({
    "scheme": "http",
    "host":"localhost",
    "port": "9999",
    "logger": log
})

scene_data = stash.find_scene(1234)
log.info(scene_data)
```
This example creates a connection to Stash query's a scene with ID 1234 and prints the result to Stash's logs
