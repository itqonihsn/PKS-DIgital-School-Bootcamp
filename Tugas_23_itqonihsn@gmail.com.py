import requests
import json
import tweepy

class tweet_scraper:
    def __init__(self):
        with open("token.json") as f:
            tokens = json.load(f)
        
        self.bearer_token = tokens['bearer_token']
        self.api_key = tokens['api_key']
        self.api_key_secret = tokens['api_key_secret']
        self.access_token = tokens['access_token']
        self.access_token_secret = tokens['access_token_secret']
    
    def user_timeline_scraper(self, username):
        auth = tweepy.OAuthHandler(self.api_key, self.api_key_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        
        tweets = tweepy.Cursor(self.api.user_timeline, screen_name=username, count=10, tweet_mode='extended').items(10)
        for tweet in tweets:
            print(tweet.full_text)
            print("----------------------------------------------------")


username = "MataNajwa"
scraper = tweet_scraper()
hasil = scraper.user_timeline_scraper(MataNajwa)
# user_timeline_scraper(username)
