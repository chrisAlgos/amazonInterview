class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        by_user = defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            by_user[u].append(w)

        cnt = Counter()
        for x in by_user.values():
            cnt += Counter(set(combinations(x, 3)))

        return min(cnt, key=lambda k: (-cnt[k], k))
