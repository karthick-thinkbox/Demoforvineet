import requests
import json
load={ "request": { "source_type":"web", "source_version":"1.0", "project":"baity" }, "data": { "config_type": "property" } }
res=requests.post('http://staging.fliptango.com:2500/baity/api/getconfig/',json=load)
print(res.json()[category][name])
