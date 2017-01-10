import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener



auth = tweepy.OAuthHandler("4OAW8cfY6FLy1xW8LhLJwzMMp","Bz70UwAIPVzOV3j6lIqUjhSgbLY9GCAuy8jUIjcsyvKwMMP91p")
auth.set_access_token("358637575-qNNpnSRvnPOXZeafmwedWcL1VKw0DD9pBYwKpxRg","j4xYlBkQJtBOFlnAFAY8HdDEfyriJCpvxHmgR3WZQ94ew")

 
class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
            #json_load = json.loads(data)
            #texts = json_load['text']
            #print data
            
        except BaseException as e:
            #print &quot;Error on_data: %s&quot; % str(e))
            pass
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])

