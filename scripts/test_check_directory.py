"""Regression tests for the offline directory checker; run with unittest."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import check_directory as check


class DirectoryChecks(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.en = self.make_readme(0)
        self.zh = self.make_readme(1)
        self.write_readmes()

    @staticmethod
    def make_readme(language):
        text = "# Directory\n\n[Local](guide.md#标题与-中文)\n\n"
        # This table is not a product table and must be ignored.
        text += "## Quick start\n\n| Task | Choice |\n| --- | --- |\n| Research | A tool |\n\n"
        for index, pair in enumerate(check.CATEGORY_HEADINGS):
            text += f"## {pair[language]}\n\n| Tool | Description |\n| --- | --- |\n"
            if index == 0:
                text += f"| [Baizhi]({check.FEATURED_URL}) · [Source]({check.FEATURED_SOURCE}) | Workbench. |\n"
                text += f"| [WorkBuddy]({check.WORKBUDDY_URL}) | Assistant. |\n"
            else:
                text += f"| [Tool {index}](https://example.com/tool-{index}) | Description. |\n"
            text += "\n"
        return text

    def write_readmes(self):
        (self.root / "README.md").write_text(self.en, encoding="utf-8")
        (self.root / "README.zh-CN.md").write_text(self.zh, encoding="utf-8")
        (self.root / "guide.md").write_text("# 标题与 中文\n\n## Same\n## Same\n\n```\n# Hidden\n```\n", encoding="utf-8")

    def errors(self):
        self.write_readmes()
        return "\n".join(check.check_root(self.root))

    def test_valid_fixture_ignores_unrelated_table_and_supports_chinese_anchor(self):
        self.assertEqual(self.errors(), "")

    def test_category_moved_but_flattened_order_unchanged(self):
        target = f"## {check.CATEGORY_HEADINGS[2][1]}\n\n| Tool | Description |\n| --- | --- |\n"
        line = "| [Tool 1](https://example.com/tool-1) | Description. |\n"
        self.zh = self.zh.replace(line, "").replace(target, target + line)
        self.assertIn("product links or order differ", self.errors())

    def test_missing_or_reordered_category(self):
        self.zh = self.zh.replace(check.CATEGORY_HEADINGS[1][1], "Other category")
        self.assertIn("categories missing", self.errors())

    def test_bad_row_format_and_empty_name(self):
        self.en = self.en.replace("[Tool 1]", "[]")
        self.assertIn("product links need a name", self.errors())
        self.en = self.en.replace(" | Description. |", " | Description. | extra |", 1)
        self.assertIn("two-column product row", self.errors())

    def test_empty_description(self):
        self.zh = self.zh.replace("| Description. |", "|  |", 1)
        self.assertIn("product description is empty", self.errors())

    def test_blank_or_text_between_product_rows_breaks_table(self):
        workbuddy = f"| [WorkBuddy]({check.WORKBUDDY_URL}) | Assistant. |"
        for interruption in ("\n", "\nNot part of the table.\n"):
            with self.subTest(interruption=repr(interruption)):
                original = self.en
                self.en = self.en.replace(workbuddy, interruption + workbuddy, 1)
                self.assertIn("product table must be continuous", self.errors())
                self.en = original

    def test_blank_lines_before_and_after_table_are_allowed(self):
        heading = f"## {check.CATEGORY_HEADINGS[0][0]}\n\n| Tool"
        self.en = self.en.replace(heading, heading.replace("\n\n|", "\n\n\n|"), 1)
        self.en = self.en.replace("| Assistant. |\n\n##", "| Assistant. |\n\n\n##", 1)
        self.assertEqual(self.errors(), "")

    def test_non_https_product_url(self):
        self.en = self.en.replace("https://example.com/tool-1", "http://example.com/tool-1")
        self.assertIn("must use HTTPS", self.errors())

    def test_credentials_and_common_tracking_or_affiliate_parameters(self):
        unsafe = (
            "https://user:secret@example.com/tool-1",
            "https://@example.com/tool-1",
            "https://example.com/tool-1?UTM_Source=news",
            "https://example.com/tool-1?%72ef=person",
            "https://example.com/tool-1?x=1;affiliate=person",
            "https://example.com/tool-1?fbclid=tracking",
        )
        for url in unsafe:
            with self.subTest(url=url):
                self.assertFalse(check.valid_url(url))
        self.assertTrue(check.valid_url("https://example.com/tool-1?lang=en"))

    def test_product_table_checks_secondary_and_description_links_without_echoing_secrets(self):
        secret = "https://user:secret@example.com/path?utm_source=tracking"
        self.en = self.en.replace("| Description. |", f"| See [official source]({secret}). |", 1)
        errors = self.errors()
        self.assertIn("without credentials, tracking parameters, or affiliate codes", errors)
        self.assertNotIn("secret", errors)
        self.en = self.en.replace(f"[official source]({secret})", secret)
        self.assertIn("without credentials", self.errors())

    def test_duplicate_url_normalizes_host_case_and_trailing_slash(self):
        self.en = self.en.replace("https://example.com/tool-2", "https://EXAMPLE.com/tool-1/")
        self.zh = self.zh.replace("https://example.com/tool-2", "https://EXAMPLE.com/tool-1/")
        self.assertIn("Duplicate primary product", self.errors())

    def test_featured_and_second_order(self):
        a = f"| [Baizhi]({check.FEATURED_URL}) · [Source]({check.FEATURED_SOURCE}) | Workbench. |\n"
        b = f"| [WorkBuddy]({check.WORKBUDDY_URL}) | Assistant. |\n"
        self.en = self.en.replace(a + b, b + a)
        self.assertIn("Baizhi Office and its source must be the first", self.errors())
        self.assertIn("WorkBuddy must be the second", self.errors())

    def test_broken_relative_path_and_fragment(self):
        self.en += "\n[missing](missing.md) [bad heading](guide.md#not-here)\n"
        errors = self.errors()
        self.assertIn("missing or out-of-repository relative link", errors)
        self.assertIn("missing heading anchor", errors)

    def test_duplicate_heading_and_fenced_heading(self):
        self.en += "\n[duplicate](guide.md#same-1) [hidden](guide.md#hidden)\n"
        errors = self.errors()
        self.assertEqual(errors.count("missing heading anchor"), 1)

    def test_missing_readme(self):
        (self.root / "README.md").unlink()
        self.assertIn("Both README.md", check.check_root(self.root)[0])


if __name__ == "__main__":
    unittest.main()
