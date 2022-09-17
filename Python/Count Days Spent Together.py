from datetime import date


class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def countDaysTogether(self, arrive_alice: str, leave_alice: str, arrive_bob: str, leave_bob: str) -> int:
        start = max(self.to_date(arrive_alice), self.to_date(arrive_bob))
        end = min(self.to_date(leave_alice), self.to_date(leave_bob))
        return max((end - start).days + 1, 0)

    @staticmethod
    def to_date(month_day: str) -> date:
        return date(2001, *map(int, month_day.split('-')))
