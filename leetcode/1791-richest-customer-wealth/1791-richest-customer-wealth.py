class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_of_sum = 0
        for i in range(len(accounts)):
            wealth = 0 

            for j in range (len(accounts[i])):
                wealth += accounts[i][j]

                if wealth >= max_of_sum:
                    max_of_sum = wealth
                
        return max_of_sum 