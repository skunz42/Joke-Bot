#Bad Joke Bot
#Sean Kunz

import praw
import pdb
import re
import os

r = praw.Reddit(client_id= '47amL0AVjU1x0Q',
    client_secret= 'xXlREmF82q0ARucmF7ay8stZihY',
    password= '',
    user_agent= 'Bad Jokes',
    username= 'Bad-Joke-Bot')

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

for comment in r.subreddit('HackBUBotTest').stream.comments():
    if comment.id not in posts_replied_to and comment.author != 'Bad-Joke-Bot' and comment.body == 'hi':
        comment.reply('Hello')
        #posts_replied_to.append(comment.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
