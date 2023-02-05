class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        left_border = t - 3000

        for idx, i in enumerate(self.requests):
            if i < left_border:
                pass
            else:
                return len(self.requests) - idx
                