import tweepy

auth = tweepy.OAuthHandler("4OAW8cfY6FLy1xW8LhLJwzMMp","Bz70UwAIPVzOV3j6lIqUjhSgbLY9GCAuy8jUIjcsyvKwMMP91p")
auth.set_access_token("358637575-qNNpnSRvnPOXZeafmwedWcL1VKw0DD9pBYwKpxRg","j4xYlBkQJtBOFlnAFAY8HdDEfyriJCpvxHmgR3WZQ94ew")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print tweet.text
user = api.get_user('twitter')
#print user.screen_name
print user.followers_count
for friend in user.friends():
   print friend.screen_name

