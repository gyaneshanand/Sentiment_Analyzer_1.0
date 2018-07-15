import tweepy
from textblob import TextBlob
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys

access_token = "1274738779-RediNL4aNteNV7Kc3aPISYF8Md5PBivX0iJ1nAz"
consumer_key = "nWCKL98GwFRvwJZAGHxJMSVi5"
access_secret = '1Z3LjNLPlg93G1YL4ScSlQA5JGqAKQLhhrBeWDIDwJks9'
consumer_secret = 'r01abykzBG1t2cS055r5XVnJX1BFMOdQN61G5QT0YzbChfBf7B'


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)

# tweets = api.search('Sockpuppets')
# for tweet in tweets:
# 	print(tweet.text)
# 	print("\n")
# 	analysis = TextBlob(tweet.text)
# 	print(analysis.sentiment.polarity)
# 	print("")

# account_list = []

# for account in account_list:
# 	print("User ID :\t"+account)
# 	ac = api.get_user(account)
# 	print("User Name :\t"+ac.name)
account = 1274738779
#account ='realDonaldTrump'
print("User ID :\t"+str(account))
ac = api.get_user(account)
name = ac.name
print("User Name :\t"+name)
print("screen_name: " + ac.screen_name)
#print("description: " + ac.description)
print("statuses_count: " + str(ac.statuses_count))
print("friends_count: " + str(ac.friends_count))
print("followers_count: " + str(ac.followers_count))

# print("The followers of "+name+" are")
# for follower in api.followers(account):
# 	print(follower.name)

tweets = ac.statuses_count
account_created_date = ac.created_at
delta = datetime.utcnow() - account_created_date
account_age_days = delta.days
print("Account age (in days): " + str(account_age_days))
if account_age_days > 0:
	print("Average tweets per day : " + "%.2f"%(float(tweets)/float(account_age_days)))

hashtags = []
mentions = []
tweet_count = 0
end_date = datetime.utcnow() - timedelta(days=100)
for status in tweepy.Cursor(api.user_timeline, id=account).items():
	tweet_count += 1
	print(status.text)
	if hasattr(status, "entities"):
	    entities = status.entities
	    if "hashtags" in entities:
	      for ent in entities["hashtags"]:
	        if ent is not None:
	          if "text" in ent:
	            hashtag = ent["text"]
	            if hashtag is not None:
	              hashtags.append(hashtag)
	    if "user_mentions" in entities:
	      for ent in entities["user_mentions"]:
	        if ent is not None:
	          if "screen_name" in ent:
	            name = ent["screen_name"]
	            if name is not None:
	              mentions.append(name)
	# if status.created_at < end_date:
	# 	break
print
print("Most mentioned Twitter users:")
for item, count in Counter(mentions).most_common(10):
  print(item + "\t" + str(count))

print
print("Most used hashtags:")
for item, count in Counter(hashtags).most_common(10):
  print(item + "\t" + str(count))

print
print "All done. Processed " + str(tweet_count) + " tweets."
print