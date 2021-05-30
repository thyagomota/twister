# twister
The only Python library that you need for accessing the Twitter API

Twister gives you the flexibility to use Twitter's API methods directly. For example, to do a simple tweet lookup you need to make a call to https://api.twitter.com/2/tweets/:id, replacing :id with the tweet's id. The example below shows how to make that call to get the tweet with id = 1222975972938522624. 

```python
import os
from twister import API

if __name__ == "__main__":

    try: 
        twister = API(
            consumer_key    = os.getenv('CONSUMER_KEY'),
            consumer_secret = os.getenv('CONSUMER_SECRET')
        )
        tweet = twister.get(
            op = '2/tweets/1222975972938522624',
            params = {}
        )
        print(tweet)
```

What if you want to use Twitter's operation https://api.twitter.com/2/tweets that returns multiple tweets from a single request? 

```python
import os
from twister import API

if __name__ == "__main__":

    try: 
        twister = API(
            consumer_key    = os.getenv('CONSUMER_KEY'),
            consumer_secret = os.getenv('CONSUMER_SECRET')
        )
        params = {
            'ids': '1222975972938522624,1222959455933030400',
            'tweet.fields': 'author_id,entities,attachments,created_at,referenced_tweets', 
            'expansions': 'author_id,referenced_tweets.id,in_reply_to_user_id,geo.place_id,entities.mentions.username,referenced_tweets.id.author_id'
        }        
        tweets = twister.get(
            op = '2/tweets',
            params = params
        )
        print(tweets)
```
