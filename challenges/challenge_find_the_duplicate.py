def count_occurrences(nums):
    count_dict = {}
    for item in nums:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def is_valid_input(nums):
    if nums is None or len(nums) <= 1 or any(
        not isinstance(item, int) or item < 0 for item in nums
    ):
        return False
    return True


def find_duplicate(nums):
    if not is_valid_input(nums):
        return False

    count_dict = count_occurrences(nums)

    max_value = max(count_dict.values())
    if max_value <= 1:
        return False

    major_key = max(count_dict, key=count_dict.get)
    return major_key

# find_duplicate([1, 3, 4, 2, 2])
# find_duplicate([3, 1, 3, 4, 2])
# find_duplicate([3, 1, 2, 4, 6, 5, 7, 7, 7, 8])
