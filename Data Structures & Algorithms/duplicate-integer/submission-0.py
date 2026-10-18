class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size = len(nums) + 1
        table = [[] for _ in range(size)]

        for n in nums:
            index = n % size
            bucket = table[index]

            for value in bucket:
                if value == n:
                    return True

            bucket.append(n)

        return False
        