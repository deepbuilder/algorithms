'''https://leetcode.com/problems/maximum-score-from-removing-substrings/'''
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        '''
        s = "cdbcbbaaabab", x = 4, y = 5
        1. Greedily remove high value pair from the string
            a, Use stack to handle recursively removing the pair
        2. Remove the others until no more is found
        3. Sum the scores from 1 & 2
        '''
        def remove(s, first, sec, v):
            stack = []
            total = 0
            for i in range(len(s)):
                if stack and stack[-1] == first and s[i] == sec:
                    total+=v
                    stack.pop()
                else:
                    stack.append(s[i])
            return ''.join(stack), total


        if x > y:
            s, score1 = remove(s, 'a', 'b', x)
            _, score2 = remove(s, 'b', 'a', y)
        
        else:
            s, score1 = remove(s, 'b', 'a', y)
            _, score2 = remove(s, 'a', 'b', x)
        
        return score1 + score2
