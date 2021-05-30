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
