from DictionaryTextFormatter import DictionaryTextFormatter
from TickerCounterFiltered import TickerCounterFiltered
from ContentParser import ContentParser
from TickerCounter import TickerCounter
from ConfigReader import ConfigParser
from loguru import logger
import praw
import re

config = ConfigParser()
print(config.get("Secret"))



reddit = praw.Reddit(
    client_id = config.get("ClientId"),
    client_secret = config.get("Secret"),
    user_agent = "windows:com.tothemoon (by u/skykight)",
    password= config.get("Password"),
    username= config.get("Username")
)
subreddit = reddit.subreddit("wallstreetbets")

print(subreddit.display_name)  # output: redditdev

counter = TickerCounterFiltered()

def word_match_count(sentence: str):
    parser = ContentParser()

    words = parser.get_clean_sentence(sentence).split(" ")

    for word in words:
        if word in counter.counter.keys():
            counter.counter[word] = counter.counter[word] + 1 

for submission in subreddit.new(limit=300):
    word_match_count(submission.title)
    word_match_count(submission.selftext)
    
    for comment in submission.comments:
        try:
            word_match_count(comment.body)
        except:
            logger.warning("An exception occurred fetch + parse a comment")
        
    
    #print(submission.title)
    #print(submission.selftext)


DictionaryTextFormatter.write_formatted_list( counter.get_ticker_count(), limit=0)