import re
from collections import defaultdict
from typing import List


class Solution:
    """
    Time:   O(n*k)
    Memory: O(n*k)

    where k - maximum number of files in one path
    """

    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicates = defaultdict(list)

        for path in paths:
            path, files = path.split(' ', 1)
            for file in files.split():
                filename, content, _ = re.split(r'[\(\)]', file)
                duplicates[content].append(path + '/' + filename)

        return [p for p in duplicates.values() if len(p) > 1]
