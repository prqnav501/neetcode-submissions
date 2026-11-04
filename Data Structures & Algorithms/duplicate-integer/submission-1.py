class Solution:
    def hasDuplicate(self, num: List[int]) -> bool:
      seen = set()
      for x in num:
        if x in seen:
          return True
        seen.add(x)
      return False