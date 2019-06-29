import http.client, urllib.request, urllib.parse, urllib.error, base64
import urllib.request
import config
import tweepy
import json


# fetch tweets from our twitter-api
def get_user_tweets(twitter_handle):
    url = config.MLH_TWITTER_API + "/api/tweets/" + twitter_handle
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req).read()
    decoded_response = response.decode('utf-8')
    json_data = json.loads(decoded_response)
    return json_data["data"] or []

def moderate(message):
    url = config.MLH_TWITTER_API + "/api/moderated_content"
    req = urllib.request.Request(url)
    req.add_header("Content-Type", "application/json; charset=utf-8")
    jsondata = json.dumps({"content": message})
    jsondataasbytes = jsondata.encode("utf-8")
    req.add_header("Content-Length", len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes).read()
    decoded_data=response.decode('utf-8')
    json_data = json.loads(decoded_data)
    moderated_data = json_data["data"]
    if not moderated_data or moderated_data == None:
      return message
    return moderated_data