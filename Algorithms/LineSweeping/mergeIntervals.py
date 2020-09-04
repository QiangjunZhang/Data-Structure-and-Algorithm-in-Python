class MergeIntervals:
    def __init__(self, content = []):
        self.intervals = content

    def merge(self):
        """
        line sweeping method, record events: (signal, guide)
        """
        events = []
        for left, right in self.intervals:
            events.append((left, -1))
            events.append((right, 1))
        events.sort()

        merged = []
        for pos, guide in events:
            if guide > 0 and len(merged) > 1 and merged[-1][1] < 0 and merged[-2][1] < 0:
                merged.pop()
            else:
                merged.append((pos, guide))

        result = []
        for i in range(0, len(merged), 2):
            result.append([merged[i][0], merged[i + 1][0]])
        return result


