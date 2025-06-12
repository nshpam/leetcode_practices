class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 1st optimization => using one-pass hash
        # map_list = {}
        # for i in range(len(nums)):
        #     if target - nums[i] in map_list.keys():
        #         return [map_list[target - nums[i]],i]
        #     map_list[nums[i]] = i

        # 2nd optimization => more readable variables and slightly faster
        # E.g. map_list => nums_to_index
        # change from in+dict.keys to in+dict because if faster
        # nums_to_index = {}
        # for i, num in enumerate(nums):
        #     x = target-num
        #     if x in nums_to_index:
        #         return [i , nums_to_index[x]]
        #     nums_to_index[num] = i

        # 3rd optimization => more readable variables and change index array sequence into decreasing order
        # E.g. x => complement
        # E.g. return [i , nums_to_index[x]] => return [nums_to_index[complement] , i]
        nums_to_index = {}
        for i, num in enumerate(nums):
            complement = target-num
            if complement in nums_to_index:
                return [nums_to_index[complement] , i]
            nums_to_index[num] = i
