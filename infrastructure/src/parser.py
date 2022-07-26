import logging
from typing import Optional

import requests
from pydantic import ValidationError
from requests import JSONDecodeError
from requests.exceptions import ConnectionError

from infrastructure.config import GRAPHQL_QUERY, LEETCODE_API_URL
from infrastructure.src.db.models import Problem
from infrastructure.src.db.schemas import ProblemSchema

logger = logging.getLogger(__name__)


class LeetCodeParser:
    @classmethod
    def get_problem_data(cls, title: str) -> Optional[dict]:
        response = cls._make_request(Problem.to_slug(title))

        if response is None:
            return None

        if 'errors' in response:
            logger.error(f'Response errors: {response["errors"]}')
            return None

        problem_data = response['data']['question']

        try:
            return ProblemSchema.parse_obj(problem_data).dict()
        except ValidationError as err:
            logger.error(f'Invalid problem data: {problem_data}, error: {err}')

    @classmethod
    def _make_request(cls, slug: str) -> Optional[dict]:
        try:
            data = cls._get_request_data(slug)
            return requests.get(LEETCODE_API_URL, json=data).json()
        except (ConnectionError, JSONDecodeError) as err:
            logger.error(f'Error making request for slug "{slug}": {err}')

    @staticmethod
    def _get_request_data(slug: str) -> dict:
        return {
            'operationName': 'questionData',
            'variables': {'titleSlug': slug},
            'query': GRAPHQL_QUERY,
        }
