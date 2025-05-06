def find_difference(numbers):
    """
    Finds the difference between the largest and smallest numbers in the list.

    Args:
        numbers: the list of integers

    Returns:
        the difference between the largest and smallest numbers
    """
    small = numbers[0]
    large = numbers[1]
    if small > large:
        large = numbers[0]
        small = numbers[1]


    for i in range(2, len(numbers)):
        if numbers[i] > large:
            large = numbers[i]
        elif numbers[i] < small:
            small = numbers[i]
    return large - small


if __name__ == '__main__':
    sample_list = [10, 3, 5, 6, 20, -2]
    difference = find_difference(sample_list)
    print(difference)  # 22 should be printed