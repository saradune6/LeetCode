class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s)
        wordSet = set(wordDict)

        # Step 1: DP
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for w in wordSet:
                if s.startswith(w, i) and dp[i + len(w)]:
                    dp[i] = True
                    break

        # Step 2: DFS + Memo
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            res = []
            for w in wordSet:
                if s.startswith(w, i) and dp[i + len(w)]:
                    if i + len(w) == n:
                        res.append(w)
                    else:
                        for tail in dfs(i + len(w)):
                            res.append(w + " " + tail)

            memo[i] = res
            return res

        return dfs(0)
