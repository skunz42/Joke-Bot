#Bad Joke Bot
#Sean Kunz

import praw

reddit = praw.Reddit(client_id= ':^)',
    client_secret= ':^)',
    password= ':^)',
    user_agent= 'Bad Jokes',
    username= 'Bad-Joke-Bot')

print(reddit.user.me())