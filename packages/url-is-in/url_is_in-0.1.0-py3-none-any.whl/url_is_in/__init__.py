"""Efficient URL matching against large whitelists and blacklists.

This package provides tools for checking if URLs are part of large sets of URLs
(blacklists or whitelists). It uses SURT (Sort-friendly URI Reordering
Transform) internally for normalized URL comparison and offers multiple matching
strategies optimized for different use cases.

The package automatically selects the most efficient matching algorithm based on
the size of the URL list, but also allows manual selection for fine-tuned control.

Example:
    Basic usage for URL matching:

    >>> matcher = URLMatcher(["https://example.com", "https://test.org"])
    >>> matcher.is_in("https://example.com/path")
    True
    >>> matcher.is_in("https://other.com")
    False

    Using SURT matching directly:

    >>> surt_matcher = SURTMatcher(["com,example)/", "org,test)/"])
    >>> surt_matcher.is_in("com,example)/path")
    True
"""

from typing import List, Literal

from surt import surt as convert_url_to_surt

from url_is_in.prefix_matcher import TrieMatcher, TupleMatcher

TRIE_MATCHER_THRESHOLD = 100

MatcherMode = Literal["auto", "trie", "tuple"]


class SURTMatcher:
    """Matcher for SURTs (Sort-friendly URI Reordering Transform).

    SURTMatcher provides efficient prefix matching against a list of SURT
    (Sort-friendly URI Reordering Transform) strings. It automatically selects
    the optimal matching algorithm based on the size of the SURT list.

    The matcher supports subdomain matching and offers three different matching
    modes: automatic selection, trie-based matching for large sets, and tuple-based
    matching for smaller sets.

    Attributes:
        list_of_surts: The processed list of SURT strings used for matching.
        prefix_matcher: The underlying matcher instance (TrieMatcher or TupleMatcher).

    Example:
        >>> surts = ["com,example)/", "org,test)/"]
        >>> matcher = SURTMatcher(surts)
        >>> matcher.is_in("com,example)/path")
        True
        >>> matcher.is_in("com,other)/")
        False
    """

    def __init__(
        self,
        list_of_surts: List[str],
        match_subdomains: bool = True,
        mode: MatcherMode = "auto",
    ):
        """Initialize the SURT matcher.

        Args:
            list_of_surts: List of SURT strings to match against. These should be
                properly formatted SURT strings (e.g., 'com,example)/').
            match_subdomains: If True, automatically adds subdomain matching patterns
                for SURT strings that end with ')/' (domain-only patterns).
            mode: Matching algorithm to use:
                - "auto": Automatically select based on list size (default)
                - "trie": Use trie-based matching (efficient for large lists)
                - "tuple": Use tuple-based matching (efficient for small lists)

        Raises:
            ValueError: If an invalid mode is specified.

        Example:
            >>> matcher = SURTMatcher(["com,example)/"], match_subdomains=True)
            >>> # Will also match subdomains like 'com,example,www)/'
        """
        self.list_of_surts = list_of_surts

        if match_subdomains:
            # also match subdomains if no path or query is provided
            self.list_of_surts += [item_surt[:-2] + "," for item_surt in self.list_of_surts if item_surt.endswith(")/")]

        if mode == "auto":
            matcher_cls = TrieMatcher if len(self.list_of_surts) > TRIE_MATCHER_THRESHOLD else TupleMatcher
        elif mode == "trie":
            matcher_cls = TrieMatcher
        elif mode == "tuple":
            matcher_cls = TupleMatcher
        else:
            raise ValueError(f"Invalid matcher mode: {mode} (available: auto, trie, tuple)")

        self.prefix_matcher = matcher_cls(prefixes=list_of_surts)

    def is_in(self, surt: str) -> bool:
        """Check if a SURT string matches any of the configured patterns.

        Args:
            surt: The SURT string to check for matches. Should be a properly
                formatted SURT string.

        Returns:
            True if the input SURT starts with at least one of the SURT patterns
            from the configured list, False otherwise.

        Example:
            >>> matcher = SURTMatcher(["com,example)/"])
            >>> matcher.is_in("com,example)/path?query=value")
            True
            >>> matcher.is_in("com,other)/path")
            False
        """
        return self.prefix_matcher.matches(surt)


class URLMatcher:
    """URL matcher with automatic SURT conversion.

    URLMatcher provides a convenient interface for matching URLs against a list
    of reference URLs. It automatically converts all URLs to SURT format internally
    for efficient and normalized matching.

    This class is ideal when you want to work directly with URLs rather than
    dealing with SURT conversion manually. It supports all the same matching
    modes and subdomain options as SURTMatcher.

    Attributes:
        surt_matcher: The underlying SURTMatcher instance that performs the actual matching.

    Example:
        >>> urls = ["https://example.com", "https://test.org/path"]
        >>> matcher = URLMatcher(urls, match_subdomains=True)
        >>> matcher.is_in("https://www.example.com/some/path")
        True
        >>> matcher.is_in("https://other.com")
        False
    """

    def __init__(self, list_of_urls: List[str], match_subdomains: bool = True, mode: MatcherMode = "auto"):
        """Initialize the URL matcher.

        Args:
            list_of_urls: List of URLs to match against. These can be any valid URLs
                including different protocols, domains, paths, and query parameters.
            match_subdomains: If True, automatically enables subdomain matching for
                domain-only URLs (e.g., 'https://example.com' will also match
                'https://www.example.com').
            mode: Matching algorithm to use:
                - "auto": Automatically select based on list size (default)
                - "trie": Use trie-based matching (efficient for large lists)
                - "tuple": Use tuple-based matching (efficient for small lists)

        Example:
            >>> matcher = URLMatcher(["https://example.com", "https://test.org/specific/path"])
            >>> # Will match subdomains and paths under the specified URLs
        """
        self.surt_matcher = SURTMatcher(
            list_of_surts=[convert_url_to_surt(item_url) for item_url in list_of_urls],
            match_subdomains=match_subdomains,
            mode=mode,
        )

    def is_in(self, url: str) -> bool:
        """Check if a URL matches any of the configured URL patterns.

        This method automatically converts the input URL to SURT format and
        checks it against the configured list of URL patterns.

        Args:
            url: The URL to check for matches. Can be any valid URL string.

        Returns:
            True if the input URL matches any of the configured URL patterns,
            False otherwise.

        Example:
            >>> matcher = URLMatcher(["https://example.com"])
            >>> matcher.is_in("https://example.com/any/path?query=value")
            True
            >>> matcher.is_in("https://www.example.com/path")  # if match_subdomains=True
            True
            >>> matcher.is_in("https://different.com")
            False
        """
        return self.surt_matcher.is_in(
            surt=convert_url_to_surt(url),
        )
