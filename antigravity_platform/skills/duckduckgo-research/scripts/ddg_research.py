"""
DuckDuckGo Web Search & Page Content Collector CLI
Enables querying DuckDuckGo, retrieving search results, and extracting clean readable text.
"""

import sys
import os
import argparse
import json
import re
import urllib.parse
from html import unescape
from html.parser import HTMLParser

try:
    import requests
except ImportError:
    requests = None


class CleanTextExtractor(HTMLParser):
    """Extracts readable article/body text while filtering code, styles, and navigation chrome."""
    def __init__(self):
        super().__init__()
        self.text_chunks = []
        self.ignore_tags = {'script', 'style', 'noscript', 'header', 'footer', 'nav', 'svg', 'aside', 'head'}
        self.tag_stack = []

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag.lower())

    def handle_endtag(self, tag):
        tag_lower = tag.lower()
        if tag_lower in self.tag_stack:
            self.tag_stack.remove(tag_lower)
        if tag_lower in {'p', 'div', 'h1', 'h2', 'h3', 'h4', 'li', 'article', 'section', 'tr'}:
            self.text_chunks.append('\n')

    def handle_data(self, data):
        if any(tag in self.ignore_tags for tag in self.tag_stack):
            return
        text = data.strip()
        if text:
            self.text_chunks.append(text + ' ')

    def get_text(self):
        raw = ''.join(self.text_chunks)
        cleaned = re.sub(r'[ \t]+', ' ', raw)
        cleaned = re.sub(r'\n\s*\n+', '\n\n', cleaned)
        return cleaned.strip()


def parse_ddg_html(html_text: str, max_results: int = 10):
    title_links = re.findall(
        r'<a[^>]*class="[^"]*result__a[^"]*"[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
        html_text,
        re.DOTALL
    )
    snippets = re.findall(
        r'<a[^>]*class="[^"]*result__snippet[^"]*"[^>]*>(.*?)</a>',
        html_text,
        re.DOTALL
    )

    results = []
    limit = min(len(title_links), max_results)
    for i in range(limit):
        raw_url, raw_title = title_links[i]
        snippet_text = snippets[i] if i < len(snippets) else ''

        clean_title = unescape(re.sub(r'<[^>]+>', '', raw_title).strip())
        clean_snippet = unescape(re.sub(r'<[^>]+>', '', snippet_text).strip())

        if 'uddg=' in raw_url:
            parsed = urllib.parse.urlparse(raw_url)
            qs = urllib.parse.parse_qs(parsed.query)
            target_url = urllib.parse.unquote(qs.get('uddg', [raw_url])[0])
        else:
            target_url = raw_url

        results.append({
            'title': clean_title,
            'link': target_url,
            'snippet': clean_snippet
        })
    return results


def parse_ddg_lite(html_text: str, max_results: int = 10):
    # Matches on lite.duckduckgo.com
    # Table rows contain result links and snippets
    # link: <a rel="nofollow" href="...">Title</a>
    # snippet: <td class="result-snippet">...</td>
    links = re.findall(r'<a\s+rel="nofollow"\s+href="([^"]+)"[^>]*>(.*?)</a>', html_text, re.DOTALL)
    snippets = re.findall(r'<td\s+class="result-snippet"[^>]*>(.*?)</td>', html_text, re.DOTALL)

    results = []
    limit = min(len(links), max_results)
    for i in range(limit):
        raw_url, raw_title = links[i]
        snippet_text = snippets[i] if i < len(snippets) else ''

        clean_title = unescape(re.sub(r'<[^>]+>', '', raw_title).strip())
        clean_snippet = unescape(re.sub(r'<[^>]+>', '', snippet_text).strip())

        if 'uddg=' in raw_url:
            parsed = urllib.parse.urlparse(raw_url)
            qs = urllib.parse.parse_qs(parsed.query)
            target_url = urllib.parse.unquote(qs.get('uddg', [raw_url])[0])
        else:
            target_url = raw_url

        results.append({
            'title': clean_title,
            'link': target_url,
            'snippet': clean_snippet
        })
    return results


