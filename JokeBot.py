#Bad Joke Bot
#Sean Kunz

import praw
import pdb
import re
import os



if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Get the subreddit
subreddit = reddit.subreddit('HackBUBotTest')
for submission in subreddit.hot(limit=10):

    # If new post
    if submission.id not in posts_replied_to:

        # Caps ignored, can be within a word
        if re.search("ITGOES", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("GUILLOTINE...YUH")
            #YUH
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

print(reddit.user.me())
