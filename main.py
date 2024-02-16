import praw
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

reddit = praw.Reddit(
    client_id = config['client_id'],
    client_secret = config['client_secret'],
    user_agent = config['user_agent'],
    username = config['username'],
    password = config['password']
)

for submission in reddit.subreddit('wallstreetbets').hot(limit=5):
    print(submission.title)