main_list = []

def flatten_list(nested_list):
    """
    Flattens a nested list into a single list of integers.

    Args:
        nested_list: the input nested list

    Returns:
        a flat list containing all integers from the nested structure
    """
    # hint: isinstance()
    global main_list
    for i in range(len(nested_list)):
        if isinstance(nested_list[i], list):
            return_flat_list(nested_list[i])
        else:
            main_list.append(nested_list[i])

    new_list = main_list
    main_list = []
    return new_list

def return_flat_list(nested):
    for i in range(len(nested)):
        if isinstance(nested[i], list):
            return_flat_list(nested[i])
        else:
            main_list.append(nested[i])



if __name__ == '__main__':
    nested_list = [
        1,
        [2, 3],
        [4, [5, 6]],
        7
    ]

    flat_list = flatten_list(nested_list)

    print(f"Flattened list: {flat_list}")  # Should be [1, 2, 3, 4, 5, 6, 7]