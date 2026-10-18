class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size = 2 * len(nums) + 1
        hash_table = [[] for _ in range(size)]

        for n in nums:
            index = n % size
            bucket = hash_table[index]

            for value in bucket:
                if value == n:
                    return True

            bucket.append(n)

        return False