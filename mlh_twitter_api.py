import http.client, urllib.request, urllib.parse, urllib.error, base64
import urllib.request
import config
import tweepy
import json

# fetch tweets from our twitter-api
def fetch(twitter_handle):
    url = config.MLH_TWITTER_API + "/api/tweets/" + twitter_handle
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req).read()
    decoded_response = response.decode('utf-8')
    json_data = json.loads(decoded_response)
    return json_data["data"] or []
