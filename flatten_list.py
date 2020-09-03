def is_list_or_tuple(elem):
    """ Returns true iff the elem is a list or a tuple. """
    return isinstance(elem, list) or isinstance(elem, tuple)

def recursion(to_flatten, result):
    """ 
    Appends list element to result list if it's not a list or tuple.
    Otherwise goes one level deeper until a shallow list is reached.
    """
    for elem in to_flatten:
        if is_list_or_tuple(elem):
            recursion(elem, result)     # go one level deeper  
        else:
            result.append(elem) # we reached a non-list and non-tuple element


def flatten_iterable(to_flatten):
    """
    Flatten a nested list into a non-nested list recursively.
    """
    result = list()
    # Now let's execute on the input:
    if is_list_or_tuple(to_flatten):    # input is a nested list
        recursion(to_flatten, result)
    else:                               # input is not actually a list
        result.append(to_flatten)
    return result

if __name__ == "__main__":
    a = [(1,2), ("string", ("other string", "yet another")), [1, 10, [100, 1000, [10000, 100000]]], "hello"]
    b = flatten_iterable(a)
    print(b)
