import praw
import pdb
import re
import os

# Create the Reddit instance
reddit = praw.Reddit('bot1')

# create an empty list if we haven't run this code before
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else: # file does exist
    # read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n") # split on newlines
       posts_replied_to = list(filter(None, posts_replied_to))

# Get the top 5 values from our subreddit
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=5):
    
    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Search for posts that contain the words "I love python"
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("Bob the bot says: Yess, it's the best language!!") # bot replies
            print("Bot replying to : ", submission.title)

            posts_replied_to.append(submission.id) # store the current id into our list


# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")








