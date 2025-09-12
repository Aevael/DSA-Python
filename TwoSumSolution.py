class Solution(object):
    def twoSum(self, nums, target):
        values_map = {}
        for index, current_value in enumerate(nums):
            x = target - current_value
            if x in values_map:
                return [index, values_map[x] ]
            else:
                values_map.update({current_value : index})
        return null