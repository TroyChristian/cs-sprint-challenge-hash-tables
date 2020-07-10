def has_negatives(a):
    positive_nums = {}
    for i in a:
        if i > 0 and -i in a:
            positive_nums[i] = -i

    result = list(positive_nums.keys())
    return result

    


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
