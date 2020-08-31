import tweepy
import time

auth = tweepy.OAuthHandler('75831L11mh3WGZ265okVdfcD3',
                           'dbrBUnFWywIueah36KyWSmeeChlnimDC1B8QbAIuuyVODPao6c')
auth.set_access_token('4257143053-XqMItXNB5qYAkt3jC9HRJyxA5ZQhBJ3JW1rcjGA',
                      'bDgET6UPThCaIPpGPcdVNs7TZI4XYxflRq3j5nkdxpJ83')

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# Genrous Bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     # print(follower.name)
#     if follower.name == 'Dj Broox':
#         # if follower.followers_count > 1000:
#         follower.follow()
#         break

search_string = 'Sushant Singh Rajput'
numberofTweets = 3

for tweet in tweepy.Cursor(api.search, search_string).items(numberofTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
