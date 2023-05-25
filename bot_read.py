import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("learnpython")

for submission in subreddit.hot(limit=5): # get_hot() gets the top 5 popular subreddit posts
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score) # the total score, adding upvotes and downvotes
    print("---------------------------------\n")

