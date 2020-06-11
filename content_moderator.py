import http.client, urllib.request, urllib.parse, urllib.error, base64
import urllib.request
import config
import json


def moderate(message):
    print('Moderating message')
    data = make_request_to_api(message)
    decoded_data=data.decode('utf-8')
    json_data = json.loads(decoded_data)
    moderated_data = json_data["data"]
    print(moderated_data)

    if not moderated_data or moderated_data == None:
        return message
    print('returning moderated data: ' + moderated_data)
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
