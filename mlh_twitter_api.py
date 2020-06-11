import http.client, urllib.request, urllib.parse, urllib.error, base64
import urllib.request
import config
import tweepy
import json

def moderate(message):
    data = make_request_to_api(message)
    decoded_data=data.decode('utf-8')
    json_data = json.loads(decoded_data)
    moderated_data = json_data["data"]
    print(moderated_data)

    if not moderated_data or moderated_data == None:
        return message
    return moderated_data
  
# fetch tweets from our twitter-api
def fetch(twitter_handle):
    url = config.MLH_TWITTER_API + "/api/tweets/" + twitter_handle
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req).read()
    decoded_response = response.decode('utf-8')
    json_data = json.loads(decoded_response)
    return json_data["data"] or []
