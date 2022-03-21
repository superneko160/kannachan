import codeinfo
import tweepy
import sys

# TwitterAPIの取得
def get_twitterclient():
    try:
        client = tweepy.Client(
            bearer_token=codeinfo.BEARER_TOKEN,
            consumer_key=codeinfo.API_KEY,
            consumer_secret=codeinfo.API_SECRET,
            access_token=codeinfo.ACCESS_TOKEN,
            access_token_secret=codeinfo.ACCESS_SECRET
        )
        return client
    except Exception as e:
        print(e)
        return ""

# タイムラインの取得
def get_timeline(client): 
    user = client.get_user(username=codeinfo.TL_PROVIDER_NAME)
    tweets =client.get_users_tweets(id=user[0]['id'])
    return tweets[0]

# ツイートする
def tweet(client, tweet_text):
    # Tweepyの内部でtwitter api v1を使っているので、Elvatedへの申請が必要
    # 申請してないとレスポンス401
    response = client.create_tweet(text=tweet_text)
    # print(response)