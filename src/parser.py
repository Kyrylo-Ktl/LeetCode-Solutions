from typing import Optional

import requests
from requests.exceptions import ConnectionError

from problem import Problem


class LeetCodeProblemParser:
    URL = 'https://leetcode.com/graphql'

    def __init__(self, graphql_query: str):
        self._graphql_query = graphql_query

    def get_problem(self, slug: str) -> Optional[Problem]:
        response = self._make_request(slug)

        if response is None:
            return None

        if 'errors' in response:
            print('Response errors', response['errors'])
            return None

        problem = Problem.parse_obj(response['data']['question'])
        return problem

    def _make_request(self, slug: str) -> Optional[dict]:
        data = {
            'operationName': 'questionData',
            'variables': {'titleSlug': slug},
            'query': self._graphql_query,
        }
        try:
            return requests.get(self.URL, json=data).json()
        except ConnectionError:
            return None
