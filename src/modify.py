def squares_of(nums):
    result = []
    for num in nums:
        result.append(num * num)
    return result


def sorted_names(users):
    users.sort(key=lambda user: user["name"])
    return users
