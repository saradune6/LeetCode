class Solution:
    def unhappyFriends(self, n, preferences, pairs):
        # partner[x] = person paired with x
        partner = [0] * n
        for x, y in pairs:
            partner[x] = y
            partner[y] = x

        # rank[x][y] = preference order of y for x
        rank = [[0] * n for _ in range(n)]
        for i in range(n):
            for j, p in enumerate(preferences[i]):
                rank[i][p] = j

        unhappy = 0

        for x in range(n):
            y = partner[x]
            for u in preferences[x]:
                # stop when we reach current partner
                if u == y:
                    break
                v = partner[u]
                # check mutual preference
                if rank[u][x] < rank[u][v]:
                    unhappy += 1
                    break

        return unhappy
