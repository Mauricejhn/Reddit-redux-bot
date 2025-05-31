import os
import time
import random
import praw
from flask import Flask
from threading import Thread

# Reddit API credentials from environment variables
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"),
    user_agent=os.getenv("USER_AGENT"),
)

# Confirm login
try:
    print(f"✅ Logged in as: {reddit.user.me()}")
except Exception as e:
    print(f"❌ Reddit login failed: {e}")

# Subreddits and search terms
subreddits = ["Roblox", "RobloxDev", "RobloxUsers", "FreeRobux", "gaming"]
search_terms = ["robux", "free robux", "robux method", "roblox giveaway"]

# Rotating comments
comments = [
    "This actually works! ✅ [Get Free Robux here](https://legendary-basbousa-8c894c.netlify.app)",
    "Just got mine from here! 🔥 [Claim Free Robux](https://legendary-basbousa-8c894c.netlify.app)",
    "Not a scam — try this if you're from 🇺🇸🇬🇧🇨🇦🇦🇺🇩🇪 [Get Robux Now](https://legendary-basbousa-8c894c.netlify.app)",
    "Worked for me 💯 Check it out: [Free Robux](https://legendary-basbousa-8c894c.netlify.app)"
]

def comment_on_posts():
    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        for term in search_terms:
            print(f"Searching in r/{subreddit_name} for '{term}'...")
            try:
                for submission in subreddit.search(term, limit=2):
                    print(f"📝 Commenting on: {submission.title}")
                    try:
                        submission.reply(random.choice(comments))
                        print("✅ Comment posted.")
                        time.sleep(random.randint(45, 80))
                    except Exception as e:
                        print(f"⚠ Error replying: {e}")
            except Exception as e:
                print(f"⚠ Search error in r/{subreddit_name}: {e}")

# Flask app to keep bot alive
app = Flask('')

@app.route('/')
def home():
    return "✅ Reddit Robux bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()

# Run bot
if __name__ == "_main_":
    keep_alive()
    while True:
        comment_on_posts()
        print("😴 Sleeping for 1 hour...")
        time.sleep(3600)