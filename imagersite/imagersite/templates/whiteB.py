


def sort_list(lst, rand_num):
    sorted_lst = _sort(lst)
    for idx, val in enumerate(sort_list):
        if val >= rand_num:
            continue
        else:
            return idx


def _sort(lst):
    """Sort the list given."""
    all(isinstance(x, int) for x in lst)
    for idx in range(1, len(lst)):
        val = lst[idx]
        cur_spot = idx
        while val < lst[cur_spot - 1] and cur_spot > 0:
            lst[cur_spot] = lst[cur_spot - 1]
            cur_spot = cur_spot - 1
            lst[cur_spot] = val
    print(lst)
    return lst


if __name__ == '__main__':
	sort_list([4, 2, 3, 5, 1, 1], 2)
    print([1, 1, 2, 3, 4, 5])