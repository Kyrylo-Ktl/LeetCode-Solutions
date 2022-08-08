import re


class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    IPv4_PATTERN = re.compile(rf'{IPv4}\.{IPv4}\.{IPv4}\.{IPv4}')

    IPv6 = r'([0-9a-fA-F]{1,4})'
    IPv6_PATTERN = re.compile(rf'{IPv6}\:{IPv6}\:{IPv6}\:{IPv6}\:{IPv6}\:{IPv6}\:{IPv6}\:{IPv6}')

    def validIPAddress(self, address: str) -> str:
        return {
            self.IPv4_PATTERN.fullmatch(address) is not None: 'IPv4',
            self.IPv6_PATTERN.fullmatch(address) is not None: 'IPv6',
        }.get(True, 'Neither')
