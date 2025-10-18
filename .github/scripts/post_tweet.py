import tweepy
import os
import sys

# 環境変数から認証情報を取得
try:
    consumer_key = os.environ['TWITTER_API_KEY']
    consumer_secret = os.environ['TWITTER_API_KEY_SECRET']
    access_token = os.environ['TWITTER_ACCESS_TOKEN']
    access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    tweet_text = os.environ['TWEET_TEXT']
except KeyError as e:
    print(f"エラー: 必要な環境変数が設定されていません: {e}")
    sys.exit(1)

# ツイート本文が空でないかチェック
if not tweet_text:
    print("ツイート内容が空のため、投稿をスキップします。")
    sys.exit(0)

print("Twitter API v2 を使用してツイートを投稿します...")
print(f"ツイート内容:\n{tweet_text}")

try:
    # API v2用のクライアントを初期化
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    # ツイートを投稿
    response = client.create_tweet(text=tweet_text)
    
    print("\nツイートの投稿に成功しました！")
    print(f"ツイートID: {response.data['id']}")

except Exception as e:
    print(f"\nエラー: ツイートの投稿に失敗しました。")
    print(e)
    sys.exit(1)
