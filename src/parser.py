import logging
from typing import Optional

import pydantic
import requests
from requests.exceptions import ConnectionError
from problem import ProblemSchema

from models import Problem


class LeetCodeProblemDataParser:
    URL = 'https://leetcode.com/graphql'

    def __init__(self, graphql_query: str):
        self._graphql_query = graphql_query

    def get_problem_data(self, title: str) -> Optional[dict]:
        response = self._make_request(Problem.to_slug(title))

        if response is None:
            return None

        if 'errors' in response:
            logging.error('Response errors', response['errors'])
            return None

        try:
            problem_data = response['data']['question']
            return ProblemSchema.parse_obj(problem_data).dict()
        except pydantic.ValidationError:
            logging.error('TODO logging 3')

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
