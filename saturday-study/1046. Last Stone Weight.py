class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1 :
            fir_lgest = max(stones)
            stones.remove(fir_lgest)

            sec_lgest = max(stones)
            stones.remove(sec_lgest)

            if fir_lgest != sec_lgest:
                stones.append(abs(fir_lgest - sec_lgest))
                
        if len(stones) == 0:
            return 0
        else:
            return stones[0]