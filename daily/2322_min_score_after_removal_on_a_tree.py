from typing import List

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        '''
        1. Create an adjancency matrix
        2. Start from every node,
                (We need to remove two edges)
                a. Remove edge from curr to parent
                b. Remove another edge anywhere from the tree starting from curr. (Sub problem)
                c. Calculate the XOR of the 3 parts, 
                   ideally a^b= c => b^c = a, 
                   so if you find total XOR and XORs of two subtrees, third is just 
                   total^XOR1^XOR2

        '''
        adj = defaultdict(list)

        n = len(nums)
        for s, t in edges:
            adj[s].append(t)
            adj[t].append(s)

        min_score=float('inf')
        total_xor = 0
        for n in nums:
            total_xor^=n

        def calc(i, j, k):
            return max(i, j, k) - min(i, j, k)
        
        def second_split(child, parent, first_xor, first_tree_root):
            second_xor = nums[child]
            for neighbor in adj[child]:
                if neighbor == parent:
                    continue
                second_xor ^= second_split(neighbor, child, first_xor, first_tree_root)
            if parent == first_tree_root:
                return second_xor
            third_xor = total_xor^first_xor^second_xor
            nonlocal min_score
            min_score = min(min_score, calc(first_xor, second_xor, third_xor))
            return second_xor

        def first_split(child, parent):
            first_xor = nums[child]
            for neighbor in adj[child]:
                if neighbor == parent:
                    continue
                first_xor ^= first_split(neighbor, child)
            
            for neighbor in adj[child]:
                if neighbor == parent:
                    second_split(neighbor, child, first_xor, child)
                    
            return first_xor
        
        first_split(0, -1)
        
        return min_score