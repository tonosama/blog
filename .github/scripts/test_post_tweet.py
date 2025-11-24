import sys
import os

# post_tweet.pyをインポートできるようにパスを追加
sys.path.insert(0, os.path.dirname(__file__))

from post_tweet import generate_blog_url

try:
    import pytest
    PYTEST_AVAILABLE = True
except ImportError:
    PYTEST_AVAILABLE = False


class TestGenerateBlogUrl:
    """generate_blog_url関数のテストクラス"""
    
    def test_md_filename_converts_to_posts_url_without_extension(self):
        """
        .mdファイル名が拡張子なしのpostsURLに変換されることを確認
        入力: "2025-11-14-pm-05.md"
        期待: "https://tonosama.github.io/blog/posts/2025-11-14-pm-05/"
        """
        filename = "2025-11-14-pm-05.md"
        expected = "https://tonosama.github.io/blog/posts/2025-11-14-pm-05/"
        assert generate_blog_url(filename) == expected
    
    def test_posts_directory_path_is_removed_from_url(self):
        """
        _posts/ディレクトリパスがURLから除去されることを確認
        入力: "_posts/2025-11-14-pm-05.md"
        期待: "https://tonosama.github.io/blog/posts/2025-11-14-pm-05/"
        """
        filename = "_posts/2025-11-14-pm-05.md"
        expected = "https://tonosama.github.io/blog/posts/2025-11-14-pm-05/"
        assert generate_blog_url(filename) == expected
    
    def test_full_absolute_path_is_removed_from_url(self):
        """
        絶対パス全体がURLから除去され、ファイル名のみが使用されることを確認
        入力: "/Users/tonosama/work/ブログ/startbootstrap-clean-blog-jekyll/_posts/2025-11-14-pm-05.md"
        期待: "https://tonosama.github.io/blog/posts/2025-11-14-pm-05/"
        """
        filename = "/Users/tonosama/work/ブログ/startbootstrap-clean-blog-jekyll/_posts/2025-11-14-pm-05.md"
        expected = "https://tonosama.github.io/blog/posts/2025-11-14-pm-05/"
        assert generate_blog_url(filename) == expected
    
    def test_different_date_format_is_preserved_in_url(self):
        """
        異なる日付フォーマット（01-01）がURLでそのまま保持されることを確認
        入力: "2025-01-01-new-year.md"
        期待: "https://tonosama.github.io/blog/posts/2025-01-01-new-year/"
        """
        filename = "2025-01-01-new-year.md"
        expected = "https://tonosama.github.io/blog/posts/2025-01-01-new-year/"
        assert generate_blog_url(filename) == expected
    
    def test_custom_base_url_replaces_default_domain(self):
        """
        カスタムベースURLがデフォルトドメインを置き換えることを確認
        入力: "2025-11-14-pm-05.md", base_url="https://example.com"
        期待: "https://example.com/posts/2025-11-14-pm-05/"
        """
        filename = "2025-11-14-pm-05.md"
        base_url = "https://example.com"
        expected = "https://example.com/posts/2025-11-14-pm-05/"
        assert generate_blog_url(filename, base_url) == expected
    
    def test_filename_without_md_extension_works(self):
        """
        .md拡張子なしのファイル名も正しく処理されることを確認
        入力: "2025-11-14-pm-05"
        期待: "https://tonosama.github.io/blog/posts/2025-11-14-pm-05/"
        """
        filename = "2025-11-14-pm-05"
        expected = "https://tonosama.github.io/blog/posts/2025-11-14-pm-05/"
        assert generate_blog_url(filename) == expected
    
    def test_multiple_hyphens_in_filename_are_preserved(self):
        """
        ファイル名内の複数のハイフンがURLで保持されることを確認
        入力: "2025-11-14-pm-05-extended-version.md"
        期待: "https://tonosama.github.io/blog/posts/2025-11-14-pm-05-extended-version/"
        """
        filename = "2025-11-14-pm-05-extended-version.md"
        expected = "https://tonosama.github.io/blog/posts/2025-11-14-pm-05-extended-version/"
        assert generate_blog_url(filename) == expected


if __name__ == "__main__":
    # pytestがインストールされていない場合の簡易テスト実行
    test = TestGenerateBlogUrl()
    
    print("テスト実行中...")
    try:
        test.test_md_filename_converts_to_posts_url_without_extension()
        print("✓ .mdファイル名が拡張子なしのpostsURLに変換される - 成功")
        
        test.test_posts_directory_path_is_removed_from_url()
        print("✓ _posts/ディレクトリパスがURLから除去される - 成功")
        
        test.test_full_absolute_path_is_removed_from_url()
        print("✓ 絶対パス全体がURLから除去される - 成功")
        
        test.test_different_date_format_is_preserved_in_url()
        print("✓ 異なる日付フォーマットがURLで保持される - 成功")
        
        test.test_custom_base_url_replaces_default_domain()
        print("✓ カスタムベースURLがデフォルトドメインを置き換える - 成功")
        
        test.test_filename_without_md_extension_works()
        print("✓ .md拡張子なしのファイル名も正しく処理される - 成功")
        
        test.test_multiple_hyphens_in_filename_are_preserved()
        print("✓ ファイル名内の複数のハイフンがURLで保持される - 成功")
        
        print("\n全てのテストが成功しました！")
    except AssertionError as e:
        print(f"✗ テスト失敗: {e}")
        sys.exit(1)

