import tweepy
import time

auth = tweepy.OAuthHandler('42RIPQO7ozMoIfRR12czuQnr2', 'RhhGtwoXO1gNhgWzPVc8Kqz3tIpUE93zZ5haFquQlfr2RMwLYA')
auth.set_access_token('1236554053850628096-ET80BEZ0ygXicu7pq7RPUfc5oHX5dR',
                      'E8SMn4IAZTQfdFDtw3Wuwt0JgHoaM2EgisbsZnUpb5UTG')

api = tweepy.API(auth)

user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


# generousBot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Madam':
        follower.follow()
        break
