import tweepy
from textblob import TextBlob


class TweetAnalysis:
    consumer_key = 'JWKTQCuMm0GAtXg6YYrGUJzx3'
    consumer_secret = 'D4PCqBeQQpCfi8V5M6BFoEX7XkpuU4ifNTwmNRLeSPilnfvK7C'
    access_token = '2823584030-EZV6sIfbSKuINaTtzI3E6Dn6JBrQItaW8DaYy9a'
    access_secret = 'qmFPe4jh5jb1mEZAdCiT72uOQZGbEhcTzjDozEFkOjKNj'


    def __init__(self):
        access_secret = 'qmFPe4jh5jb1mEZAdCiT72uOQZGbEhcTzjDozEFkOjKNj'


    def performAnalysis(self, querry):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        positive = 0
        negative = 0
        neutral = 0
        api = tweepy.API(auth)
        public_tweets = api.search(q=querry, count=100)

        for tweet in public_tweets:
            # print(tweet.text)
            # print(tweet.created_at)
            # print(tweet)
            analysis = TextBlob(tweet.text)
            if analysis.sentiment.polarity > 0:
                positive = positive+1

            if analysis.sentiment.polarity < 0:
                negative = negative +1

            if analysis.sentiment.polarity == 0:
                neutral = neutral + 1

        list = []

        list.append(positive)
        list.append(negative)
        list.append(neutral)

        return list
