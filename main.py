import praw
import time
from keep_alive import keep_alive

# Start web server for UptimeRobot ping
keep_alive()

# Reddit login
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    username='YOUR_REDDIT_USERNAME',
    password='YOUR_REDDIT_PASSWORD',
    user_agent='script by /u/YOUR_REDDIT_USERNAME'
)

print(f"Logged in as: {reddit.user.me()}")

# Subreddits and keywords
subreddits = ['Roblox', 'FreeRobux', 'RobloxDev', 'RobloxUsers', 'gaming']
search_terms = ['free robux', 'robux', 'robux method', 'roblox giveaway']
comments = [
    "I just got Robux using this! 🔥 [Try here](https://legendary-basbousa-8c894c.netlify.app)",
    "You can actually earn Robux now! ✅ [Check this site](https://legendary-basbousa-8c894c.netlify.app)",
    "Worked for me today! 💯 Get Robux [right here](https://legendary-basbousa-8c894c.netlify.app)"
]

def run_bot():
    while True:
        for sub in subreddits:
            subreddit = reddit.subreddit(sub)
            for term in search_terms:
                print(f"Searching in r/{sub} for '{term}'...")
                try:
                    for post in subreddit.search(term, sort='new', limit=3):
                        try:
                            post.reply(random.choice(comments))
                            print(f"Commented on post: {post.title}")
                            time.sleep(10)
                        except Exception as e:
                            print(f"Error commenting: {e}")
                    time.sleep(5)
                except Exception as e:
                    print(f"Error in r/{sub}: {e}")
        print("Sleeping for 1 hour...")
        time.sleep(3600)

import random
run_bot()