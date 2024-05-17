import requests
import json


class PyQuotable:

    base_url = "https://api.quotable.io/"

    @staticmethod
    def construct_query_params(**kwargs):
        query_params = {}

        for key, value in kwargs.items():
            if value is not None:
                query_params[key] = value

        return query_params

    def fetch_random_quote(self,
                           limit=None,
                           min_len=None,
                           max_len=None,
                           tags=None,
                           author=None):

        url = f"{PyQuotable.base_url}quotes/random/"
        query = PyQuotable.construct_query_params(limit=limit,
                                                  minLength=min_len,
                                                  maxLength=max_len,
                                                  tags=tags,
                                                  author=author)

        try:
            response = requests.get(url, params=query)
            json_response = response.json()
            formatted_json = json.dumps(json_response, indent=4)
            return formatted_json
        except requests.RequestException as e:
            print("Error fetching quote:\n", e)
        except json.JSONDecodeError as e:
            print("Error decoding JSON:\n", e)

    def fetch_quote(self,
                    min_len=None,
                    max_len=None,
                    tags=None,
                    author=None,
                    sort_by=None,
                    order=None,
                    limit=20,
                    page=1):

        url = f"{PyQuotable.base_url}quotes"
        query = PyQuotable.construct_query_params(minLength=min_len,
                                                  maxLength=max_len,
                                                  tags=tags,
                                                  author=author,
                                                  sortBy=sort_by,
                                                  order=order,
                                                  limit=limit,
                                                  page=page)

        try:
            response = requests.get(url, params=query)
            json_response = response.json()
            formatted_json = json.dumps(json_response, indent=4)
            return formatted_json
        except requests.RequestException as e:
            print("Error fetching quotes:", e)
            return None
        except json.JSONDecodeError as e:
            print("Error decoding JSON:\n", e)
            return None

    def fetch_quote_by_id(self, quote_id=None):

        if quote_id is None:
            print("No quote id provided")
            return None

        url = f"{PyQuotable.base_url}quotes/{quote_id}"

        try:
            response = requests.get(url)
            json_response = response.json()
            return json.dumps(json_response, indent=4)
        except requests.RequestException as e:
            print("Error fetching quotes:\n", e)
            return None
        except json.JSONDecodeError as e:
            print("Error decoding JSON:\n", e)
            return None

    def search_quotes(self,
                      query=None,
                      fields=None,
                      fuzzy_max_edits=None,
                      fuzzy_max_expansions=None,
                      limit=None,
                      page=None):

        if query is None:
            print("Missing required parameter: 'query'")
            return None

        url = f"{PyQuotable.base_url}search/quotes"
        query = PyQuotable.construct_query_params(query=query,
                                                  fields=fields,
                                                  fuzzyMaxEdits=fuzzy_max_edits,
                                                  fuzzyMaxExpansions=fuzzy_max_expansions,
                                                  limit=limit,
                                                  page=page)

        try:
            response = requests.get(url, params=query)
            json_response = response.json()
            formatted_json = json.dumps(json_response, indent=4)
            return formatted_json
        except requests.RequestException as e:
            print("Error fetching quotes:", e)
            return None
        except json.JSONDecodeError as e:
            print("Error decoding JSON:\n", e)
            return None

    def fetch_authors(self,
                      slug=None,
                      sort_by=None,
                      order=None,
                      limit=None,
                      page=None):

        url = f"{PyQuotable.base_url}quotes"
        query = PyQuotable.construct_query_params(slug=slug,
                                                  sortBy=sort_by,
                                                  order=order,
                                                  limit=limit,
                                                  page=page)

        try:
            response = requests.get(url, params=query)
            json_response = response.json()
            formatted_json = json.dumps(json_response, indent=4)
            return formatted_json
        except requests.RequestException as e:
            print("Error fetching quotes:\n", e)
            return None
        except json.JSONDecodeError as e:
            print("Error decoding JSON:\n", e)
            return None

    def fetch_author_by_id(self, author_id=None):
        if author_id is None:
            print("No author id provided")
            return None
        url = f"{PyQuotable.base_url}authors/{author_id}"

        try:
            response = requests.get(url)
            json_response = response.json()
            return json.dumps(json_response, indent=4)
        except requests.RequestException as e:
            print("Error fetching quotes:\n", e)
            return None
        except json.JSONDecodeError as e:
            print("Error decoding JSON:\n", e)
            return None

    def search_authors(self,
                       query=None,
                       autocomplete=None,
                       match_threshold=None,
                       limit=None,
                       page=None):

        if query is None:
            print("Missing required parameter: 'query'")
            return None

        url = f"{PyQuotable.base_url}search/authors"
        query = PyQuotable.construct_query_params(query=query,
                                                  autocomplete=autocomplete,
                                                  matchThreshold=match_threshold,
                                                  limit=limit,
                                                  page=page)

        try:
            response = requests.get(url, params=query)
            json_response = response.json()
            formatted_json = json.dumps(json_response, indent=4)
            return formatted_json
        except requests.RequestException as e:
            print("Error fetching quotes:", e)
            return None
        except json.JSONDecodeError as e:
            print("Error decoding JSON:\n", e)
            return None

    def fetch_tags(self,
                   sort_by=None,
                   order=None):
        url = f"{PyQuotable.base_url}tags"
        query = PyQuotable.construct_query_params(sortBy=sort_by,
                                                  order=order)

        try:
            response = requests.get(url, params=query)
            json_response = response.json()
            return json.dumps(json_response, indent=4)
        except requests.RequestException as e:
            print("Error fetching quotes:\n", e)
            return None
        except json.JSONDecodeError as e:
            print("Error decoding JSON:\n", e)
            return None
