import urllib.request
import json
import config
import re


def moderate(message):
  data = make_request_to_api(message)
  decoded_data=data.decode('utf-8')
  json_data = json.loads(decoded_data)
  moderated_data = json_data["data"]

  if not moderated_data or moderated_data == None:
    return message

  return moderated_data


def make_request_to_api(message):
  url = config.MLH_TWITTER_API + "/api/moderated_content"
  req = urllib.request.Request(url)
  req.add_header("Content-Type", "application/json; charset=utf-8")
  jsondata = json.dumps({"content": message})
  jsondataasbytes = jsondata.encode("utf-8")
  req.add_header("Content-Length", len(jsondataasbytes))
  response = urllib.request.urlopen(req, jsondataasbytes).read()

  return response
