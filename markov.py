                  ## write code here!!
import config
from mlh_twitter_api import get_user_tweets as fetch
from twitter_scraper_fetcher import *
import re


# remove emoji, punctuation, urls from tweets
def create_string(tweets):
    text = ""

    for tweet in tweets:
        text += (
            tweet + "\n\n"
        )  # Make sure each tweet is handled properly by markovify
    return text


def generate_bot_answer_with_text_model(text_model):
    pass
    ## write code here
    
    
    
    
    
    
    
# build the markov chain based on the text we read
# we use the markovify library to do this step
def generate_bot_answer(twitter_handle, user_question):
    pass
  
    ## write code here
