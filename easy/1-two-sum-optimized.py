class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_list = {}
        for i in range(len(nums)):
            if target - nums[i] in map_list.keys():
                return [map_list[target - nums[i]],i]
            map_list[nums[i]] = i
