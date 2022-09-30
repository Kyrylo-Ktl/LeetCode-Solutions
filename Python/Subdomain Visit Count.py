from collections import defaultdict
from typing import List


class Solution:
    """
    Time:   O(n*k)
    Memory: O(n*k)

    where k - maximum number of subdomains
    """

    def subdomainVisits(self, domains: List[str]) -> List[str]:
        ans = defaultdict(int)

        for domain in domains:
            count, domain = domain.split()
            count = int(count)

            sub_domains = domain.split('.')
            for i in range(len(sub_domains)):
                ans['.'.join(sub_domains[i:])] += count

        return ['{} {}'.format(cnt, dom) for dom, cnt in ans.items()]
