#!/usr/bin/python
'''Example Application to post a tweet from AGI'''

import tweepy
import asterisk.agi
import sys

# Your Keys Here:
consumerKey = ''
consumerSecret = ''
oauthToken = ''
oauthTokenSecret = ''

agi = asterisk.agi.AGI()
status = agi.get_variable('status')[1:-1]

try:
   auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
   auth.set_access_token(oauthToken, oauthTokenSecret)
   api = tweepy.API(auth)
   tweet = api.update_status(status)
   success = "SUCCESS! https://twitter.com/%s/status/%s" % (tweet.user.screen_name, tweet.id)
   agi.verbose(success)
   agi.set_variable('tweet_success','1')
except tweepy.TweepError as e:
   agi.verbose('Twitter encountered an error: %s' % e.reason[1:-1])
   agi.set_variable('tweet_success','0')

sys.exit(0)
