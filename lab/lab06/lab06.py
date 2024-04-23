this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    counter = -1
    def adder(b):
        nonlocal a, counter
        counter += 1
        return a + b + counter
    return adder


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    # How can I distinguish it is the first time or the second time calling function? 
    # make a nonlocal variable called counter
    # local state is the preceding two number plus counter
    n, m = 0, 1 # the first two number
    counter = 0
    def return_fib():
        nonlocal n, m, counter
        # it's hardcore
        if counter == 0:
            counter += 1
            return 0
        elif counter == 1:
            counter += 1
            return 1
        else:
            counter += 1
            n, m = m, n + m # change the local state
            return m # m is the next number now
    return return_fib


def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    # current index I'm in
    index = 0
    # find the entry in lst
    while index < len(lst):
        if entry == lst[index]:
            # Find
            # utilize list method - insert
            index += 1
            lst.insert(index, elem) # index is one after the index where entry is on
            index += 1 # move on to skip checking what you have just inserted
        else:
            index += 1
    return lst

