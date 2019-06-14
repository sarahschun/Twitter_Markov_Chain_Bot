from flask import Flask, render_template
from flask_socketio import SocketIO
from twitter_scraper_fetcher import *
from content_moderator import moderate
import json
import config
import random

app = Flask(__name__)
socketio = SocketIO(app)

# Renders UI
@app.route("/")
def home():
  return render_template("homepage.html")

# Chat API - WebSocket
@socketio.on("send question")
def generate_message(body, methods=["POST"]):
  question = body["message"]
  twitter_handle = body["username"]

  # Call get_user_tweets() from twitter_scraper_fetcher.py to scrape some tweets
  tweets = get_user_tweets(twitter_handle)

  try:
    # Get a random tweet from the list of tweets
    single_tweet = random.choice(tweets)
    bot_answer = moderate(single_tweet)

    # Send the answer to the app, to display to the user
    answer = {"username": twitter_handle, "message": bot_answer}
    socketio.emit("bot answer", answer)
  except:
    bot_answer = "Sorry, I couldn't process that. Try again please."
    socketio.emit("error", {"username": twitter_handle, "message": bot_answer})

if __name__ == "__main__":
    socketio.run(app)

