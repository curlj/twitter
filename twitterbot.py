#!/usr/bin/python3.6

import tweepy
import datetime

d = datetime.datetime.today()
today = d.date()

consumer_key = 'nU3Z4mSTHVXnZ2a2U5tdVvAvk'
consumer_secret = 'a6f2fyDjUoW2gZkoAZUHkJCcmcZ0XYznc9sOyFmD7M5ujzqzJH'
access_token = '1120036623876538368-SFyOn6hdChQpr6JyaWoS1I4UOcaY3c'
access_token_secret = '72sCVERPMahLkbePRpdSSsWLf57ukIWVkLvIc7lOFIXTq'

# sets up the authentication for boringpostsonly account
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
boring = tweepy.API(auth)

terms = {"#potatoes", "#oklahoma", "#bored", "#flatearth"}
output = ""
for term in terms:
    counter = 0
    for tweet in tweepy.Cursor(boring.search, q=term, since=today).items():
        try:
            # Add \n escape character to print() to organize tweets
            counter += 1
        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
    output += term + ": " + str(counter) + "\n"
boring.update_status(output)
print("update completed")