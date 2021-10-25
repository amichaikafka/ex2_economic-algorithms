def is_leximin_better(x: list, y: list) -> bool:
    """
    return true iff x is leximin-better than y.
    :param x:
    :param y:
    :return:
    >>> is_leximin_better([50,50],[50,100])
    False
    >>> is_leximin_better([3,1,3],[1,2,99])
    True
    >>> is_leximin_better([1,1,1,1,1,1,1],[1,1,1,1,1,1,2])
    False
    >>> is_leximin_better([1,1,1,1,1,1,2],[1,1,1,1,1,1,1])
    True
    >>> is_leximin_better([1,1,1,1,1,1,1],[1,1,1,1,1,1,1])
    False
    >>> is_leximin_better([100,4,99,3],[7,4,10,33])
    False
    >>> is_leximin_better([9.99,2,7,20.1,21],[10,2,22.9,21,6.99])
    True
    >>> is_leximin_better([0,0,0,0,0,0,0,0,0,0,0,0,2],[0,0,0,0,0,0,0,0,0,0,0,0,0])
    True
    >>> is_leximin_better([5.0],[5])
    False
    >>> is_leximin_better([3.5],[2.9])
    True
    >>> is_leximin_better([1],[2])
    False
    >>> is_leximin_better([5,4.2,3.1,2,1,0],[5,4.2,3.1,2,1,1])
    False
    >>> is_leximin_better([5,4,3,2,1,1],[5,4,3,2,1,0])
    True
    >>> is_leximin_better([100,4.1,99,3.9],[7,4,10,33])
    False
    >>> is_leximin_better([55,6,44,3,99],[100,200,300,2,400])
    True
    >>> is_leximin_better([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    False
    >>> is_leximin_better([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    True
    >>> is_leximin_better([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
    False
    >>> is_leximin_better([1,2,4,8,16,32,64],[64,32,16,8,4,2,1])
    False
    >>> is_leximin_better([1,2,4,8,16,32,64],[64,32,16,8,4,2,0])
    True

    """

    x.sort()
    y.sort()
    m_lst = tuple(zip(x, y))
    for i, j in m_lst:
        if i != j:
            if i < j:
                return False
            else:
                return True
    return False

if __name__ == "__main__":
    import doctest
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

