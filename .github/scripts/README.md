# Twitter投稿スクリプト

このディレクトリには、ブログ記事をTwitterに自動投稿するためのスクリプトが含まれています。

## ファイル構成

- `post_tweet.py`: Twitter APIを使用してツイートを投稿するメインスクリプト
- `test_post_tweet.py`: URL生成機能のテストスクリプト
- `requirements.txt`: 必要なPythonパッケージ
- `prepare_tweet.py`: ツイート準備用スクリプト（既存）

## セットアップ

### 必要なパッケージのインストール

```bash
pip install -r requirements.txt
```

## 機能

### 1. URL生成機能

`generate_blog_url()` 関数は、ブログ記事のファイル名から公開URLを生成します。

**例:**
```python
from post_tweet import generate_blog_url

# 基本的な使用例
url = generate_blog_url("2025-11-14-pm-05.md")
# 結果: "https://tonosama.github.io/blog/posts/2025-11-14-pm-05/"

# パスを含むファイル名
url = generate_blog_url("_posts/2025-11-14-pm-05.md")
# 結果: "https://tonosama.github.io/blog/posts/2025-11-14-pm-05/"

# カスタムベースURL
url = generate_blog_url("2025-11-14-pm-05.md", "https://example.com")
# 結果: "https://example.com/posts/2025-11-14-pm-05/"
```

### 2. Twitter投稿機能

`post_tweet.py` をスクリプトとして実行すると、環境変数から認証情報を取得してツイートを投稿します。

**必要な環境変数:**
- `TWITTER_API_KEY`: Twitter APIキー
- `TWITTER_API_KEY_SECRET`: Twitter APIキーシークレット
- `TWITTER_ACCESS_TOKEN`: Twitterアクセストークン
- `TWITTER_ACCESS_TOKEN_SECRET`: Twitterアクセストークンシークレット
- `TWEET_TEXT`: 投稿するツイートの内容

**実行例:**
```bash
export TWITTER_API_KEY="your_api_key"
export TWITTER_API_KEY_SECRET="your_api_key_secret"
export TWITTER_ACCESS_TOKEN="your_access_token"
export TWITTER_ACCESS_TOKEN_SECRET="your_access_token_secret"
export TWEET_TEXT="新しいブログ記事を公開しました！"

python3 post_tweet.py
```

## テスト

### テストの実行

URL生成機能のテストを実行するには:

```bash
# 基本的なテスト実行（pytestなし）
python3 test_post_tweet.py

# pytestを使用したテスト実行（pytestがインストールされている場合）
pytest test_post_tweet.py -v
```

### テストケース

以下のテストケースが含まれています：

1. **test_md_filename_converts_to_posts_url_without_extension**: .mdファイル名が拡張子なしのpostsURLに変換されることを確認
   - 入力: `2025-11-14-pm-05.md`
   - 期待: `https://tonosama.github.io/blog/posts/2025-11-14-pm-05/`

2. **test_posts_directory_path_is_removed_from_url**: _posts/ディレクトリパスがURLから除去されることを確認
   - 入力: `_posts/2025-11-14-pm-05.md`
   - 期待: `https://tonosama.github.io/blog/posts/2025-11-14-pm-05/`

3. **test_full_absolute_path_is_removed_from_url**: 絶対パス全体がURLから除去され、ファイル名のみが使用されることを確認
   - 入力: `/Users/tonosama/work/ブログ/startbootstrap-clean-blog-jekyll/_posts/2025-11-14-pm-05.md`
   - 期待: `https://tonosama.github.io/blog/posts/2025-11-14-pm-05/`

4. **test_different_date_format_is_preserved_in_url**: 異なる日付フォーマット（01-01）がURLでそのまま保持されることを確認
   - 入力: `2025-01-01-new-year.md`
   - 期待: `https://tonosama.github.io/blog/posts/2025-01-01-new-year/`

5. **test_custom_base_url_replaces_default_domain**: カスタムベースURLがデフォルトドメインを置き換えることを確認
   - 入力: `2025-11-14-pm-05.md`, ベースURL: `https://example.com`
   - 期待: `https://example.com/posts/2025-11-14-pm-05/`

6. **test_filename_without_md_extension_works**: .md拡張子なしのファイル名も正しく処理されることを確認
   - 入力: `2025-11-14-pm-05`
   - 期待: `https://tonosama.github.io/blog/posts/2025-11-14-pm-05/`

7. **test_multiple_hyphens_in_filename_are_preserved**: ファイル名内の複数のハイフンがURLで保持されることを確認
   - 入力: `2025-11-14-pm-05-extended-version.md`
   - 期待: `https://tonosama.github.io/blog/posts/2025-11-14-pm-05-extended-version/`

## 開発

### 新しいテストの追加

`test_post_tweet.py`の`TestGenerateBlogUrl`クラスに新しいテストメソッドを追加してください：

```python
def test_your_specific_behavior_description(self):
    """
    何をテストするかの具体的な説明（期待結果を含む）
    入力: "your-test-file.md"
    期待: "https://tonosama.github.io/blog/posts/your-test-file/"
    """
    filename = "your-test-file.md"
    expected = "https://tonosama.github.io/blog/posts/your-test-file/"
    assert generate_blog_url(filename) == expected
```

テストメソッドを追加した後、`if __name__ == "__main__":`ブロックにも追加してください：

```python
test.test_your_specific_behavior_description()
print("✓ あなたのテストの説明 - 成功")
```

**テストメソッド名のベストプラクティス:**
- 何をテストするかが明確に分かる名前を使用する
- 期待される動作を動詞で表現する（例: `converts_to`, `is_removed`, `are_preserved`）
- 長くても読みやすさを優先する

## トラブルシューティング

### ImportError: No module named 'tweepy'

必要なパッケージがインストールされていません：
```bash
pip install -r requirements.txt
```

### 環境変数が設定されていませんエラー

Twitter APIの認証情報が環境変数として設定されていることを確認してください。GitHub Actionsで使用する場合は、リポジトリのSecretsに設定してください。

