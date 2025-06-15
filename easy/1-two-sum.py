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


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        method #1 for loop => O(n^2)
        [2,7,15,11,15] => 22
           ^i
             ^j
        Time complexity => O(n)

        method #2 hash map
        [2,7,15,11,15] => 22
              ^
        current + y = 22
        y = 22-current

        {
            2:0,
            7:1,
        }
        [1,2]
        """

        # dict storing hash map
        result = {nums[0]:0}
        # loop
        for i in range(1,len(nums)):
            # find the complement of the current number
            complement = target - nums[i]
            # check the complement with the key in the hash table
            if complement in result:
                # print([result[complement],i])
                return [i,result[complement]]
            result[nums[i]] = i