def search_duckduckgo(query: str, max_results: int = 10, use_browser: bool = False):
    """Searches DuckDuckGo with fallback mechanisms."""
    if use_browser:
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto(f"https://duckduckgo.com/?q={urllib.parse.quote(query)}", wait_until="networkidle", timeout=20000)
                html = page.content()
                browser.close()
                res = parse_ddg_html(html, max_results)
                if res:
                    return res
        except Exception:
            pass

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    # Attempt 1: html endpoint
    try:
        if requests is not None:
            r = requests.post('https://html.duckduckgo.com/html/', data={'q': query}, headers=headers, timeout=12)
            if r.status_code == 200:
                results = parse_ddg_html(r.text, max_results)
                if results:
                    return results
    except Exception:
        pass

    # Attempt 2: lite endpoint fallback
    try:
        if requests is not None:
            r = requests.post('https://lite.duckduckgo.com/lite/', data={'q': query}, headers=headers, timeout=12)
            if r.status_code == 200:
                results = parse_ddg_lite(r.text, max_results)
                if results:
                    return results
    except Exception:
        pass

    # Attempt 3: urllib fallback
    try:
        req = urllib.request.Request(
            'https://html.duckduckgo.com/html/',
            data=urllib.parse.urlencode({'q': query}).encode('utf-8'),
            headers=headers
        )
        with urllib.request.urlopen(req, timeout=12) as response:
            html = response.read().decode('utf-8', errors='ignore')
            results = parse_ddg_html(html, max_results)
            if results:
                return results
    except Exception:
        pass

    return []


def extract_page_text(url: str, use_browser: bool = False, timeout: int = 15):
    """Fetches a URL and returns clean extracted text."""
    if use_browser:
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page(
                    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                )
                page.goto(url, timeout=timeout * 1000, wait_until='domcontentloaded')
                content = page.content()
                browser.close()
                parser = CleanTextExtractor()
                parser.feed(content)
                return parser.get_text()
        except Exception as e:
            return f"[Error fetching with browser: {e}]"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }
    try:
        if requests is not None:
            resp = requests.get(url, headers=headers, timeout=timeout)
            html_text = resp.text
        else:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                html_text = r.read().decode('utf-8', errors='ignore')

        parser = CleanTextExtractor()
        parser.feed(html_text)
        return parser.get_text()
    except Exception as e:
        return f"[Error fetching page content: {e}]"


def main():
    parser = argparse.ArgumentParser(description="DuckDuckGo Search and Page Content Collector")
    parser.add_argument("--query", "-q", type=str, help="Search query")
    parser.add_argument("--url", "-u", type=str, help="Directly extract text from a specific URL")
    parser.add_argument("--max-results", "-n", type=int, default=5, help="Maximum search results to return (default 5)")
    parser.add_argument("--fetch", "-f", action="store_true", help="Fetch and extract text content from the top results")
    parser.add_argument("--browser", "-b", action="store_true", help="Use headless Playwright browser")
    parser.add_argument("--output", "-o", type=str, help="Output file (.json or .md)")
    parser.add_argument("--json", action="store_true", help="Output JSON format")

    args = parser.parse_args()

    if not args.query and not args.url:
        parser.error("Either --query or --url must be provided.")

    # Direct URL extraction mode
    if args.url:
        print(f"Fetching URL: {args.url} ...", file=sys.stderr)
        content = extract_page_text(args.url, use_browser=args.browser)
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Saved content to {args.output}")
        else:
            print(content)
        return

    # Search mode
    results = search_duckduckgo(args.query, args.max_results, use_browser=args.browser)

    if args.fetch:
        for idx, item in enumerate(results, start=1):
            target_url = item.get('link')
            if target_url and target_url.startswith('http'):
                print(f"[{idx}/{len(results)}] Fetching content from: {target_url} ...", file=sys.stderr)
                content = extract_page_text(target_url, use_browser=args.browser)
                # Truncate content to first 3000 chars for clean context
                item['content'] = content[:3000] + ('\n[...truncated...]' if len(content) > 3000 else '')
            else:
                item['content'] = ""

    # Output formatting
    if args.json or (args.output and args.output.endswith('.json')):
        out_str = json.dumps(results, indent=2, ensure_ascii=False)
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(out_str)
            print(f"Saved JSON results to {args.output}")
        else:
            print(out_str)
    else:
        lines = [f"# DuckDuckGo Research: \"{args.query}\"\n"]
        for idx, item in enumerate(results, start=1):
            lines.append(f"### {idx}. {item['title']}")
            lines.append(f"- **URL**: {item['link']}")
            lines.append(f"- **Snippet**: {item['snippet']}\n")
            if 'content' in item and item['content']:
                quoted = '\n> '.join(item['content'].split('\n'))
                lines.append(f"> **Extracted Content:**\n> {quoted}\n")
            lines.append("")

        out_str = '\n'.join(lines)
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(out_str)
            print(f"Saved Markdown report to {args.output}")
        else:
            print(out_str)


if __name__ == '__main__':
    main()
