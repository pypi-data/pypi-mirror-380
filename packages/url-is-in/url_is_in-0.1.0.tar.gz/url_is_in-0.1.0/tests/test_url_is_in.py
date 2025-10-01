from url_is_in import URLMatcher


def test_url_matcher():
    matcher = URLMatcher(list_of_urls=["http://www.example.com"], match_subdomains=True)

    assert matcher.is_in("http://example.com/foo"), "Invalid match"


def test_url_matcher_mode():
    urls = ["http://www.example.com", "https://github.com/commoncrawl"]
    needle = "http://example.com/foo"

    auto_matcher = URLMatcher(list_of_urls=urls, mode="auto")
    tuple_matcher = URLMatcher(list_of_urls=urls, mode="tuple")
    trie_matcher = URLMatcher(list_of_urls=urls, mode="trie")

    assert auto_matcher.is_in(needle), "Invalid match"
    assert tuple_matcher.is_in(needle), "Invalid match"
    assert trie_matcher.is_in(needle), "Invalid match"
