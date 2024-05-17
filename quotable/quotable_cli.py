import argparse

from .quotable import PyQuotable


def parse_args():

    parser = argparse.ArgumentParser(
        description="A CLI tool for the quotable api")
    subparsers = parser.add_subparsers(
        dest="command", help="Available Commands")

    # for fetching random quote:
    get_random_quote = subparsers.add_parser(
        "get-random-quote", help="Get random quotes.")
    get_random_quote.add_argument("--limit", type=int, help="Number of random quotes to retrieve; default: 1, min: 1, max: 50")
    get_random_quote.add_argument("--max-length", type=int, help="The maximum length in characters ( can be combined with --min-length )")
    get_random_quote.add_argument("--min-length", type=int, help="The minimum length in characters ( can be combined with --max-length )")
    get_random_quote.add_argument("--tags",
                                  type=str,
                                  help="""Get a random quote with specific tag(s).
                                         Tags can be provided as a comma-separated (,) string for AND conditions or a pipe-separated (|) string for OR conditions.
                                         Tag names are not case-sensitive and multi-word tags can be in kebab-case or space-separated format.""")
    get_random_quote.add_argument("--author", type=str, help="Get random quotes by name of author(s). For multiple authors, use a pipe-separated (|) string.")

    # for fetching quotes matching a given query:
    get_quote = subparsers.add_parser("get-quote", help="Get all quotes matching a given query. By default, this will return a paginated list of all quotes.")
    get_quote.add_argument("--limit", type=int, help="Number of random quotes to retrieve; default: 20, min: 1, max: 150")
    get_quote.add_argument("--max-length", type=int, help="The maximum length in characters ( can be combined with --min-length )")
    get_quote.add_argument("--min-length", type=int, help="The minimum length in characters ( can be combined with --max-length )")
    get_quote.add_argument("--tags",
                           type=str,
                           help="""Get a random quote with specific tag(s).
                                  Tags can be provided as a comma-separated (,) string for AND conditions or a pipe-separated (|) string for OR conditions.
                                  Tag names are not case-sensitive and multi-word tags can be in kebab-case or space-separated format.""")
    get_quote.add_argument("--author", type=str, help="Get random quotes by name of author(s). For multiple authors, use a pipe-separated (|) string.")
    get_quote.add_argument("--sort-by", "-s", type=str, choices=["dateAdded", "dateModified", "author", "content"], help="Default: 'dateAdded'")
    get_quote.add_argument("--order", "-o", type=str, choices=["asc", "desc"], help="Specify the sorting order. Default order: For string fields, it's ascending; for number and date fields.")
    get_quote.add_argument("--page", type=int, help="Page number for pagination. Min: 1   Default: 1")

    # for fetching quote by a specific id
    get_quote_by_id = subparsers.add_parser("get-quote-by-id", help="Get a quote by its ID.")
    get_quote_by_id.add_argument("--id", type=str, required=True, help="Provide ID of the quote")

    # search for quotes by keywords, content, and/or author name.
    search_quotes = subparsers.add_parser("search-quote", help="Search for quotes by keywords, content, and/or author name.")
    search_quotes.add_argument("--query", "-q", type=str, required=True, help="Specify the search string. The query can be wrapped in single-quotes to search for an exact phrase.")
    search_quotes.add_argument("--fields", "-f", type=str, help="Specify fields to search as a comma-separated list. Supported fields: 'content', 'author', 'tags'. By default, searches all fields simultaneously.")
    search_quotes.add_argument("--fuzzy-max-edits", type=int, help="Max single-character edits to match the search term. Min:0; Max: 2; Default: 0(which disables fuzzy matching)")
    search_quotes.add_argument("--fuzzy-max-expansions", type=int, help="Maximum variations to generate and search for per token when fuzzy search is enabled. Min: 0; Max: 150; Default: 50")
    search_quotes.add_argument("--page", type=int, help="Page number for pagination. Min: 1; Default: 1")
    search_quotes.add_argument("--limit", type=int, help="The maximum number of results per page. Min: 0; Max: 150; Default: 20")

    # for fetching authors matching a given query

    get_author = subparsers.add_parser("get-author", help="Get all authors matching a given query. By default, this will return a paginated details of all author.")
    get_author.add_argument("--slug", type=str, help="Filter authors by one or more slugs. Use a pipe-separated list for multiple slugs.")
    get_author.add_argument("--sort-by", "-s", type=str, choices=["dateAdded", "dateModified", "name", "quoteCount"], help="Default: 'name'")
    get_author.add_argument("--order", "-o", type=str, choices=["asc", "desc"], help="Specify the sorting order. Default order: For string fields, it's ascending; for number and date fields.")
    get_author.add_argument("--limit", type=int, help="The maximum number of results per page. Min: 0; Max: 150; Default: 20")
    get_author.add_argument("--page", type=int, help="Page number for pagination. Min: 1   Default: 1")

    # search for authors by name
    search_author = subparsers.add_parser("search-author", help="Search for authors by name")
    search_author.add_argument("--query", "-q", type=str, required=True, help="Specify the search string.")
    search_author.add_argument("--autocomplete", type=bool, help="Enables autocomplete matching. Default: True")
    search_author.add_argument("--match-threshold", type=int, help="Sets the minimum number of search terms(words) that must match for an author to be included. Min: 1; Max: 3; Default: 2")
    search_author.add_argument("--page", type=int, help="Page number for pagination. Min: 1; Default: 1")
    search_author.add_argument("--limit", type=int, help="The maximum number of results per page. Min: 0; Max: 150; Default: 20")

    # for fetching quote by a specific id
    get_author_by_id = subparsers.add_parser("get-author-by-id", help="Get a author by its ID.")
    get_author_by_id.add_argument("--id", type=str, required=True, help="Provide ID of the author.")

    # get list of available tags
    get_tags = subparsers.add_parser("get-tags", help="Get a list of all tags")
    get_tags.add_argument("--sort_by", "-s", type=str, choices=["dateAdded", "dateModified", "name", "quoteCount"], help="Default: 'name'")
    get_tags.add_argument("--order", "-o", type=str, choices=["asc", "desc"], help="Specify the sorting order. Default order: For string fields, it's ascending; for number and date fields.")

    return parser.parse_args()


