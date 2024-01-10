class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        answer = ""
        rows = [[] for _ in range(numRows)] # [[], [], [], []]
        curr = 0
        step = 1
        for c in s:
            if curr == 0:
                rows[curr].append(c)
                step = 1
                curr += step
            elif curr == numRows - 1:
                rows[curr].append(c)
                step = -1
                curr += step
            else:
                rows[curr].append(c)
                curr += step
        print(rows)
        for row in rows:
            answer += "".join(map(str, row))
        return answer
