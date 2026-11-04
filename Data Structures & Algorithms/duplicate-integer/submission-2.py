class Solution:
    def hasDuplicate(self, num: List[int]) -> bool:
      seen=set()
      for i in num:
        if i in seen:
            return True
        seen.add(i)
      return False