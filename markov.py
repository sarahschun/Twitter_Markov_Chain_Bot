# write code here!!
import markovify
import config
from mlh_twitter_api import *
from twitter_scraper_fetcher import *
import random
import re
    
    
def generate_bot_answer_with_text_model(twitter_handle, user_question, text_model):
    bot_answer = None

    word_list = user_question.split("")
    random_word = random.choice(word_list)
# build the markov chain based on the text we read
# we use the markovify library to do this step
def generate_bot_answer(twitter_handle, user_question):
    pass
    # write code here