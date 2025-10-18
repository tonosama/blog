import os
import yaml
from urllib.parse import quote
import re

post_file = os.environ.get('LATEST_POST_FILE')
if not post_file:
    print("LATEST_POST_FILE environment variable not set. Exiting.")
    exit()

config_file = '_config.yml'

try:
    # --- サイト設定ファイルを読み込む ---
    with open(config_file, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    base_url = config.get('url', '')

    # --- 投稿ファイルを読み込む ---
    with open(post_file, 'r', encoding='utf-8') as f:
        content_parts = f.read().split('---', 2)
        if len(content_parts) < 3:
            print(f"Error: Could not parse front matter for {post_file}. Dashes '---' not found correctly.")
            exit()
        front_matter = yaml.safe_load(content_parts[1])
    
    title = front_matter.get('title', '')
    tags = front_matter.get('tags', [])
    category = front_matter.get('category', 'uncategorized')

    # --- 記事のURLを組み立てる ---
    filename = os.path.basename(post_file)
    match = re.match(r'(\d{4})-(\d{2})-(\d{2})-(.*)\.md', filename)
    if not match:
        print(f"Error: Filename {filename} does not match expected format YYYY-MM-DD-slug.md")
        exit()

    year, month, day, slug = match.groups()
    
    encoded_category = quote(category.strip())
    post_url = f"{base_url}/{encoded_category}/{year}/{month}/{day}/{slug}.html"

    # --- ツイート本文を組み立てる ---
    hashtags = " ".join([f"#{tag.replace(' ', '').replace('　', '')}" for tag in tags if tag])
    
    base_text = "ブログを更新しました！\n\n『』\n\n"
    url_length = 23 # t.co の短縮URLは23文字
    hashtags_length = len(hashtags) + (2 if hashtags else 0)
    
    max_title_length = 280 - len(base_text) - url_length - hashtags_length
    
    if len(title) > max_title_length:
        title = title[:max_title_length - 3] + '...'
    
    tweet_text = f"ブログを更新しました！\n\n『{title}』\n\n{post_url}"
    if hashtags:
        tweet_text += f"\n\n{hashtags}"

    # GitHub Actionsの次のステップへ、複数行のツイート本文を出力する
    with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
        f.write(f'tweet_text<<EOF\n')
        f.write(f'{tweet_text}\n')
        f.write(f'EOF\n')

except FileNotFoundError as e:
    print(f"Error: File not found - {e}. Make sure the action runs from the repository root.")
    exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit(1)