def main():
    args = parse_args()
    pyquotable = PyQuotable()

    if args.command == "get-random-quote":
        result = pyquotable.fetch_random_quote(
            limit=args.limit,
            min_len=args.min_length,
            max_len=args.max_length,
            tags=args.tags,
            author=args.author
        )
        print(result)

    elif args.command == "get-quote":
        result = pyquotable.fetch_quote(
            min_len=args.min_length,
            max_len=args.max_length,
            tags=args.tags,
            author=args.author,
            sort_by=args.sort_by,
            order=args.order,
            limit=args.limit,
            page=args.page
        )
        print(result)

    elif args.command == "get-quote-by-id":
        result = pyquotable.get_quote_by_id(
            quote_id=args.id
        )
        print(result)

    elif args.command == "search-quote":
        result = pyquotable.search_quotes(
            query=args.query,
            fields=args.fields,
            fuzzy_max_edits=args.fuzzy_max_edits,
            fuzzy_max_expansions=args.fuzzy_max_expansions,
            page=args.page,
            limit=args.limit
        )
        print(result)

    elif args.command == "get-authors":
        result = pyquotable.get_authors(
            slug=args.slug,
            sort_by=args.sort_by,
            order=args.order,
            limit=args.limit,
            page=args.page
        )
        print(result)

    elif args.command == "search-author":
        result = pyquotable.search_author(
            query=args.query,
            autocomplete=args.autocomplete,
            match_threshold=args.match_threshold,
            page=args.page,
            limit=args.limit
        )
        print(result)

    elif args.command == "get-author-by-id":
        result = pyquotable.fetch_author_by_id(
            author_id=args.id
        )
        print(result)

    elif args.command == "get-tags":
        result = pyquotable.fetch_tags(
            args.sort_by,
            args.order
        )
        print(result)
    else:
        print("No valid command provided. Use --help for usage information.")
        return


if __name__ == "__main__":
    main()
