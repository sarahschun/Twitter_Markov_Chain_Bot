import markovify
import config
from mlh_twitter_api import get_user_tweets as fetch
from twitter_scraper_fetcher import *
import re
    
 
# build the markov chain based on the text we read
# we use the markovify library to do this step
def generate_bot_answer(twitter_handle, user_question):
    pass
    # write code here
    
def generate_bot_answer_with_text_model(twitter_handle, user_question, text_model):
  bot_answer = None

  word_list = user_question.split(' ')
  random_word = random.choice(word_list)
  bot_answer = text_model.make_sentence_with_start(random_word, strict=False)

  return bot_answer

    
    