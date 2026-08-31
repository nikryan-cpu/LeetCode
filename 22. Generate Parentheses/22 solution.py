class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtracking(open, close, tmp):
            if open == n and close == open:
                result.append(tmp)

            if open < n:
                backtracking(open + 1, close, tmp + "(")

            if close < open:
                backtracking(open, close + 1, tmp + ")")

        backtracking(0, 0, "")
        
        return result