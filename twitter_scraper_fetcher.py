import requests
from bs4 import BeautifulSoup
import re

CONTENT_CLASS_NAME = "TweetTextSize"
CONTENT_CONTAINER_TAGS = ["p"]
EMPTY_ITEMS = [None, " ", "None"]
TWITTER_URL = "https://twitter.com/"


def get_elements(twitter_handle):
    url = TWITTER_URL + twitter_handle
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html, features="html.parser")

    return soup.find_all(
CONTENT_CONTAINER_TAGS,  
	attrs={"class": CONTENT_CLASS_NAME})

    
def get_user_tweets(twitter_handle):
  elements = get_elements(twitter_handle)
  tweets = []

  for post in elements:
      for text in post.contents:
          # check if line contains real text
          if text.string not in EMPTY_ITEMS:
              tweets.append(text.string)
  return tweets

def clean_tweets_data(tweets):
  emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+",
        flags=re.UNICODE,
    )
  url_pattern = re.compile(r"\S+\/\S+", re.DOTALL)
  mentions_pattern = re.compile(r"@\S+", re.DOTALL)

  cleaned_tweets = []
  for tweet in tweets:
    text_without_emoji = emoji_pattern.sub(r"", tweet)
    text_without_url = url_pattern.sub(r"", text_without_emoji)
    cleaned_tweets.append(mentions_pattern.sub(r"", text_without_url))

  return cleaned_tweets 

 


    
  
            
                

    
