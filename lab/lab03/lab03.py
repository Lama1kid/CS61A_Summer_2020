HW_SOURCE_FILE=__file__


def pascal(row, column):
    """Returns a number corresponding to the value at that location
    in Pascal's Triangle.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 4 (1 3 3 1), 3rd entry
    3
    """
    "*** YOUR CODE HERE ***"
    # deal with Empty entry
    if column > row:
        return 0
    # define the algorithm
    def cal_next_row(pre_sequence):
        next_sequence = [1]
        for i in range(1, len(pre_sequence) + 1): # end is not inclued
            # how to deal with index exceed?
            # initialize next_sequence by preset index0 num 1, and begin iteration in index1
            try:
                next_sequence.append(pre_sequence[i] + pre_sequence[i-1])
            except IndexError: # deal with the end num
                next_sequence.append(1)
        return next_sequence

    # initialize the first column
    pre_sequence = [1]
    # iterate for row times
    for i in range(row):
        # how can I keep track of pre_sequence?
        pre_sequence = cal_next_row(pre_sequence)
    return pre_sequence[column]

def pascal(row, column):
    """Return value in the position (row, column) (start with 0) of Pascal triangle"""
    if column == 0:
        return 1
    if column == row:
        return 1
    elif row < column: # empty entry
        return 0
    else:
        return pascal(row - 1, column) + pascal(row - 1, column - 1)

def compose1(f, g):
    """"Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def repeated(f, n):
    """Return the function that computes the nth application of func (recursively!).

    >>> add_three = repeated(lambda x: x + 1, 3)
    >>> add_three(5)
    8
    >>> square = lambda x: x ** 2
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> repeated(square, 0)(5)
    5
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'repeated',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    # base case
    if n == 0:
        return lambda x: x

    # conceive recursion call
    return compose1(repeated(f, n - 1), f)


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # base case
    if x == 0:
        return 0
    # recursive call
    return num_eights(x // 10) + (x % 10 == 8)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    """ if last switch is switching direction to down, num = pre_num - 1, vise versa
        but How do I know the current direction?
        In other words, the recursive call depends on the current direction,
        but I don't know how to determine the current direction
        count satisfied times needs assignment statement that I'm not allowed to use
    """
    def helper(i, state, direction):
        # i represents current index
        if i == n: # the end
            return state
        elif num_eights(i) or i % 8 == 0:
            # go to reverse direction
            return helper(i + 1, state - direction, direction * -1)
        else:
            # go forward
            return helper(i + 1, state + direction, direction)

    return helper(1, 1, 1)

