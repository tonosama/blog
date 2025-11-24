import tweepy
import os
import sys
import re


def generate_blog_url(filename, base_url="https://tonosama.github.io/blog"):
    """
    ブログ記事のファイル名からURLを生成する
    
    Args:
        filename (str): ブログ記事のファイル名（例: "2025-11-14-pm-05.md" または "_posts/2025-11-14-pm-05.md"）
        base_url (str): ブログのベースURL
    
    Returns:
        str: 生成されたURL（例: "https://tonosama.github.io/blog/posts/2025-11-14-pm-05/"）
    """
    # ファイル名からベース名を取得（パスと拡張子を除去）
    basename = os.path.basename(filename)
    name_without_ext = os.path.splitext(basename)[0]
    
    # URLを生成
    url = f"{base_url}/posts/{name_without_ext}/"
    return url


def main():
    """メイン処理"""
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


if __name__ == "__main__":
    main()
