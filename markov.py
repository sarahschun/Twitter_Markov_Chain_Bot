import markovify
import config
from mlh_twitter_api import *
from twitter_scraper_fetcher import *
import random
import re
    
    
def generate_bot_answer_with_text_model(twitter_handle, user_question, text_model):
    bot_answer = None
    
    word_list = user_question.split(" ")
    random_word = random.choice(word_list)
    bot_answer = text_model.make_sentence_with_start(random_word, strict = False)
    print("Print me if this function runs!")
    if bot_answer == None:
      bot_answer = text_model.make_sentence()
      
    if bot_answer == None:
      bot_answer = generate_bot_answer_with_text_model(twitter_handle, user_question, text_model)
    
    return bot_answer
    

# build the markov chain based on the text we read
# we use the markovify library to do this step
def generate_bot_answer(twitter_handle, user_question):
    tweets = fetch(twitter_handle)
    clean_tweets = clean_tweets_data(tweets)
    text = "".join(map(str, clean_tweets))
    text_model = markovify.Text(text)
    bot_answer = generate_bot_answer_with_text_model(twitter_handle, user_question, text_model)
    return bot_answer