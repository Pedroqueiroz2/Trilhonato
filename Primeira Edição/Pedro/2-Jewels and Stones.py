class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cont = 0
        s = set(jewels)
        for stone in stones:
            if stone in s:
                cont += 1
        print(cont)
        return cont


solution = Solution()
jewels = "aA"
stones = "aAAbbbb"
